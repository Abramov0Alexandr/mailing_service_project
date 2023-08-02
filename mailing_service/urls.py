from django.urls import path
from django.views.generic import TemplateView
from mailing_service import views as custom_views


app_name = 'mailing_service'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='homepage'),
    path('mailing-menu/', custom_views.MailingMenuView.as_view(), name='mailing_menu'),

    # Ссылки для работы с моделью Customers
    path('mailing-menu/users', custom_views.CustomersListView.as_view(), name='customers_list'),
    path('mailing-menu/users/create', custom_views.CustomerCreateView.as_view(), name='customer_create'),
    path('mailing-menu/users/update/<int:pk>', custom_views.CustomerUpdateView.as_view(), name='customer_update'),
    path('mailing-menu/users/delete/<int:pk>', custom_views.CustomerDeleteView.as_view(), name='customer_delete'),
    path('mailing-menu/users/block-unblock/<int:pk>', custom_views.ToggleAccountStatusView.as_view(), name='toggle_account'),

    # Ссылки для работы с моделью MailingSettings
    path('mailing-settings/', custom_views.MailingSettingsListView.as_view(), name='mail_settings_table'),
    path('mailing-settings/create', custom_views.MailingSettingsCreateView.as_view(), name='mail_settings_create'),
    path('mailing-settings/detail/<int:pk>', custom_views.MailingSettingsDetailView.as_view(), name='mail_settings_detail'),
    path('mailing-settings/delete/<int:pk>', custom_views.MailingSettingsDeleteView.as_view(), name='mail_settings_delete'),
    path('mailing-settings/stop-run/<int:pk>', custom_views.ToggleSendingStatusView.as_view(), name='toggle_mail_settings_status'),

    # Ссылка для просмотра логов рассылок
    path('message-logs/', custom_views.MessagesLogsListView.as_view(), name='message_logs'),
]
