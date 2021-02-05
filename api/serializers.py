from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *


class UserCreateSerrializer(UserCreateSerializer):
    """создание пользователя"""

    class Meta:
        model = User
        fields = '__all__'


class InterviewSerializer(serializers.ModelSerializer):
    """опрос"""

    class Meta:
        model = Interview
        fields = '__all__'


class OptionTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionText
        fields = ['option']


class OptionChooseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionChoose
        fields = ['option']


class QuestionSerializer(serializers.ModelSerializer):
    """вопрос к опросу"""

    option_choose = OptionChooseSerializer(read_only=True, many=True)
    option_text = OptionTextSerializer(required=True, many=True)

    class Meta:
        model = Question
        fields = ['id', 'type', 'option_choose', 'option_text']


class InterviewDetailSerializer(serializers.ModelSerializer):
    """опрос с вопросом в нем"""

    questions = QuestionSerializer(read_only=True, many=True)

    class Meta:
        model = Interview
        fields = ['name', 'description', 'questions']
