from django.shortcuts import render
from django.views import View

from .models import *


class HomePageView(View):
    """главная страница"""

    def get(self, request):
        interviews_list = Interview.objects.all()
        template = 'web_app/index.html'
        context = {'objects': interviews_list}

        return render(request, template, context=context)


class InterviewView(View):
    """интервью детально"""

    def get(self, request, interview_slug):
        interview = Interview.objects.get(slug=interview_slug)
        template = 'web_app/interview.html'
        context = {'object': interview}

        return render(request, template, context=context)