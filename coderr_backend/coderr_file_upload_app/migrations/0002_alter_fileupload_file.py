# Generated by Django 5.1.2 on 2024-12-18 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderr_file_upload_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]