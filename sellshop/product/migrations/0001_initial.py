# Generated by Django 3.2.7 on 2021-10-04 09:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Max 30 char.', max_length=30, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Max 30 char.', max_length=30, verbose_name='Title')),
                ('subcategory', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='product.category', verbose_name='Subcategory')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Max 30 char.', max_length=30, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('title', models.CharField(help_text='Max 30 char.', max_length=30, verbose_name='Title')),
                ('subtitle', models.CharField(help_text='Max 30 char.', max_length=30, verbose_name='Subtitle')),
                ('ex_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ex Price')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.brand')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=3, verbose_name='Rating')),
                ('is_main', models.BooleanField(default=False, verbose_name='Main')),
                ('color', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.color', verbose_name='Color')),
                ('product', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Max 30 char.', max_length=30, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Max 30 char.', max_length=30, unique=True, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('review', models.TextField(verbose_name='Review')),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='Rating')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 10, 4, 9, 31, 36, 653379, tzinfo=utc), verbose_name='Created_at')),
                ('product', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='product.productversion')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='productversion',
            name='size',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.size', verbose_name='Size'),
        ),
        migrations.AddField(
            model_name='productversion',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='product.Tag'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='media/', verbose_name='Image')),
                ('productversion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productversion', verbose_name='Product Version')),
            ],
        ),
    ]
