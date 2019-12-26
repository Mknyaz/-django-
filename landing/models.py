from django.db import models
from django.utils import timezone
import datetime
from masters.models import *
from barbershop.models import *
from django.db.models.signals import post_save

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=155)
    date = models.DateTimeField(u'Дата и время',default=timezone.now)
    def __str__(self):
        return '%s %s' % (self.name, self.date)
