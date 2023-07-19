from django.urls import reverse_lazy
from django.views import generic
from mailing_service.forms import CustomerForm
from mailing_service.models import Customers


class CustomersListView(generic.ListView):
    model = Customers
    template_name = 'mailing_service/customers_table.html'


class CustomerCreateView(generic.CreateView):
    form_class = CustomerForm
    template_name = 'mailing_service/customer_creating.html'
    success_url = reverse_lazy('mailing_service:customers_list')


class CustomerUpdateView(generic.UpdateView):
    model = Customers
    form_class = CustomerForm
    template_name = 'mailing_service/customer_creating.html'
    success_url = reverse_lazy('mailing_service:customers_list')


class CustomerDeleteView(generic.DeleteView):
    model = Customers
    template_name = 'mailing_service/customer_delete.html'
    success_url = reverse_lazy('mailing_service:customers_list')
