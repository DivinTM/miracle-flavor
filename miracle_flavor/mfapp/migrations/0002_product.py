# Generated by Django 4.1.7 on 2023-07-17 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mfapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_image', models.ImageField(upload_to='products')),
            ],
        ),
    ]
