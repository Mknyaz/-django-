from django.db import models
from masters.models import *
from django.utils import timezone
from django.db.models.signals import post_save

class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return " %s" % self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Barbershop(models.Model):
    custumer_email = models.EmailField(u'Эл. почта',blank=True, null=True, default=None)
    custumer_name = models.CharField(u'Имя клиента',max_length=64, blank=True, null=True, default=None)
    custumer_master = models.CharField(u'Мастер',max_length=48, blank=True, null=True, default=None)
    custumer_haircut = models.CharField(u'Стрижка',max_length=48, blank=True, null=True, default=None)
    custumer_date = models.DateTimeField(u'Дата и время',default=timezone.now)
    price = models.DecimalField(u'Цена',max_digits=10, decimal_places=2,default=0)
    comments = models.TextField(u'Комментарий',blank=True, null=True, default=None)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return "Заказ номер %s, %s" % (self.id, self.status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        super(Barbershop, self).save(*args, **kwargs)


class MasterInBarbershop(models.Model):
    barbershop = models.ForeignKey(Barbershop, blank=True, null=True, default=None,on_delete=models.CASCADE)
    master = models.ForeignKey(Master, blank=True, null=True, default=None,on_delete=models.CASCADE)
    haircut =models.CharField(u'Стрижка',max_length=48, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    date_per_master = models.DateTimeField(default=timezone.now)
    custumer_date = models.DateTimeField(u'Дата и время',default=timezone.now)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s, %s" % (self.master.name, self.master.position)

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'

    def save(self, *args, **kwargs):
        # price = self.haircut.price
        # self.price = price
        #self.price_per_item = price_per_item
        # barbershop = self.barbershop
        # all_masters_in_barbershop = MasterInBarbershop.objects.filter(barbershop=barbershop, is_active=True)
        #
        # for item in all_masters_in_barbershop:
        #    total_price = item.price
        # self.barbershop.custumer_haircut = self.haircut.name
        self.barbershop.custumer_master = self.master.name
        self.barbershop.price = self.haircut.price
        self.barbershop.save(force_update=True)
        super(MasterInBarbershop, self).save(*args, **kwargs)

def master_in_barbershop_save(sender, instance, created, **kwargs):
    barbershop = instance.barbershop
    # all_masters_in_barbershop = MasterInBarbershop.object.filter(barbershop=barbershop, is_active=True)
    # total_price = 0\\
    # for item in all_masters_in_barbershop:
    #     total_price = item.price
    # self.barbershop.price = total_price
    instance.barbershop.save(force_update=True)

post_save.connect(master_in_barbershop_save, sender=MasterInBarbershop)
