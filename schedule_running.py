import os
import django
# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
import schedule
from schedule_script import opd_mailing, opm_mailing, opw_mailing
from mailing_service.models import MailingSettings


def run_scheduler():
    opd_mailing()
    opw_mailing()
    for item in MailingSettings.objects.filter(frequency='OPM'):
        schedule.every().day.at(item.send_time.strftime('%H:%M')).do(opm_mailing)

    while True:
        schedule.run_pending()


# Ваша точка входа в приложение Django
if __name__ == '__main__':
    run_scheduler()
