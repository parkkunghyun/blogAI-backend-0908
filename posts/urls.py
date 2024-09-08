from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

# 라우터 인스턴스 생성
router = DefaultRouter()
router.register(r'posts', PostViewSet)  # URL 엔드포인트 등록

# URL 패턴 정의
urlpatterns = [
    path('api/', include(router.urls)),
]
