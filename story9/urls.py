from django.urls import path

from . import views

app_name = "story8"
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('signup', views.user_signUp, name='signup'),
    path('logout', views.logout_user, name='logout'),
]