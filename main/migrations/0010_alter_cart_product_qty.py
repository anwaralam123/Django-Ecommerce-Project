# Generated by Django 5.0 on 2024-04-18 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_cart_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product_qty',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
