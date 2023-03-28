from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import path

from .views import CustomUserViewSet, SignUp

app_name = 'users'

router = DefaultRouter()
router.register('users', CustomUserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path(
        'signup/',
        SignUp.as_view(),
        name='signup',
    ),

    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path(
        'password_reset/',
        PasswordResetView
        .as_view(template_name='users/password_reset_form.html'),
        name='password_reset_form'
    ),
    path(
        'password_reset/done',
        PasswordResetDoneView
        .as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        'logout/',
        LogoutView
        .as_view(template_name='users/loggen_out.html'),
        name='logout'
    ),
    path(
        'Rassword_change/',
        PasswordChangeView
        .as_view(template_name='users/password_change_form.html'),
        name='password_change_form'
    ),
    path(
        'Rassword_change/done/',
        PasswordChangeDoneView
        .as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        'auth/reset/<uidb64>/<token>/',
        PasswordResetConfirmView
        .as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path(
        'auth/reset/done/',
        PasswordResetCompleteView
        .as_view(template_name='users/password_reset_complete..html'),
        name='password_reset_complete.'
    ),
]
