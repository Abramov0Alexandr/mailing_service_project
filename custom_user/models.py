from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class CustomUser(AbstractUser):

    USER_STATUS = [
        (True, 'Активирован'),
        (False, 'Не активирован')
    ]

    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    fullname = models.CharField(max_length=100, verbose_name='ФИО пользователя')
    avatar = models.ImageField(upload_to=f'users', verbose_name='Аватар', **NULLABLE)

    is_active = models.BooleanField(default=False, verbose_name='Статус активации')
    verification_key = models.CharField(default='Не верифицирован', verbose_name='Ключ активации')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        self.email = self.email.lower()  # преобразование email в нижний регистр
        super().save(*args, **kwargs)
