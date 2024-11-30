from django.db import migrations, models
import datetime

def add_default_flights(apps, schema_editor):
    Flight = apps.get_model('airline', 'Flight')
    default_flights = [
        {
            'flight_number': 'FL123',
            'departure_city': 'New York',
            'arrival_city': 'London',
            'departure_time': datetime.datetime(2024, 12, 1, 10, 0),
            'arrival_time': datetime.datetime(2024, 12, 1, 20, 0),
            'price': 500.00,
            'status': 'Scheduled',
        },
        {
            'flight_number': 'FL456',
            'departure_city': 'Los Angeles',
            'arrival_city': 'Tokyo',
            'departure_time': datetime.datetime(2024, 12, 2, 8, 0),
            'arrival_time': datetime.datetime(2024, 12, 2, 18, 0),
            'price': 700.00,
            'status': 'Scheduled',
        },
        {
            'flight_number': 'FL789',
            'departure_city': 'Paris',
            'arrival_city': 'Berlin',
            'departure_time': datetime.datetime(2024, 12, 3, 9, 0),
            'arrival_time': datetime.datetime(2024, 12, 3, 11, 0),
            'price': 200.00,
            'status': 'Scheduled',
        },
        {
            'flight_number': 'FL101',
            'departure_city': 'Dubai',
            'arrival_city': 'Mumbai',
            'departure_time': datetime.datetime(2024, 12, 4, 14, 0),
            'arrival_time': datetime.datetime(2024, 12, 4, 18, 0),
            'price': 300.00,
            'status': 'Scheduled',
        },
        {
            'flight_number': 'FL202',
            'departure_city': 'Sydney',
            'arrival_city': 'Singapore',
            'departure_time': datetime.datetime(2024, 12, 5, 6, 0),
            'arrival_time': datetime.datetime(2024, 12, 5, 12, 0),
            'price': 400.00,
            'status': 'Scheduled',
        },
    ]
    for flight in default_flights:
        Flight.objects.create(**flight)

class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0001_initial'),  # Replace with the last migration dependency
    ]

    operations = [
        migrations.RunPython(add_default_flights),
    ]
