from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from mailing_service.forms import CustomerForm
from mailing_service.models import Customers


class CustomersListView(generic.ListView):
    model = Customers
    template_name = 'mailing_service/customers_table.html'

    def get_queryset(self):
        # if self.request.user.is_superuser:
        if self.request.user.is_superuser or self.request.user.groups.filter(name='Менеджеры').exists():

            # Если пользователь является суперпользователем, выводим все созданные рассылки
            return self.model.objects.all()

        else:
            # Иначе фильтруем рассылки только по текущему пользователю
            return self.model.objects.filter(customer_owner=self.request.user)


class CustomerCreateView(generic.CreateView):
    form_class = CustomerForm
    template_name = 'mailing_service/customer_creating.html'
    success_url = reverse_lazy('mailing_service:customers_list')

    def form_valid(self, form):
        form.instance.customer_owner = self.request.user
        return super().form_valid(form)


class CustomerUpdateView(generic.UpdateView):

    model = Customers
    form_class = CustomerForm
    template_name = 'mailing_service/customer_creating.html'
    success_url = reverse_lazy('mailing_service:customers_list')

    def get_object(self, queryset=None):

        self.object = super().get_object(queryset)
        if self.object.customer_owner != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object


class CustomerDeleteView(generic.DeleteView):
    model = Customers
    template_name = 'mailing_service/customer_delete.html'
    success_url = reverse_lazy('mailing_service:customers_list')


class ToggleAccountStatusView(PermissionRequiredMixin, generic.View):

    permission_required = 'mailing_service.block_user'

    def get(self, request, pk):
        client = get_object_or_404(Customers, id=pk)

        if client.is_active:
            client.is_active = False
        else:
            client.is_active = True

        client.save()

        return redirect(reverse('mailing_service:customers_list'))
