# Generated by Django 4.0.6 on 2022-07-18 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_remove_userinfo_premium_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='mobile_no',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]