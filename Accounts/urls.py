from django.urls import path
from . import views
from django.conf.urls import handler404
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('settings/', views.settings, name='settings'),
    path('logout/', views.logout, name='logout')
]
