from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from mailing_service.forms import MailingSettingsForm
from mailing_service.models import MailingSettings, Customers


class MailingMenuView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'mailing_service/mailing_menu.html'


class MailingSettingsListView(generic.ListView):
    model = MailingSettings
    template_name = 'mailing_service/mail_settings_table.html'

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.groups.filter(name='Менеджеры').exists():
            # Если пользователь является суперпользователем, выводим все созданные рассылки
            return self.model.objects.all()

        else:
            # Иначе фильтруем рассылки только по текущему пользователю
            return self.model.objects.filter(mailing_owner=self.request.user)


class MailingSettingsCreateView(generic.CreateView):
    form_class = MailingSettingsForm
    template_name = 'mailing_service/mail_settings_create.html'
    success_url = reverse_lazy('mailing_service:mail_settings_table')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        if self.request.user.is_superuser:
            # Если клиент является суперпользователем, выводим всех имеющихся пользователей
            form.fields['customers'].queryset = Customers.objects.all()
            return form

        else:
            # Иначе фильтруем пользователей только по текущему клиенту
            form.fields['customers'].queryset = Customers.objects.filter(customer_owner=self.request.user)
            return form

    def form_valid(self, form):
        form.instance.mailing_owner = self.request.user
        return super().form_valid(form)


class MailingSettingsDetailView(generic.DetailView):
    model = MailingSettings
    template_name = 'mailing_service/mail_settings_detail.html'

    def get_object(self, queryset=None):

        self.object = super().get_object(queryset)
        if self.object.mailing_owner != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object


class MailingSettingsDeleteView(generic.DeleteView):
    model = MailingSettings
    template_name = 'mailing_service/mail_settings_delete.html'
    success_url = reverse_lazy('mailing_service:mail_settings_table')


class ToggleSendingStatusView(PermissionRequiredMixin, generic.View):

    permission_required = 'mailing_service.stop_mailing'

    def get(self, request, pk):
        mailing = get_object_or_404(MailingSettings, id=pk)

        if mailing.sending_status in ('created', 'active'):
            mailing.sending_status = 'closed'
        else:
            mailing.sending_status = 'active'

        mailing.save()

        return redirect(reverse('mailing_service:mail_settings_table'))
