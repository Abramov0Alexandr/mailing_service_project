from django.db import models
from django.utils import timezone


NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):

    title = models.CharField(max_length=250, verbose_name='Заголовок')
    article_content = models.TextField(verbose_name='Содержимое статьи')
    blog_image = models.ImageField(upload_to='blog', **NULLABLE)
    view_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    published_date = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')

    def __str__(self):
        return f'{self.title} {self.published_date}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'
        ordering = ('published_date',)
