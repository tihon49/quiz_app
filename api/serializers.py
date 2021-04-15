from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from web_app.models import *
from account.models import User


class UserCreateSerrializer(UserCreateSerializer):
    """создание пользователя"""

    class Meta:
        model = User
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    """ответы"""

    class Meta:
        model = Answer
        fields = ['option']


class QuestionSerializer(serializers.ModelSerializer):
    """вопрос"""

    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['type', 'text', 'answers']


class InterviewSerializer(serializers.ModelSerializer):
    """опрос"""

    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Interview
        fields = ['id', 'slug', 'name', 'description', 'questions']
