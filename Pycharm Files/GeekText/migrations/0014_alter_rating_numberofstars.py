# Generated by Django 3.2.9 on 2021-11-02 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeekText', '0013_auto_20211102_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='numberOfStars',
            field=models.IntegerField(choices=[('5', '5'), ('2', '2'), ('3', '3'), ('1', '1'), ('4', '4')], default=''),
        ),
    ]