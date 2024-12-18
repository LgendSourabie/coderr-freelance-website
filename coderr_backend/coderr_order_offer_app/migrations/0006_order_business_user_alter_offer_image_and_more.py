# Generated by Django 5.1.2 on 2024-12-19 22:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderr_order_offer_app', '0005_alter_offer_user_alter_order_customer_user_and_more'),
        ('coderr_user_profile_app', '0004_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='business_user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='business_user_order', to='coderr_user_profile_app.profile'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='uploads/images/'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='coderr_user_profile_app.profile'),
        ),
    ]
