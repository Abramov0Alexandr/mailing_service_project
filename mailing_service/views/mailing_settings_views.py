from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from mailing_service.forms import MailingSettingsForm
from mailing_service.models import MailingSettings


class MailingMenuView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'mailing_service/mailing_menu.html'


class MailingSettingsListView(generic.ListView):
    model = MailingSettings
    template_name = 'mailing_service/mail_settings_table.html'


class MailingSettingsCreateView(generic.CreateView):
    form_class = MailingSettingsForm
    template_name = 'mailing_service/mail_settings_create.html'
    success_url = reverse_lazy('mailing_service:mail_settings_table')


class MailingSettingsDetailView(generic.DetailView):
    model = MailingSettings
    template_name = 'mailing_service/mail_settings_detail.html'


class MailingSettingsDeleteView(generic.DeleteView):
    model = MailingSettings
    template_name = 'mailing_service/mail_settings_delete.html'
    success_url = reverse_lazy('mailing_service:mail_settings_table')

