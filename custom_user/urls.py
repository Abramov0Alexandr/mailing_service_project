from django.contrib.auth import views as default_views
from django.urls import path
from custom_user import views as customer_views


app_name = 'custom_user'

urlpatterns = [
    path('login/', default_views.LoginView.as_view(template_name='custom_user/log_in.html'), name='log_in'),
    path('logout/', default_views.LogoutView.as_view(template_name='custom_user/log_out.html'), name='log_out'),

    path('registration/', customer_views.UserRegistrationView.as_view(), name='registration'),

    path('registration/verify', customer_views.EmailConfirmView.as_view(), name='email_confirm'),
    path('verify/<key>/', customer_views.EmailConfirmView.as_view(), name='email_confirm'),
    path('registration/verify/email-confirm', default_views.TemplateView.as_view(
        template_name='custom_user/success_verify.html'),name='success_verify'),
]
