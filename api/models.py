from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class User(AbstractUser):
    """Стандартная модель пользователей"""

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Список пользователей'
        ordering = ['id']


class Interview(models.Model):
    """модель опроса"""

    name = models.CharField('Название', max_length=64)
    start_date = models.DateField('Дата старта', auto_now_add=True)
    end_date = models.DateField('Дата окончани', blank=True, null=True)
    description = models.TextField('Описание')

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
        ordering = ('-start_date',)

    def __str__(self):
        return self.name


TYPE_CHOICES = (
    ('текст', 'текст'),
    ('два и более варианта', 'два и более варианта')
)


class Question(models.Model):
    """вопрос к опросу"""

    interview = models.ForeignKey(Interview, verbose_name='Опрос', related_name='questions', on_delete=models.CASCADE)
    text = models.TextField('Текст вопроса')
    type = models.CharField(verbose_name='Тип', choices=TYPE_CHOICES, max_length=256)
    answer_options = models.CharField('Вариант(ы) ответа(ов)', max_length=256)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ('-id',)

    def __str__(self):
        return self.text


class OptionChoose(models.Model):
    """вариант ответа на вопрос выбором"""

    option = models.CharField('вариант ответа', max_length=250)
    question = models.ForeignKey(Question, verbose_name='Вопрос', related_name='option_choose',
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вариант ответа (вывбор)'
        verbose_name_plural = 'Варианты ответа (выбор)'

    def __str__(self):
        return self.option


class OptionText(models.Model):
    """вариант ответа на вопрос текстом"""

    option = models.TextField('вариант ответа')
    question = models.ForeignKey(Question, verbose_name='Вопрос', related_name='option_text', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вариант ответа (текст)'
        verbose_name_plural = 'Варианты ответа (текст)'

    def __str__(self):
        return self.option


# логика при сохранении модели Question #
# 1) source: https://www.youtube.com/watch?v=3wFpyKcVT_w&list=PLSWnD6rL-m9adebgpvvOLH5ASGJiznWdg&index=7  17:25
# 2) source: https://www.youtube.com/watch?v=Kc1Q_ayAeQk
@receiver(post_save, sender=Question)
def question_create_answer_post_save(sender, instance, created, **kwargs):
    """
    функция создания вариантов ответов при сохранении модели Question
    """

    if instance.type == 'текст':
        answer = OptionText.objects.get_or_create(option=instance.answer_options, question=instance)
        print(f'Создана модель с текстовым вариантом ответа: {instance}')
    elif instance.type == 'два и более варианта':
        # разобьем по запятой варианты ответов
        answer_choose = instance.answer_options
        for answer in answer_choose.split(','):
            OptionChoose.objects.get_or_create(option=answer, question=instance)
            print(f'Создана модель с несколькими вариантами ответов: {instance}')
