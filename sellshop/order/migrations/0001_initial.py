# Generated by Django 3.2.7 on 2021-10-04 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ManyToManyField(related_name='Product_wishlist', to='product.ProductVersion')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Max 30 char.', max_length=30, verbose_name='First name')),
                ('last_name', models.CharField(help_text='Max 30 char.', max_length=30, verbose_name='Last name')),
                ('phone_number', models.CharField(help_text='Max 30 char.', max_length=30, verbose_name='Phone number')),
                ('company_name', models.CharField(help_text='Max 255 char.', max_length=255, verbose_name='Company name')),
                ('country', models.CharField(max_length=255, verbose_name='Country')),
                ('state', models.CharField(max_length=255, verbose_name='State')),
                ('city', models.CharField(max_length=255, verbose_name='City')),
                ('address', models.TextField(verbose_name='Address')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_Shipping', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ManyToManyField(related_name='Product_Cart', to='product.ProductVersion')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(help_text='Max 255 char.', max_length=255, verbose_name='Company name')),
                ('country', models.CharField(max_length=255, verbose_name='Country')),
                ('state', models.CharField(max_length=255, verbose_name='State')),
                ('city', models.CharField(max_length=255, verbose_name='City')),
                ('address', models.TextField(verbose_name='Address')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_Billing', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
