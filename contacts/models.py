from django.db import models
from datetime import datetime
from django.utils.timezone import now

class Contact(models.Model):
    name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    dates = models.DateField(default=now)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
