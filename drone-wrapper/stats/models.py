import uuid
from pyexpat import model
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from ..users.models import User


class Deck(models.Model):
    """
    A model of deck objects.
    덱 객체의 모델.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    deck_name = models.CharField(max_length=200)
    is_occupied = models.BooleanField(default=False)


class Drone(models.Model):
    """
    A model of drone objects.
    드론 객체의 모델.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE)
    surveilance_area = models.TextField(null=True) # JSON-serialized (text) version of list of lat, lng decimals
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, null=True)
    drone_alias = models.CharField(max_length=200, null=True)
    is_active = models.BooleanField(default=False)



class Flight(models.Model):
    """
    A model of flight instances. Records of each flight information.
    드론 비행 정보 인스턴스의 모델. 모든 비행 정보의 기록.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    flight_record_url = models.URLField(max_length=200)
    flight_path = models.TextField(null=True)
    auto_start_time = models.DateTimeField()
    auto_end_time = models.DateTimeField()
    drone_id = models.ForeignKey(Drone, on_delete=models.CASCADE, null=True)

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
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE)
    flight_record = models.TextField()
    # start_time = models.DateTimeField()
    # end_time = models.DateTimeField()
    weather = models.CharField(max_length=20, choices=WEATHER_TYPES)
    is_fire = models.BooleanField()
    is_smoke = models.BooleanField()

