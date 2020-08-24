from django.urls import include, path

from . import views
urlpatterns = [
    path('reset-password/', views.admin_send_reset_password_email, name='backend.admin_send_reset_password_email'),
    path('confirm-reset-password', views.admin_reset_password, name='backend.admin_reset_password'),
]