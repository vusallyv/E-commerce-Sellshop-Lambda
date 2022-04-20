# Generated by Django 3.2.7 on 2021-11-23 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20211119_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_item',
            name='price',
            field=models.FloatField(default=0.0, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='cart_item',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Quantity'),
        ),
    ]
