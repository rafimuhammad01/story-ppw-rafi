from django.urls import path

from . import views

app_name = 'story8'

urlpatterns = [
    path('', views.index, name='index'),
    path('data/', views.data, name='data')
]