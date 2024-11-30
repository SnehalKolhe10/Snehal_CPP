# Generated by Django 4.2.16 on 2024-11-18 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0002_rename_arrival_time_flight_departure_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='departure',
            new_name='departure_time',
        ),
        migrations.RenameField(
            model_name='flight',
            old_name='arrival_city',
            new_name='destination',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='arrival',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='departure_city',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='name',
        ),
        migrations.AlterField(
            model_name='flight',
            name='flight_number',
            field=models.CharField(max_length=10),
        ),
    ]
