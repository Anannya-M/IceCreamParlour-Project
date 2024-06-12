from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.home, name='home'),
    path('homepage/', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]
