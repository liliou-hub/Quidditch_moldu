# Generated by Django 4.1.4 on 2022-12-09 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligues', '0002_joueur_nom_joueur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='nom_match',
            field=models.CharField(default='nom_match', max_length=100),
        ),
    ]
