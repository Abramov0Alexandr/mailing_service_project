from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class MailingSettings(models.Model):
    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('active', 'Запущена'),
        ('closed', 'Завершена')
    ]

    FREQUENCY_CHOICES = [
        (None, 'Не указано'),
        ('OPD', 'Раз в день'),
        ('OPW', 'Раз в неделю'),
        ('OPM', 'Раз в месяц')
    ]

    customers = models.ManyToManyField('Customers', verbose_name='Клиенты')

    # Атрибуты для настройки рассылки
    send_time = models.DateTimeField(default=timezone.now, verbose_name='Время рассылки')
    # time = ...

    frequency = models.CharField(
        max_length=3, choices=FREQUENCY_CHOICES, default=None, verbose_name='Периодичность'
    )

    sending_status = models.CharField(
        max_length=7, choices=STATUS_CHOICES, default='created', verbose_name='Статус отправки'
    )

    # Атрибуты для создания письма в рассылке
    message_title = models.CharField(max_length=250, verbose_name='Тема письма')
    message_content = models.TextField(verbose_name='Содержание')

    mailing_owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Создатель рассылки')

    def __str__(self):
        return f'Периодичность: {self.frequency}. Статус отправки: {self.sending_status}'

    class Meta:
        verbose_name = 'Настройка рассылки'
        verbose_name_plural = 'Настройки рассылок'
        ordering = ('pk', 'sending_status')

        permissions = [
            (
                'stop_mailing', 'Stop or run mailing'
            )
        ]
