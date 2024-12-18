from django.contrib import admin
from django.urls import path

from companyProfileApplication.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', about, name='about'),
    path('contact',contact, name='contact'),
    path('', index_view, name='index'),
    path('projects', projects, name='projects'),
    path('projects/<int:id>/', projects_details, name='projects_details'),
    path('services', services, name='services'),
    path('services/<int:id>/', services_details, name='services_details'),
    path('quote',quote_view, name='quote_mail')
]
