# Generated by Django 4.1.2 on 2022-11-09 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_parser', '0013_alter_authorsarticles_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorsarticles',
            name='moderation_done',
            field=models.BooleanField(default=False, verbose_name='Модерация выполнена'),
        ),
    ]