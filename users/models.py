from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта', help_text='Введите почту')
    phone = models.CharField(max_length=35, blank=True, null=True, verbose_name='Телефон',
                             help_text='Введите номер телефона')
    city = models.CharField(max_length=150, blank=True, null=True, verbose_name='Город')
    avatar = models.ImageField(upload_to='users/avatars', blank=True, null=True, verbose_name='Аватар')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
