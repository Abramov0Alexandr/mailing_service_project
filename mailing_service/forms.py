from django import forms
from mailing_service.models import Customers, MailingSettings


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CustomerForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Customers
        exclude = ('is_active', 'customer_owner',)


class MailingSettingsForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = MailingSettings
        exclude = ('sending_status', 'mailing_owner',)
