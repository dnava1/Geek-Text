# Generated by Django 3.2.8 on 2021-11-01 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GeekText', '0004_auto_20211101_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='image',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='slug',
        ),
    ]