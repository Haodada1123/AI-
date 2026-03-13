import logging

from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from web.models.user import UserProfile

logger = logging.getLogger(__name__)


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = request.data or {}
            username = (data.get("username") or "").strip()
            password = (data.get("password") or "").strip()
            if not username or not password:
                return Response({
                    'result': '用户名和密码不能为空'
                })
            user = authenticate(username=username, password=password)
            if user:  # 用户名密码正确
                try:
                    user_profile = UserProfile.objects.get(user=user)
                except UserProfile.DoesNotExist:
                    return Response({
                        'result': '用户资料未初始化，请联系管理员'
                    })
                photo_url = ''
                if user_profile.photo:
                    try:
                        photo_url = user_profile.photo.url
                    except (ValueError, AttributeError):
                        pass
                refresh = RefreshToken.for_user(user)  # 生成jwt
                response = Response({
                    'result': 'success',
                    'access': str(refresh.access_token),
                    'user_id': user.id,
                    'username': user.username,
                    'photo': photo_url,
                    'profile': user_profile.profile or '',
                })
                response.set_cookie(
                    key='refresh_token',
                    value=str(refresh),
                    httponly=True,
                    samesite='Lax',
                    secure=False,  # 本地 http 开发时设为 False，部署 https 时改为 True
                    max_age=86400 * 7,
                )
                return response
            return Response({
                'result': '用户名或密码错误'
            })
        except Exception as e:
            logger.exception("登录异常")
            return Response({
                'result': '系统异常，请稍后重试'
            })
