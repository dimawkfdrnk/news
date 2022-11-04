from django.urls import path

from . import views


urlpatterns = [
    path('registration_user', views.registration_user, name='registration_user'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name= 'logout_user'),
]