# Generated by Django 4.2.16 on 2024-11-20 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0006_remove_cart_passengers_cart_added_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
    ]
