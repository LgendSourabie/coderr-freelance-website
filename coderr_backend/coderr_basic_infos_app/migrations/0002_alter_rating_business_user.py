# Generated by Django 5.1.2 on 2024-12-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderr_basic_infos_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='business_user',
            field=models.IntegerField(),
        ),
    ]
