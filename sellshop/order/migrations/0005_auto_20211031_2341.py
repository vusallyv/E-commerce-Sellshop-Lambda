# Generated by Django 3.2.7 on 2021-10-31 19:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_initial'),
        ('order', '0004_auto_20211029_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='billing',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wishlist',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(blank=True, to='product.ProductVersion'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='product',
            field=models.ManyToManyField(blank=True, related_name='Product_wishlist', to='product.ProductVersion'),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('quantity', models.IntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_item', to='order.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_product', to='product.productversion')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
