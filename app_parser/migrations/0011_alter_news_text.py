# Generated by Django 4.1.2 on 2022-10-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_parser', '0010_alter_news_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='text',
            field=models.TextField(),
        ),
    ]
