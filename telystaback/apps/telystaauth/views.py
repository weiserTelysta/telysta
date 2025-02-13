from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from  django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from .serializers import UserLoginSerializer,UserRegistrationSerializer


# Create your views here.
class RegisterView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "uid":str(user.id),
                "username":user.username,
                "email":user.email,
            },status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)

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


