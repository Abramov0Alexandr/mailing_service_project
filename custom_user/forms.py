from django.contrib.auth.forms import UserCreationForm
from django import forms

from custom_user.models import CustomUser


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegistrationForm(StyleFormMixin, UserCreationForm):

    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email'}))

    class Meta:
        model = CustomUser
        fields = ('email', 'fullname', 'avatar')

    def clean_email(self):
        email = self.cleaned_data['email']
        return email.lower()
