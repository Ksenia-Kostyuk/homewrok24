from django.db import models

from course.models import Course


class Lesson:
    name = models.CharField(max_length=200, verbose_name='Название')
    descriptions = models.TextField(blank=True, null=True, verbose_name='Описание')
    preview = models.ImageField(upload_to='lesson/preview', blank=True, null=True, verbose_name='Картинка')
    video_url = models. URLField(verbose_name='Ссылка на видеоурок')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
