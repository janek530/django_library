# Generated by Django 4.2.2 on 2023-06-08 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_track_number_alter_album_image_alter_album_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='track_number',
            field=models.IntegerField(),
        ),
    ]