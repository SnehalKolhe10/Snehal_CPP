{"filter":false,"title":"0010_auto_20241130_1933.py","tooltip":"/airline_project/airline/migrations/0010_auto_20241130_1933.py","ace":{"folds":[],"scrolltop":286,"scrollleft":0,"selection":{"start":{"row":64,"column":0},"end":{"row":64,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":19,"state":"start","mode":"ace/mode/python"}},"hash":"bbeb46ff692bb916bcd016d68ac3b3085ed8929b","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":13,"column":0},"action":"remove","lines":["# Generated by Django 4.2.16 on 2024-11-30 19:33","","from django.db import migrations","","","class Migration(migrations.Migration):","","    dependencies = [","        ('airline', '0009_remove_cart_added_at_alter_flight_departure_city_and_more'),","    ]","","    operations = [","    ]",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":64,"column":0},"action":"insert","lines":["from django.db import migrations, models","import datetime","","def add_default_flights(apps, schema_editor):","    Flight = apps.get_model('airline', 'Flight')","    default_flights = [","        {","            'flight_number': 'FL123',","            'departure_city': 'New York',","            'arrival_city': 'London',","            'departure_time': datetime.datetime(2024, 12, 1, 10, 0),","            'arrival_time': datetime.datetime(2024, 12, 1, 20, 0),","            'price': 500.00,","            'status': 'Scheduled',","        },","        {","            'flight_number': 'FL456',","            'departure_city': 'Los Angeles',","            'arrival_city': 'Tokyo',","            'departure_time': datetime.datetime(2024, 12, 2, 8, 0),","            'arrival_time': datetime.datetime(2024, 12, 2, 18, 0),","            'price': 700.00,","            'status': 'Scheduled',","        },","        {","            'flight_number': 'FL789',","            'departure_city': 'Paris',","            'arrival_city': 'Berlin',","            'departure_time': datetime.datetime(2024, 12, 3, 9, 0),","            'arrival_time': datetime.datetime(2024, 12, 3, 11, 0),","            'price': 200.00,","            'status': 'Scheduled',","        },","        {","            'flight_number': 'FL101',","            'departure_city': 'Dubai',","            'arrival_city': 'Mumbai',","            'departure_time': datetime.datetime(2024, 12, 4, 14, 0),","            'arrival_time': datetime.datetime(2024, 12, 4, 18, 0),","            'price': 300.00,","            'status': 'Scheduled',","        },","        {","            'flight_number': 'FL202',","            'departure_city': 'Sydney',","            'arrival_city': 'Singapore',","            'departure_time': datetime.datetime(2024, 12, 5, 6, 0),","            'arrival_time': datetime.datetime(2024, 12, 5, 12, 0),","            'price': 400.00,","            'status': 'Scheduled',","        },","    ]","    for flight in default_flights:","        Flight.objects.create(**flight)","","class Migration(migrations.Migration):","","    dependencies = [","        ('airline', '0001_initial'),  # Adjust based on the last migration file","    ]","","    operations = [","        migrations.RunPython(add_default_flights),","    ]",""]}],[{"start":{"row":0,"column":0},"end":{"row":64,"column":0},"action":"remove","lines":["from django.db import migrations, models","import datetime","","def add_default_flights(apps, schema_editor):","    Flight = apps.get_model('airline', 'Flight')","    default_flights = [","        {","            'flight_number': 'FL123',","            'departure_city': 'New York',","            'arrival_city': 'London',","            'departure_time': datetime.datetime(2024, 12, 1, 10, 0),","            'arrival_time': datetime.datetime(2024, 12, 1, 20, 0),","            'price': 500.00,","            'status': 'Scheduled',","        },","        {","            'flight_number': 'FL456',","            'departure_city': 'Los Angeles',","            'arrival_city': 'Tokyo',","            'departure_time': datetime.datetime(2024, 12, 2, 8, 0),","            'arrival_time': datetime.datetime(2024, 12, 2, 18, 0),","            'price': 700.00,","            'status': 'Scheduled',","        },","        {","            'flight_number': 'FL789',","            'departure_city': 'Paris',","            'arrival_city': 'Berlin',","            'departure_time': datetime.datetime(2024, 12, 3, 9, 0),","            'arrival_time': datetime.datetime(2024, 12, 3, 11, 0),","            'price': 200.00,","            'status': 'Scheduled',","        },","        {","            'flight_number': 'FL101',","            'departure_city': 'Dubai',","            'arrival_city': 'Mumbai',","            'departure_time': datetime.datetime(2024, 12, 4, 14, 0),","            'arrival_time': datetime.datetime(2024, 12, 4, 18, 0),","            'price': 300.00,","            'status': 'Scheduled',","        },","        {","            'flight_number': 'FL202',","            'departure_city': 'Sydney',","            'arrival_city': 'Singapore',","            'departure_time': datetime.datetime(2024, 12, 5, 6, 0),","            'arrival_time': datetime.datetime(2024, 12, 5, 12, 0),","            'price': 400.00,","            'status': 'Scheduled',","        },","    ]","    for flight in default_flights:","        Flight.objects.create(**flight)","","class Migration(migrations.Migration):","","    dependencies = [","        ('airline', '0001_initial'),  # Adjust based on the last migration file","    ]","","    operations = [","        migrations.RunPython(add_default_flights),","    ]",""],"id":3},{"start":{"row":0,"column":0},"end":{"row":64,"column":0},"action":"insert","lines":["from django.db import migrations, models","import datetime","","def add_default_flights(apps, schema_editor):","    Flight = apps.get_model('airline', 'Flight')","    default_flights = [","        {","            'flight_number': 'FL123',","            'departure_city': 'New York',","            'arrival_city': 'London',","            'departure_time': datetime.datetime(2024, 12, 1, 10, 0),","            'arrival_time': datetime.datetime(2024, 12, 1, 20, 0),","            'price': 500.00,","            'status': 'Scheduled',","        },","        {","            'flight_number': 'FL456',","            'departure_city': 'Los Angeles',","            'arrival_city': 'Tokyo',","            'departure_time': datetime.datetime(2024, 12, 2, 8, 0),","            'arrival_time': datetime.datetime(2024, 12, 2, 18, 0),","            'price': 700.00,","            'status': 'Scheduled',","        },","        {","            'flight_number': 'FL789',","            'departure_city': 'Paris',","            'arrival_city': 'Berlin',","            'departure_time': datetime.datetime(2024, 12, 3, 9, 0),","            'arrival_time': datetime.datetime(2024, 12, 3, 11, 0),","            'price': 200.00,","            'status': 'Scheduled',","        },","        {","            'flight_number': 'FL101',","            'departure_city': 'Dubai',","            'arrival_city': 'Mumbai',","            'departure_time': datetime.datetime(2024, 12, 4, 14, 0),","            'arrival_time': datetime.datetime(2024, 12, 4, 18, 0),","            'price': 300.00,","            'status': 'Scheduled',","        },","        {","            'flight_number': 'FL202',","            'departure_city': 'Sydney',","            'arrival_city': 'Singapore',","            'departure_time': datetime.datetime(2024, 12, 5, 6, 0),","            'arrival_time': datetime.datetime(2024, 12, 5, 12, 0),","            'price': 400.00,","            'status': 'Scheduled',","        },","    ]","    for flight in default_flights:","        Flight.objects.create(**flight)","","class Migration(migrations.Migration):","","    dependencies = [","        ('airline', '0001_initial'),  # Replace with the last migration dependency","    ]","","    operations = [","        migrations.RunPython(add_default_flights),","    ]",""]}]]},"timestamp":1732995497116}