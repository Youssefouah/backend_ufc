# Generated by Django 4.0.4 on 2022-06-22 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('respond', '0012_alter_social_profile_urloptionid'),
    ]

    operations = [
        migrations.AddField(
            model_name='urloption',
            name='hint',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]