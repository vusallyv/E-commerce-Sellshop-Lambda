# Generated by Django 3.2.7 on 2021-09-29 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ManyToManyField(related_name='Wishlist_Product', to='product.ProductVersion')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_Wishlist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ManyToManyField(related_name='Cart_Product', to='product.ProductVersion')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_Cart', to=settings.AUTH_USER_MODEL)),
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
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='User_Billing', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
