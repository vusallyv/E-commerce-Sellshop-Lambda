# Generated by Django 3.2.7 on 2022-05-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211119_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default='', max_length=30, unique=True),
            preserve_default=False,
        ),
    ]
