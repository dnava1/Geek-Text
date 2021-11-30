# Generated by Django 3.2.9 on 2021-11-02 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeekText', '0011_alter_rating_numberofstars'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={'ordering': (['numberOfstars'],)},
        ),
        migrations.AlterField(
            model_name='rating',
            name='numberOfStars',
            field=models.IntegerField(choices=[('4', '4'), ('3', '3'), ('5', '5'), ('1', '1'), ('2', '2')], default=''),
        ),
        migrations.AlterField(
            model_name='rating',
            name='review',
            field=models.TextField(default='', help_text='Your review here...', max_length=250),
        ),
    ]