# Generated by Django 4.2.2 on 2023-07-20 09:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingsettings',
            name='send_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время рассылки'),
        ),
        migrations.AlterField(
            model_name='messageslogs',
            name='last_attempt_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время последней попытки'),
        ),
    ]
