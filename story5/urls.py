from django.urls import path

from . import views
app_name = "story5"
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('update/<int:id>', views.update, name='update'),
    path('detail/<int:id>', views.detail, name='detail')
]