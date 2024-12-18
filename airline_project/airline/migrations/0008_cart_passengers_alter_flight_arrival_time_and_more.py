# Generated by Django 4.2.16 on 2024-11-21 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0007_flight_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='passengers',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_time',
            field=models.DateTimeField(),
        ),
    ]
