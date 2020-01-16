from django.db import models
from django.utils import timezone
import datetime
from masters.models import *
from barbershop.models import *
from django.db.models.signals import post_save
from django.shortcuts import render,get_object_or_404, redirect
from django.http import Http404, HttpResponse
class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=155)
    date = models.DateTimeField(u'Дата и время',default=timezone.now)
    # master = models.ForeignKey(Master, blank=True, null=True, default=None, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, blank=True, null=False, default=None, on_delete=models.CASCADE)
    # busy = models.BooleanField(u'Свободен?',default=True)
    def __str__(self):
        return '%s %s' % (self.name, self.date)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

    def save(self, *args, **kwargs):
        q = Subscriber.objects.filter(
            # master__id=self.master.id,
            date__year=self.date.year,
            date__month=self.date.month,
            date__day=self.date.day
        )
        if q.exists() > 0:
            raise Http404('Данная дата занята, выберете другую.')
        else:
            super(Subscriber, self).save(*args, **kwargs)
