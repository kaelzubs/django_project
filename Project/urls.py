"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from proj1 import views as proj1_views

from django.conf.urls import handler404, handler500


urlpatterns = [

    path('', include('proj1.urls')),
    path('three/', include('proj2.urls')),
    path('five/', include('proj3.urls')),
    path('ten/', include('proj4.urls')),
    path('disclaimer/', include('proj5.urls')),
    path('about/', include('proj6.urls')),
    path('contact/', include('proj7.urls')),
    path('robots.txt/', include('robots.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = proj1_views.handler404
handler500 = proj1_views.handler500