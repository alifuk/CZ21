from django.db import models

from django.db.models import (
  DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField,
  Model, TextField
)

class Brand(Model):
  name = CharField(max_length=64)

  def __str__(self):
    return f"Značka auta: {self.name}"