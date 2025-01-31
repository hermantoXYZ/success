from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('forgot-password', views.forgot_password, name='forgot_password'),
    path('dashboard/mahasiswa', views.dashboard_mahasiswa, name='dashboard_mahasiswa'),
    path('profil', views.profil, name='profil'),
]