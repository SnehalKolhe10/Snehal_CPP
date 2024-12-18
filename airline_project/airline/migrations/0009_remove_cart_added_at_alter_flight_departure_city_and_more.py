# Generated by Django 4.2.16 on 2024-11-24 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0008_cart_passengers_alter_flight_arrival_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='added_at',
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='flight',
            name='flight_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='flight',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='flight',
            name='status',
            field=models.CharField(max_length=20),
        ),
    ]
