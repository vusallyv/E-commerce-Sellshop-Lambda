# Generated by Django 3.2.7 on 2021-09-23 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Max 30 char.', max_length=30, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('creator', models.CharField(help_text='Max 30 char.', max_length=30, verbose_name='Creator')),
                ('created_at', models.DateField(verbose_name='Created_at')),
                ('like', models.IntegerField(verbose_name='Like')),
            ],
        ),
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
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.IntegerField(verbose_name='Description')),
                ('created_at', models.DateField(verbose_name='Created_at')),
                ('blog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.blog')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Max 30 char.', max_length=30, verbose_name='Title')),
                ('subtitle', models.CharField(help_text='Max 30 char.', max_length=30, verbose_name='Subtitle')),
                ('ex_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ex Price')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Rating')),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.brand')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Max 30 char.', max_length=30, verbose_name='Title')),
                ('category_id', models.ManyToManyField(related_name='Product_Category', to='product.Category')),
            ],
            options={
                'verbose_name': 'Subcategory',
                'verbose_name_plural': 'Subcategories',
            },
        ),
        migrations.CreateModel(
            name='Self_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.IntegerField(verbose_name='Description')),
                ('created_at', models.DateTimeField(verbose_name='Created_at')),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.comment')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Max 30 char.', max_length=30, verbose_name='Name')),
                ('email', models.CharField(help_text='Max 30 char.', max_length=30, verbose_name='Email')),
                ('review', models.TextField(verbose_name='Review')),
                ('rating', models.IntegerField(verbose_name='Rating')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Product_version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('color', models.IntegerField(choices=[(1, 'red'), (2, 'blue'), (3, 'red'), (4, 'black'), (5, 'green'), (6, 'yellow'), (7, 'white')], default=1, verbose_name='Color')),
                ('size', models.IntegerField(choices=[(1, 'S'), (2, 'M'), (3, 'L'), (4, 'X'), (5, 'XL'), (6, 'XXl'), (7, '2XXl'), (8, '3XXl')], default=1, verbose_name='Size')),
                ('is_main', models.BooleanField(verbose_name='Is_main')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(help_text='Max 255 char.', max_length=255, verbose_name='Image')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='brand_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.brand'),
        ),
        migrations.AddField(
            model_name='blog',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
    ]
