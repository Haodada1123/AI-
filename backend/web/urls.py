# 配置JWT接口 (urls.py)

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from web.views.index import index
from web.views.user.account.login import LoginView
from web.views.user.account.logout import LogoutView
from web.views.user.account.register import RegisterView

urlpatterns = [
    path('api/user/account/login', LoginView.as_view()),
    path('api/user/account/logout', LogoutView.as_view()),
    path('api/user/account/register', RegisterView.as_view()),
    path('api/user/account/refresh_token', TokenRefreshView.as_view()),

    path('', index),
]