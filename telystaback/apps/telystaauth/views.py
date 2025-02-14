from datetime import timedelta

from django.shortcuts import render
from django.utils import timezone
from rest_framework import status, permissions
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from  django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

from django.core.cache import cache
from .models import User
from .serializers import UserLoginSerializer,UserRegistrationSerializer,ResentActivationSerializer

from .utils.tokens import ActivationTokenManager

from django.utils import timezone


# Create your views here.
class RegisterView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        print("Serializer is valid!")
        if serializer.is_valid():
            email =  serializer.validated_data.get('email')

            user = serializer.save()
            print("User created:", user)

            key = f"user:{email}:activation_token_time"
            value = timezone.now().timestamp()  # 使用 Unix 时间戳来表示时间
            cache.set(key, value, timeout=60)

            return Response({"message": "注册成功，请查收激活邮件！"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivateUserView(APIView):
    def get(self,request,token):
        token_data = ActivationTokenManager.validate_activation_token(token)

        if not token_data:
            return Response({"error": "无效或过期的激活链接"}, status=status.HTTP_400_BAD_REQUEST)

        try :
            user  = User.objects.get(uid=token_data['uid'],email=token_data['email'])

            if not user.is_active:
                user.is_active = True
                user.save()
                return Response({"message":"账号激活成功"},status=status.HTTP_200_OK)
            return Response({"message":"账号已经激活"},status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error":"用户不存在"},status.HTTP_404_NOT_FOUND)

class ResentActivationView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = ResentActivationSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            key = f"user:{email}:activation_token_time"

            try :
                user = User.objects.get(email=email)


                last_activation_time = cache.get(key)

                if last_activation_time:
                    last_time = timezone.datetime.fromtimestamp(float(last_activation_time), tz=timezone.utc)
                    time_diff = timezone.now() - last_time
                    if time_diff < timedelta(minutes=1):
                        return Response({"detail": "请等待 1 分钟后再请求重发激活邮件！"},
                                        status=status.HTTP_429_TOO_MANY_REQUESTS)
                else:
                    token = ActivationTokenManager.generate_activation_token(user)

                    value = timezone.now().timestamp()

                    cache.set(key, value, timeout=60)

                    registration_serializer = UserRegistrationSerializer()
                    registration_serializer.send_activation_email(user, token)

                    return Response({"message": "激活邮件已重新发送"}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({"detail": "该邮箱未注册或已经激活"}, status=status.HTTP_404_NOT_FOUND)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token

            return Response({
                "access_token":str(access_token),
                "refresh_token":str(refresh),
                "user":{
                    "uid":str(user.uid),
                    "username":user.username,
                    "email":user.email,
                }
            },status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RefreshTokenView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get('refresh_token')

        if not refresh_token:
            return Response({"detail":"需要刷新令牌"},status=status.HTTP_400_BAD_REQUEST)

        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)
            return Response({"access_token": str(access_token)},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_401_UNAUTHORIZED)

