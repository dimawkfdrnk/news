# Generated by Django 4.1.2 on 2022-11-01 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_parser', '0017_remove_likes_like_likes_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='likes',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
