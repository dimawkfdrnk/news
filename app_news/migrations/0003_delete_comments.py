# Generated by Django 4.1.2 on 2022-10-29 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0002_alter_comments_news'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
