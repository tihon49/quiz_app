from django.shortcuts import render, redirect
from django.views import View
from unidecode import unidecode
from django.template import defaultfilters

from .models import *
from .forms import InterviewForm


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

    def post(self, request, interview_slug):
        print(request.user)
        print(request.POST)

        return redirect('home-page')


class InterviewCreateView(View):
    """создать новый опрос"""

    def get(self, request):
        template = 'web_app/create_interview.html'
        form = InterviewForm()
        context = {'form': form}

        return render(request, template, context=context)

    def post(self, request):
        template = 'web_app/create_interview.html'
        bound_form = InterviewForm(request.POST)

        if bound_form.is_valid():
            new_interview = bound_form.save(commit=False)
            # создаем slug на английском языке
            new_interview.slug = defaultfilters.slugify(unidecode(new_interview.name))
            new_interview.save()

        return redirect('home-page')
