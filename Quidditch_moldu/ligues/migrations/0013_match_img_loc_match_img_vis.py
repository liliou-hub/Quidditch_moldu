# Generated by Django 4.1.4 on 2022-12-13 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligues', '0012_remove_match_img_loc_remove_match_img_vis_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='img_loc',
            field=models.CharField(default='img_loc', max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='img_vis',
            field=models.CharField(default='img_vis', max_length=100),
        ),
    ]
