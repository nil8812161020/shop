# Generated by Django 2.1.7 on 2019-10-01 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0004_auto_20191001_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_discount',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
