# Generated by Django 3.1.3 on 2020-11-30 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0002_auto_20201130_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='No bio!'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]