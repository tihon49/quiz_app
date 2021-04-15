from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Стандартная модель пользователей"""

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Список пользователей'
        ordering = ['id']
