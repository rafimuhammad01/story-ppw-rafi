from django.urls import path

from . import views
app_name = "story2"
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about')
]