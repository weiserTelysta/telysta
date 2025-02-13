from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from  django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

from .models import User
from .serializers import UserLoginSerializer,UserRegistrationSerializer

from .utils.tokens import ActivationTokenManager


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "注册成功，请查收激活邮件！"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivateUserView(APIView):
    def get(self,request,token):
        token_data = ActivationTokenManager.validate_token(token)
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
                    "uid":str(user.id),
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


