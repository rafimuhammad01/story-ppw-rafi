"""ppw_story URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('story4.urls')),
    path('story1/', include('story1.urls', namespace='story1')),
    path('story3/', include('story2.urls', namespace='story2')),
    path('story5/', include('story5.urls', namespace='story5')),
    path('story6/', include('story6.urls', namespace='story6')),
    path('story7/', include('story7.urls', namespace='story7')),
    path('story8/', include('story8.urls', namespace='story8')),
    path('story9/', include('story9.urls', namespace='story9')),
]
