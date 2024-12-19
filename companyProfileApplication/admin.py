from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import *

@admin.register(Services)
class ServicesModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    