# Generated by Django 4.0.4 on 2022-05-17 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('respond', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='image',
            field=models.ImageField(blank=True, default='photos/user1.jpeg', null=True, upload_to='photos'),
        ),
    ]
