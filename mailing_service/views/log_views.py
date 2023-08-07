from django.views import generic
from mailing_service.models import MessagesLogs


class MessagesLogsListView(generic.ListView):
    model = MessagesLogs
    template_name = 'mailing_service/message_logs.html'
