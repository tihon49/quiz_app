from django.contrib import admin
from web_app.models import *
from account.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'end_date']
    list_filter = ['name', 'start_date', 'end_date']
    # автоматическая генерация поля slug при заполнении поля name
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'type', 'interview']
    list_filter = ['type', 'interview']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['option', 'question']
    list_filter = ['question']
