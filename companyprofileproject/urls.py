from django.contrib import admin
from django.urls import path

from companyProfileApplication.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('services', services_view, name='services'),
]
