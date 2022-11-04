# Generated by Django 4.1.2 on 2022-11-01 08:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_parser', '0016_alter_comments_news_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='like',
        ),
        migrations.AddField(
            model_name='likes',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]