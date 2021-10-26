# Generated by Django 3.2.8 on 2021-10-22 20:55

from django.db import migrations, models
import django.db.models.deletion
from orders.utils import validation_stock, validation_six_digits


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.FloatField(blank=True)),
                ('listing_price', models.FloatField(blank=True)),
                ('stock', models.IntegerField(validators={validation_stock})),
                ('short_description', models.TextField(max_length=150)),
                ('product_number', models.PositiveIntegerField(blank=True, unique=True, validators=[validation_six_digits])),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('total', models.FloatField(blank=True)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('order_number', models.CharField(blank=True, max_length=12, unique=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.product')),
            ],
        ),
    ]
