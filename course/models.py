from django.db import models


class Course:
    name = models.CharField(max_length=200, verbose_name='Название')
    descriptions = models.TextField(blank=True, null=True, verbose_name='Описание')
    preview = models.ImageField(upload_to='lesson/preview', blank=True, null=True, verbose_name='Картинка')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
