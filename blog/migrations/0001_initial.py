# Generated by Django 4.2.2 on 2023-08-03 13:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('article_content', models.TextField(verbose_name='Содержимое статьи')),
                ('blog_image', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('view_count', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блог',
                'ordering': ('published_date',),
            },
        ),
    ]
