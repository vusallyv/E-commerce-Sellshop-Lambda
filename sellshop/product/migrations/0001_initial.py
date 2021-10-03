# Generated by Django 3.2.7 on 2021-10-01 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
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
                ('rating', models.IntegerField(verbose_name='Rating')),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.brand')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Max 30 char.', max_length=30, unique=True, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Max 30 char.', max_length=30, verbose_name='Title')),
                ('category_id', models.ManyToManyField(related_name='ProductCategory', to='product.Category')),
            ],
            options={
                'verbose_name': 'Subcategory',
                'verbose_name_plural': 'Subcategories',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('name', models.CharField(help_text='Max 30 char.', max_length=30, verbose_name='Name')),
                ('email', models.CharField(help_text='Max 30 char.', max_length=30, verbose_name='Email')),
                ('review', models.CharField(max_length=300, verbose_name='Review')),
                ('rating', models.IntegerField(default=0, verbose_name='Rating')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('color', models.IntegerField(choices=[(1, 'Red'), (2, 'Blue'), (3, 'Black'), (4, 'Green'), (5, 'Yellow'), (6, 'White')], default=1, verbose_name='Color')),
                ('size', models.IntegerField(choices=[(1, 'S'), (2, 'M'), (3, 'L'), (4, 'X'), (5, 'XL'), (6, 'XXL'), (7, '2XL'), (8, '3XL')], default=1, verbose_name='Size')),
                ('is_main', models.BooleanField(verbose_name='Is_main')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('tags', models.ManyToManyField(related_name='products', to='product.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/images', verbose_name='Image')),
                ('productversion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.productversion', verbose_name='Prodcut_ID')),
            ],
        ),
    ]
