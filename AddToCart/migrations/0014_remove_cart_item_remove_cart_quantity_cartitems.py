# Generated by Django 4.0.6 on 2022-07-22 05:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPortal', '0004_remove_worships_price_currency_alter_worships_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AddToCart', '0013_cart_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='item',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('total_items', models.PositiveIntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AddToCart.cart')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AdminPortal.worships')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
