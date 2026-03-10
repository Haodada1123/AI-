# 配置JWT接口 (urls.py)

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from web.views.index import index

urlpatterns = [
    # /api/token/
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # /api/token/refresh/
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # /
    path("", index),  # ✅ 去掉括号！
]