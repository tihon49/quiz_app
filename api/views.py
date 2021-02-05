from django.shortcuts import render
from rest_framework.decorators import permission_classes, APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status, viewsets, generics
from rest_framework.response import Response

from .models import Interview
from .serializers import InterviewSerializer, InterviewDetailSerializer


@permission_classes([IsAuthenticated, ])
class UserBaseInfo(APIView):
    """отображения данных пользователя"""

    @staticmethod
    def get(request, *args, **kwargs):
        data = {'user_id': request.user.id,
                'username': request.user.username,
                'email': request.user.email}

        return Response(data)


class InterviewCreateView(generics.CreateAPIView):
    """создание новго опроса"""

    serializer_class = InterviewSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)


class InterviewListView(generics.ListAPIView):
    """все опросы"""

    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    permission_classes = (IsAuthenticated,)


class InterviewDetailView(generics.RetrieveAPIView):
    """
    представление конкретного опроса (по его id)
    """

    queryset = Interview.objects.all()
    serializer_class = InterviewDetailSerializer
    permission_classes = (IsAuthenticated,)
