# Generated by Django 5.0 on 2024-04-18 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_cart_total_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_subtotals',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
