# Generated by Django 3.2.3 on 2021-05-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_top_banner_para'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]