# Generated by Django 5.1.2 on 2024-12-20 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderr_basic_infos_app', '0007_alter_rating_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]