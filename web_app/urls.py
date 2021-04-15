from django.urls import path

from .views import HomePageView, InterviewView, InterviewCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('<slug:interview_slug>/', InterviewView.as_view(), name='interview'),
    path('interview/create/', InterviewCreateView.as_view(), name='interview_create'),
]
