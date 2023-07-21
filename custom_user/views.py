from random import randint
from django.conf import settings
from django.contrib.auth import login
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from custom_user.forms import UserRegistrationForm
from custom_user.models import CustomUser


class UserRegistrationView(generic.CreateView):
    model = CustomUser
    form_class = UserRegistrationForm
    template_name = 'custom_user/user_registration.html'
    success_url = reverse_lazy('mailing_service:homepage')

    def form_valid(self, form):
        self.object = form.save()
        self.object.verification_key = ''.join([str(randint(0, 9))
                                                for _ in range(10)])

        send_mail(
            subject='Поздравляем с регистрацией',
            message=f'Для завершения регистрации, пожалуйста, перейдите по указанной ссылке '
                    f'http://127.0.0.1:8000/profile/verify/{self.object.verification_key}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )
        return super().form_valid(form)


class EmailConfirmView(generic.TemplateView):

    def get(self, *args, **kwargs):
        key = self.kwargs.get('key')
        user = CustomUser.objects.filter(verification_key=key).first()
        if user:
            user.is_active = True
            user.verification_key = key
            user.save()
            login(self.request, user)
        return redirect('custom_user:success_verify')
