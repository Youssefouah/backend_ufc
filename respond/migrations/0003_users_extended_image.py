# Generated by Django 4.0.4 on 2022-06-01 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('respond', '0002_alter_social_profile_socialprofileusername'),
    ]

    operations = [
        migrations.AddField(
            model_name='users_extended',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]
