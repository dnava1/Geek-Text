# Generated by Django 3.2.9 on 2021-11-02 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeekText', '0006_rating_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='numberOfStars',
            field=models.IntegerField(choices=[('4', '4'), ('3', '3'), ('1', '1'), ('2', '2'), ('5', '5')], default='1', max_length=1),
        ),
    ]