# Generated by Django 4.0.4 on 2022-05-22 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('respond', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
