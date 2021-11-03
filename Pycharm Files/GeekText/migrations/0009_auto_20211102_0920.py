# Generated by Django 3.2.9 on 2021-11-02 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeekText', '0008_alter_rating_numberofstars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='numberOfStars',
            field=models.IntegerField(choices=[('2', '2'), ('4', '4'), ('1', '1'), ('5', '5'), ('3', '3')], default='1'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='review',
            field=models.TextField(default='', max_length=250),
        ),
    ]
