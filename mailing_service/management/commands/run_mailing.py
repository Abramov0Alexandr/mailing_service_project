import os

import django
from django.core.management import BaseCommand

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
import schedule
from mailing_service.schedule_script import opd_mailing, opm_mailing, opw_mailing
from mailing_service.models import MailingSettings


class Command(BaseCommand):
    def handle(self, *args, **options):
        opd_mailing()
        opw_mailing()
        for item in MailingSettings.objects.filter(frequency='OPM'):
            schedule.every().day.at(item.send_time.strftime('%H:%M')).do(opm_mailing)

        try:
            print('Запущен процесс отправки рассылок')
            while True:
                schedule.run_pending()

        except KeyboardInterrupt:
            print('Работа рассылки приостановлена')
