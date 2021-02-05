from django.contrib import admin
from .models import User, Interview, Question, OptionChoose, OptionText


class OptionChooseInQuestion(admin.TabularInline):
    model = OptionChoose
    extra = 0


class OptionTextInQuestion(admin.TabularInline):
    model = OptionText
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date']
    list_filter = ['name', 'start_date', 'end_date']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionChooseInQuestion, OptionTextInQuestion]


@admin.register(OptionChoose)
class OptionChooseAdmin(admin.ModelAdmin):
    list_display = ['option', 'question']
    list_filter = ['option', 'question']


@admin.register(OptionText)
class OptionTextAdmin(admin.ModelAdmin):
    pass
