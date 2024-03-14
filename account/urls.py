from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # # Adres URL logowania i wylogowania.
    # # path('login/', views.user_login, name='login'), # Stary
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Adres URL panelu głównego.
    path('', views.dashboard, name='dashboard'),

    # # Adresy URL przeznaczone do obsługi zmiany hasła.
    # path('password_change/',
    #      auth_views.PasswordChangeView.as_view(),
    #      name='password_change'),
    # path('password_change/done/',
    #      auth_views.PasswordChangeDoneView.as_view(),
    #      name='password_change_done'),
    #
    # # Adresy URL przeznaczone do obsługi procedury zerowania hasła.
    # path('password_reset/',
    #      auth_views.PasswordResetView.as_view(),
    #      name='password_reset'),
    # path('password_reset/done/',
    #      auth_views.PasswordResetDoneView.as_view(),
    #      name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(),
    #      name='password_reset_confirm'),
    # path('reset/done/',
    #      auth_views.PasswordResetCompleteView.as_view(),
    #      name='password_reset_complete'),

    # Adresy URL uwierzytelniania z django zastępujący wszystkie z auth_views.
    path('', include('django.contrib.auth.urls')),

    # Adres URL do rejestracji użytkownika.
    path('register/', views.register, name='register')
]
