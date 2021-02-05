from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),  # /auth/token/login/ to get token
    path('', include('rest_framework.urls')),  # для возможности удобно логиниться через браузер
    path('userBaseInfo/', views.UserBaseInfo.as_view()),
    path('interview/create/', views.InterviewCreateView.as_view()),  # создание нового опроса админом
    path('interview/list/', views.InterviewListView.as_view()),
    path('interview/<int:pk>', views.InterviewDetailView.as_view()),  # детально об опросе
]

urlpatterns += router.urls
