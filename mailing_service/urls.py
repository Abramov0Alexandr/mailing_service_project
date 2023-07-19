from django.urls import path
from django.views.generic import TemplateView
from mailing_service import views as custom_views


app_name = 'mailing_service'

urlpatterns = [
    # Ссылки для работы с моделью Customers
    path('', TemplateView.as_view(template_name='index.html'), name='homepage'),
    path('mailing-menu/', TemplateView.as_view(template_name='mailing_service/mailing_menu.html'), name='mailing_menu'),
    path('mailing-menu/users', custom_views.CustomersListView.as_view(), name='customers_list'),
    path('mailing-menu/users/create', custom_views.CustomerCreateView.as_view(), name='customer_create'),
    path('mailing-menu/users/update/<int:pk>', custom_views.CustomerUpdateView.as_view(), name='customer_update'),
    path('mailing-menu/users/delete/<int:pk>', custom_views.CustomerDeleteView.as_view(), name='customer_delete'),

    # Ссылки для работы с моделью MailingSettings
    path('mailing-settings/', custom_views.MailingSettingsListView.as_view(), name='mail_settings_table'),
    path('mailing-settings/create', custom_views.MailingSettingsCreateView.as_view(), name='mail_settings_create'),
    path('mailing-menu/delete/<int:pk>', custom_views.MailingSettingsDeleteView.as_view(), name='mail_settings_delete'),

]
