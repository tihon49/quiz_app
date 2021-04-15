from django.urls import path

from .views import HomePageView, InterviewView

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('<slug:interview_slug>/', InterviewView.as_view(), name='interview'),
]
