from django.core.mail import send_mail
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .utils.tokens import ActivationTokenManager

from telystaback import settings

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, max_length=20, error_messages={
        "min_length": "密码长度需要大于8个字符。",
        "max_length": "密码长度需要小于20个字符。"
    })

    class Meta:
        model = User
        fields = ('email', 'password', 'username')

    def validate_email(self, value):
        """检查邮箱是否已经注册"""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("该邮箱已经被注册。")
        return value

    def create(self, validated_data):
        """创建用户"""
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])  # Hash 密码
        user.is_active = False
        user.save()

        token = ActivationTokenManager.generate_activation_token(user)
        self.send_activation_email(user,token)

        return user

    def send_activation_email(self, user,token):
        """ 发送用户激活邮件 """
        subject = "请激活你的账号"
        activation_link = f"http://your-frontend.com/activate/{token}"  # 假设前端处理激活
        message = f"你好 {user.username}，\n\n请点击以下链接激活你的账号：\n{activation_link}\n\n谢谢！"

        send_mail(
            subject,  # 主题
            message,  # 内容
            settings.DEFAULT_FROM_EMAIL,  # 发送者
            [user.email],  # 接收者
            fail_silently=False,
        )


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, error_messages={"required":"请输入邮箱！"})
    password = serializers.CharField(max_length=20, min_length=6,write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
                # user = User.objects.filter(email=email).first()
            except User.DoesNotExist:
                raise serializers.ValidationError("用户不存在。")
            except User.MultipleObjectsReturned:
                raise serializers.ValidationError("存在多个相同邮箱的用户")

            if not user.check_password(password):
                raise serializers.ValidationError("密码错误。")

        else:
            raise serializers.ValidationError("请传入邮箱或密码")

        attrs['user'] = user

        return attrs