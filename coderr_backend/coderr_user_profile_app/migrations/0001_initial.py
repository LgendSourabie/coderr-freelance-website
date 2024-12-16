# Generated by Django 5.1.2 on 2024-12-15 15:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('tel', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('working_hours', models.CharField(blank=True, max_length=10, null=True)),
                ('type', models.CharField(choices=[('business', 'business'), ('customer', 'customer')], default='customer', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
