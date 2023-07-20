from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class MessagesLogs(models.Model):

    ATTEMPT_STATUS_CHOICES = [
        (None, 'Не указано'),
        ('received', 'Получено'),
        ('failed', 'Провалено')
    ]

    mailing_settings = models.ForeignKey('MailingSettings', on_delete=models.CASCADE, verbose_name='Настройки рассылки')

    last_attempt_time = models.DateTimeField(default=timezone.now, verbose_name='Время последней попытки')

    attempt_status = models.CharField(max_length=8, choices=ATTEMPT_STATUS_CHOICES, verbose_name='Статус попытки',
                                      default=None)

    server_response = models.CharField(max_length=100, **NULLABLE, verbose_name='Ответ сервера')

    def __str__(self):
        return f'Статус попытки: {self.attempt_status}'

    class Meta:
        verbose_name = 'Логи рассылки'
        verbose_name_plural = 'Логи рассылок'
        ordering = ('attempt_status',)
