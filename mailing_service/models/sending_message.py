from django.db import models


class SendingMessage(models.Model):

    mailing_settings = models.ForeignKey('MailingSettings', on_delete=models.CASCADE, verbose_name='Настройки рассылки')
    message_title = models.CharField(max_length=250, verbose_name='Тема письма')
    message_content = models.TextField(verbose_name='Содержание')

    def __str__(self):
        return self.message_title

    class Meta:
        verbose_name = 'Сообщение для рассылки'
        verbose_name_plural = 'Сообщения для рассылки'
        ordering = ('pk',)
