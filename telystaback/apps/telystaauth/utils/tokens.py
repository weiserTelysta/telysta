import uuid
from django.core.cache import cache
from django.conf import settings

class ActivationTokenManager:
    @classmethod
    def generate_activation_token(cls,user):
        """生成激活令牌"""
        token = str(uuid.uuid4())
        key = f"activation:{token}"
        cache.set(key, {
            "uid": str(user.uid),
            "email": user.email,
        }, timeout=settings.ACTIVATION_TOKEN_EXPIRE)

        return token

    @classmethod
    def validate_activation_token(cls, token):
        """验证令牌有效性"""
        key = f"activation:{token}"
        token_data = cache.get(key)
        if token_data:
            cache.delete(key)

        # 获取令牌后删除（一次性令牌）

        return token_data
