# Generated by Django 2.1.7 on 2019-10-01 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0006_remove_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, upload_to='media'),
        ),
    ]
