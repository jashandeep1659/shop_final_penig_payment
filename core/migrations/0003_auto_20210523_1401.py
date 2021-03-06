# Generated by Django 3.2.3 on 2021-05-23 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_top_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='top_banner',
            name='image_background',
            field=models.ImageField(blank=True, null=True, upload_to='banner/bg_images'),
        ),
        migrations.AddField(
            model_name='top_banner',
            name='images_of_banner',
            field=models.ImageField(blank=True, null=True, upload_to='banner/images'),
        ),
    ]
