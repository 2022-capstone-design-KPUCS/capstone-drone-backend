from django.db import models


class Administrator(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=50)


class Flight(models.Model):
    id = models.AutoField(primary_key=True)
    flight_record_url = models.URLField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    flight_path = models.DecimalField(max_digits=10, decimal_places=10)
    flight_status = models.BooleanField()


class Deck(models.Model):
    id = models.AutoField(primary_key=True)
    deck_name = models.CharField(max_length=200)
    deck_status = models.BooleanField()


class Drone(models.Model):
    id = models.AutoField(primary_key=True)
    admin_id = models.ForeignKey(Administrator, on_delete=models.CASCADE)
    destination = models.CharField(max_length=200)
    flight = models.ManyToManyField(Flight)
    deck = models.ManyToManyField(Deck)
