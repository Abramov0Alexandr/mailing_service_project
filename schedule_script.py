from datetime import timedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta
import schedule
from django.core.mail import send_mail
from schedule import repeat, every

from config import settings
from mailing_service.models import MailingSettings, MessagesLogs


def get_next_month_date(current_date):
    next_month = current_date + relativedelta(months=1)
    return next_month


@repeat(every().day)
def opd_mailing():
    for item in MailingSettings.objects.filter(frequency='OPD'):
        if item.sending_status in ('active', 'created'):
            send_mailings(item)
            item.sending_status = 'active'
            item.save()


@repeat(every().week)
def opw_mailing():
    for item in MailingSettings.objects.filter(frequency='OPW'):
        if item.sending_status in ('active', 'created'):
            send_mailings(item)
            item.sending_status = 'active'
            item.save()


def opm_mailing():
    for item in MailingSettings.objects.filter(frequency='OPM'):
        if item.sending_status in ('active', 'created'):
            send_mailings(item)
            item.sending_status = 'active'
            item.save()

            # Вычисляем дату следующего месяца
            next_month_date = get_next_month_date(item.send_time)

            # Запланируем повторение задачи на следующий месяц
            interval = (next_month_date - datetime.now()).total_seconds()
            schedule.every(interval).seconds.do(opm_mailing)


def send_mailings(object: MailingSettings):
    emails = [customers.email for customers in object.customers.all()]
    try:
        send_mail(
            subject=object.message_title,
            message=object.message_content,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=emails
        )
        attempt_status = 'received'
        server_response = '200'

    except Exception as e:

        attempt_status = 'failed'
        server_response = str(e)

    MessagesLogs.objects.create(mailing_settings=object,
                                attempt_status=attempt_status,
                                server_response=server_response)
