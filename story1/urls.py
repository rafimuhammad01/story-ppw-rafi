from django.urls import path

from . import views

app_name = 'story1'

urlpatterns = [
    path('/', views.index, name='index'),
]