"""Mosere URL Configuration

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(('Accounts.urls', 'Accounts'), namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include(('main.urls','main'), namespace='home')),
    path('clients/', include(('Clients.urls','Clients'), namespace='clients')),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('business/', include(('Business.urls', 'Business'), namespace='business')),
    path('staff/', include(('Staff.urls', 'Staff'), namespace='staff')),
    path('jobs/', include(('Jobs.urls', 'Jobs'), namespace='jobs')),
]


#Custom titles for admin
admin.site.site_header = 'Mosere'
admin.site.index_title = 'Panel de Administrador'
admin.site.site_title = 'Mosere'