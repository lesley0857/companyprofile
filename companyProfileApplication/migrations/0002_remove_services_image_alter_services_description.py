# Generated by Django 4.2.16 on 2024-12-18 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyProfileApplication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='image',
        ),
        migrations.AlterField(
            model_name='services',
            name='description',
            field=models.CharField(max_length=3000, null=True),
        ),
    ]