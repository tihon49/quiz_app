from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from multiselectfield import MultiSelectField
from account.models import User


class Interview(models.Model):
    """модель опроса"""

    name = models.CharField('Название', max_length=64)
    slug = models.SlugField('URL (slug)', max_length=100, unique=True)
    description = models.TextField('Описание')
    start_date = models.DateField('Дата старта', auto_now_add=True)
    end_date = models.DateField('Дата окончания', blank=True, null=True)

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
        ordering = ('-start_date',)

    def __str__(self):
        return str(self.name)


class Question(models.Model):
    """вопрос"""

    STATE_CHOICES = (
        ('text', 'ответ текстом'),
        ('single choice', 'ответ с выбором одного варианта'),
        ('multi choice', 'ответ с выбором нескольких вариантов')
    )

    interview = models.ForeignKey(Interview, related_name='questions', on_delete=models.CASCADE)
    type = models.CharField('Тип вопроса', choices=STATE_CHOICES, max_length=120)
    text = models.TextField('Текст вопроса')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text


class Answer(models.Model):
    """ответ"""

    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    option = models.CharField('Вариант ответа', max_length=250)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return str(self.option)
