from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Customers(models.Model):
    email = models.EmailField(verbose_name='Почта', unique=True)
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    surname = models.CharField(max_length=20, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=40, verbose_name='Отчество')
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.email} {self.first_name} {self.surname}'

    class Meta:
        verbose_name = 'Клиент сервиса'
        verbose_name_plural = 'Клиенты сервиса'
        ordering = ('pk',)
