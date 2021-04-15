from django.shortcuts import render
from rest_framework.decorators import permission_classes, APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status, viewsets, generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from web_app.models import *
from account.models import User
from .serializers import *


# @permission_classes([IsAuthenticated, ])
class UserBaseInfo(APIView):
    """отображения данных пользователя"""

    @staticmethod
    def get(request, *args, **kwargs):
        data = {'user_id': request.user.id,
                'username': request.user.username,
                'email': request.user.email}

        return Response(data)



class InterviewView(ModelViewSet):
    """CRUD опроса"""

    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    lookup_field = 'slug'
