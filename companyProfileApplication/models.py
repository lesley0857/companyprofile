from django.db import models
from django_summernote.fields import SummernoteTextField
# Create your models here.

class Services(models.Model):
    name = models.CharField(max_length=150, blank=False)
    description = SummernoteTextField(max_length=3000, blank=False,null=True)
    icon = models.FileField(upload_to='images', null=True, blank=True)
    image = models.FileField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'