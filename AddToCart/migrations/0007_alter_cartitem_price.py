# Generated by Django 4.0.6 on 2022-07-21 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AddToCart', '0006_cart_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
