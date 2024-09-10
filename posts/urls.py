from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import PostViewSet, RegisterView

# 라우터 인스턴스 생성
router = DefaultRouter()
router.register(r'posts', PostViewSet)  # URL 엔드포인트 등록

# URL 패턴 정의
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

     # path('api/login/', LoginView.as_view(), name='login'),
]
