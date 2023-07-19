from django.urls import reverse_lazy
from django.views import generic

from mailing_service.forms import MailingSettingsForm
from mailing_service.models import MailingSettings


class MailingSettingsListView(generic.ListView):
    model = MailingSettings
    template_name = 'mailing_service/mail_settings_table.html'


class MailingSettingsCreateView(generic.CreateView):
    form_class = MailingSettingsForm
    template_name = 'mailing_service/mail_settings_create.html'
    success_url = reverse_lazy('mailing_service:mail_settings_table')


class MailingSettingsDeleteView(generic.DeleteView):
    model = MailingSettings
    template_name = 'mailing_service/mail_settings_delete.html'
    success_url = reverse_lazy('mailing_service:mail_settings_table')

