from django.contrib.auth import views as default_views
from django.urls import path
from custom_user import views as customer_views


app_name = 'custom_user'

urlpatterns = [
    # Вход / Выход из аккаунта
    path('login/', default_views.LoginView.as_view(template_name='custom_user/log_in.html'), name='log_in'),
    path('logout/', default_views.LogoutView.as_view(template_name='custom_user/log_out.html'), name='log_out'),

    # Предварительная регистрация нового пользователя без его активации
    path('registration/', customer_views.UserRegistrationView.as_view(), name='registration'),

    # Активация пользователя после перехода по ссылке из письма
    path('verify/<key>/', customer_views.EmailConfirmView.as_view()),
    path('registration/verify/reg-notification', default_views.TemplateView.as_view(
        template_name='custom_user/reg_notification.html'), name='reg_notification'),
    path('registration/verify/email-confirm', default_views.TemplateView.as_view(
        template_name='custom_user/success_verify.html'), name='success_verify'),
]
