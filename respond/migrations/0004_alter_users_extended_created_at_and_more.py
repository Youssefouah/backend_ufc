# Generated by Django 4.0.4 on 2022-06-01 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('respond', '0003_users_extended_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_extended',
            name='created_At',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='users_extended',
            name='updated_At',
            field=models.DateTimeField(auto_now=True),
        ),
    ]