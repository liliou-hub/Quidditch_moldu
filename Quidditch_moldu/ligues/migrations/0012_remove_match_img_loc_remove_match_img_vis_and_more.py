# Generated by Django 4.1.4 on 2022-12-12 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligues', '0011_match_img_loc_match_img_vis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='img_loc',
        ),
        migrations.RemoveField(
            model_name='match',
            name='img_vis',
        ),
        migrations.AddField(
            model_name='equipe',
            name='points',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]
