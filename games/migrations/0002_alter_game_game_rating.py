# Generated by Django 3.2.4 on 2021-10-13 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_rating',
            field=models.CharField(choices=[('unrated', 'Unrated'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='unrated', max_length=40),
        ),
    ]
