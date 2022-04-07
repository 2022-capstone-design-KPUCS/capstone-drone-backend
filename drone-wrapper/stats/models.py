import uuid
from django.db import models
from ..users.models import User


class Deck(models.Model):
    """
    A model of deck objects.
    덱 객체의 모델.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    deck_name = models.CharField(max_length=200)
    is_occupied = models.BooleanField(default=False)


class FlightRecord(models.Model):
    """
    A model of flight records
    비행 로그 모델.
    """
    WEATHER_TYPES = (
        ('SUNNY', 'Sunny'),
        ('CLOUDY', 'Cloudy'),
        ('RAINY', 'Rainy'),
        ('SNOWY', 'Snowy'),
        ('FOGGY', 'Foggy'),
        ('HAIL', 'Hail'),
        ('THUNDERSTORM', 'Thunderstorm'),
        ('UNKNOWN', 'Unknown'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    flight_record = models.TextField()
    weather = models.CharField(max_length=20, choices=WEATHER_TYPES)
    is_fire = models.BooleanField()
    is_smoke = models.BooleanField()


class Flight(models.Model):
    """
    A model of flight instances. Records of each flight information.
    드론 비행 정보 인스턴스의 모델. 모든 비행 정보의 기록.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    flight_record_url = models.URLField(max_length=200, blank=True)
    flight_record = models.ForeignKey(FlightRecord, on_delete=models.CASCADE, null=True)
    flight_path = models.JSONField(null=True)
    auto_start_time = models.DateTimeField(blank=True)
    auto_end_time = models.DateTimeField(blank=True)


class Drone(models.Model):
    """
    A model of drone objects.
    드론 객체의 모델.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    flight = models.OneToOneField(Flight, on_delete=models.CASCADE, null=True)
    deck = models.OneToOneField(Deck, on_delete=models.CASCADE, null=True)
    surveilance_area = models.TextField(null=True) # JSON-serialized (text) version of list of lat, lng decimals
    drone_alias = models.CharField(max_length=200, null=True, unique=True)
    is_active = models.BooleanField(default=False)
