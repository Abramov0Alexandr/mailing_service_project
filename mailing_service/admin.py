from django.contrib import admin
from mailing_service.models import Customers, MailingSettings, SendingMessage, MessagesLogs


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):

    list_display = ('pk', 'first_name', 'surname', 'patronymic', 'email',)
    list_display_links = ('first_name', 'surname', 'patronymic',)
    search_fields = ('email',)


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):

    list_display = ('pk', 'send_time', 'frequency', 'sending_status',)
    list_display_links = ('pk',)
    list_editable = ('frequency', 'sending_status',)
    list_filter = ('frequency', 'sending_status',)


@admin.register(SendingMessage)
class SendingMessageAdmin(admin.ModelAdmin):

    list_display = ('pk', 'message_title', 'message_content',)
    list_display_links = ('message_title',)
    search_fields = ('message_content',)


@admin.register(MessagesLogs)
class MessagesLogsAdmin(admin.ModelAdmin):

    list_display = ('pk', 'last_attempt_time', 'attempt_status', 'server_response',)
    list_display_links = ('attempt_status',)
    list_filter = ('last_attempt_time', 'attempt_status', 'server_response',)
