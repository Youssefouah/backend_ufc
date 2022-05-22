# Generated by Django 4.0.4 on 2022-05-22 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('respond', '0010_alter_social_option_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='social_option',
            name='url',
        ),
        migrations.AddField(
            model_name='social_option',
            name='url_web',
            field=models.URLField(blank=True),
        ),
    ]
