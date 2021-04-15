from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import InterviewView, UserBaseInfo

router = SimpleRouter()

router.register('interview', InterviewView, basename='interview')

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),  # /auth/token/login/ to get token
    path('', include('rest_framework.urls')),  # для возможности удобно логиниться через браузер

    path('userBaseInfo/', UserBaseInfo.as_view()),
] + router.urls
