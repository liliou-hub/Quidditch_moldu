# Generated by Django 4.1.4 on 2022-12-11 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligues', '0010_equipe_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='img_loc',
            field=models.CharField(default='img', max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='img_vis',
            field=models.CharField(default='img', max_length=100),
        ),
    ]
