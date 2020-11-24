from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views


app_name = 'accounts'

urlpatterns = [
    path(
        'profile', 
        views.AccountProfileView.as_view(), name='profile'
    ),
    path(
        'auth/login', 
        auth_views.LoginView.as_view(template_name='accounts/auth/login.html'), 
        name='login'
    ),
    path(
        'auth/login/done', 
        TemplateView.as_view(template_name = 'accounts/auth/login_done.html'),
        name = 'login_done'
    ),
    path(
        'auth/logout', 
        auth_views.LogoutView.as_view(template_name='accounts/auth/logout.html'), 
        name='logout'
    ),
    path(
        'auth/logout/done', 
        TemplateView.as_view(template_name = 'accounts/auth/logout_done.html'),
        name = 'logout_done'
    ),
    path(
        'auth/signup', 
        views.SignupView.as_view(), 
        name = 'signup'
    ),
    path(
        'auth/signup/done', 
        TemplateView.as_view(template_name='accounts/auth/signup_done.html'), 
        name = 'signup_done'
    ),
    path(
        'auth/password_reset/', 
        auth_views.PasswordResetView.as_view(
            template_name='accounts/auth/password_reset.html',
            email_template_name = 'accounts/auth/password_reset_email.html',
            success_url = reverse_lazy('accounts:password_reset_done')
        ), 
        name='password_reset'
    ),
    path(
        'auth/password_reset/done/', 
        auth_views.PasswordResetDoneView.as_view(
            template_name = 'accounts/auth/password_reset_done.html'
        ), 
        name='password_reset_done'
    ),
    path(
        'auth/reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
            template_name = 'accounts/auth/password_reset_confirm.html',
            success_url = reverse_lazy('accounts:password_reset_complete')
        ), 
        name='password_reset_confirm'
    ),
    path(
        'auth/reset/done/', 
        auth_views.PasswordResetCompleteView.as_view(
            template_name = 'accounts/auth/password_reset_complete.html'
        ), 
        name='password_reset_complete'
    ),
    path(
        'auth/password_change/', 
        auth_views.PasswordChangeView.as_view(), 
        name='password_change'
    ),
    path(
        'auth/password_change/done/', 
        auth_views.PasswordChangeDoneView.as_view(), 
        name='password_change_done'
    ),
]
