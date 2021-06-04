from django.conf import settings
from django.db import models
from django.utils import timezone


class Account(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)
    dob = models.DateField('dateOfBirth', default=timezone.now)

    def publish(self):
        self.dob = timezone.now()
        self.save()

    def __str__(self):
        return self.name
