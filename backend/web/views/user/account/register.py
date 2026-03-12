from django.contrib.auth.models import User # Django 自带的“用户表模型” 这是“系统用户”的数据结构。
from rest_framework.response import Response # 它会帮你把 Python 的字典 / 列表，自动变成 JSON 发给前端
from rest_framework.views import APIView #一个接口的模板/父类”
from rest_framework_simplejwt.tokens import RefreshToken  #“刷新令牌对象”。 “帮你生成/解析 JWT 的工具类”。

from web.models.user import UserProfile


class RegisterView(APIView):
    def post(self, request):
        try:
            username = request.data['username'].strip()
            password = request.data['password'].strip()
            if not username or not password:
                return Response({
                    'result': '用户名和密码不能为空'
                })
            if User.objects.filter(username=username).exists():
                return Response({
                    'result': '用户名已存在'
                })
            user = User.objects.create_user(username=username, password=password)
            user_profile = UserProfile.objects.create(user=user)
            refresh = RefreshToken.for_user(user)
            response = Response({  #准备要“回给前端”的数据  放在Response 的 JSON 里  放在内存
                'result': 'success',
                'access': str(refresh.access_token),
                'user_id': user.id,
                'username': user.username,
                'photo': user_profile.photo.url,  # 必须加url！！！
                'profile': user_profile.profile,
            })
            response.set_cookie( # 在浏览器 Cookie 里塞一个长期凭证 直接塞进浏览器的 Cookie 里
                key='refresh_token',
                value=str(refresh),
                httponly=True,
                samesite='Lax',
                secure=True,
                max_age=86400 * 7,
            )
            return response
        except:
            return Response({
                'result': '系统异常，请稍后重试'
            })
