# Generated by Django 5.0.7 on 2024-07-21 15:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('company_website', models.CharField(blank=True, max_length=255, null=True)),
                ('company_location', models.CharField(blank=True, max_length=255, null=True)),
                ('logo', models.FileField(blank=True, null=True, upload_to='logo/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'svg'])])),
            ],
        ),
    ]
