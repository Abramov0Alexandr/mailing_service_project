from django.contrib.auth.forms import UserCreationForm
from custom_user.models import CustomUser


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegistrationForm(StyleFormMixin, UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'fullname', 'avatar')
