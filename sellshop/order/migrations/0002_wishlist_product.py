# Generated by Django 3.2.7 on 2021-11-12 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='product',
            field=models.ManyToManyField(blank=True, related_name='Product_wishlist', to='product.ProductVersion'),
        ),
    ]
