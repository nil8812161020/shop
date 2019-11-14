# Generated by Django 2.2.1 on 2019-11-13 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0009_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='number',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='sum_price',
        ),
        migrations.AddField(
            model_name='order',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='is_ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projectapp.Product'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.Order')),
            ],
        ),
    ]
