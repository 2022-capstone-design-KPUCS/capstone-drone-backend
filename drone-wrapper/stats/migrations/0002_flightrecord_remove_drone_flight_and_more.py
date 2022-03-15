# Generated by Django 4.0.2 on 2022-03-14 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlightRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('flight_record', models.TextField()),
                ('weather', models.CharField(choices=[('SUNNY', 'Sunny'), ('CLOUDY', 'Cloudy'), ('RAINY', 'Rainy'), ('SNOWY', 'Snowy'), ('FOGGY', 'Foggy'), ('HAIL', 'Hail'), ('THUNDERSTORM', 'Thunderstorm'), ('UNKNOWN', 'Unknown')], max_length=20)),
                ('is_fire', models.BooleanField()),
                ('is_smoke', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='drone',
            name='flight',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='flight_status',
        ),
        migrations.AddField(
            model_name='flight',
            name='drone_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stats.drone'),
        ),
        migrations.AlterField(
            model_name='drone',
            name='admin_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Administrator',
        ),
        migrations.AddField(
            model_name='flightrecord',
            name='flight_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.flight'),
        ),
    ]