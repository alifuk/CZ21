from django.db import models
from datetime import datetime

from django.db.models import (
  DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField,
  Model, TextField
)

class Brand(Model):
  name = CharField(max_length=64)

  def __str__(self):
    return f"Značka auta: {self.name}"

class VehicleType(Model):
  name = CharField(max_length=64)

  def __str__(self):
    return f"Typ: {self.name}"

class Offer(Model):
  brand = ForeignKey(Brand, on_delete=DO_NOTHING)
  vehicle_type = ForeignKey(VehicleType, on_delete=DO_NOTHING)
  price = IntegerField()
  description = TextField()
  power = IntegerField()
  year = IntegerField()
  offer_date = DateTimeField(default=datetime.now)
  view_count = IntegerField(default=0)
  

class Comment(Model):
  username = CharField(max_length=64)
  offer = ForeignKey(Offer, on_delete=DO_NOTHING)
  text = TextField()
  commented_date = DateTimeField(default=datetime.now)

