# Generated by Django 4.1.2 on 2022-10-27 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_parser', '0005_rename_url_news_image_news_text_alter_news_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.SlugField(),
        ),
    ]