# Generated by Django 4.0.8 on 2023-11-25 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('organization', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('order', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('customization', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('organize', models.CharField(max_length=100)),
                ('ph', models.CharField(max_length=15)),
                ('mail', models.EmailField(max_length=254)),
                ('orders', models.CharField(max_length=100)),
                ('types', models.CharField(max_length=100)),
                ('product_customization', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=100)),
            ],
        ),
    ]
