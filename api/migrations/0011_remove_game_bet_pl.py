# Generated by Django 3.2 on 2021-05-02 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_game_bet_pl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='bet_pl',
        ),
    ]
