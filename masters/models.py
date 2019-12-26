from django.db import models
from django.utils import timezone

class Haircut(models.Model):
    name = models.CharField(u'название стрижки',max_length=50, blank=True, null=True, default=None)
    price = models.DecimalField(u'цена',max_digits=10, decimal_places=2,default=None)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return "%s, %s" % (self.name, self.price)

    class Meta:
        verbose_name = 'Стрижка'
        verbose_name_plural = 'Стрижки'

class MasterCategory(models.Model):
    name = models.CharField(u'Мастер',max_length=155, blank=True, null=True, default=None)
    is_active = models.BooleanField(u'Активность',default=True)
    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Тип мастера'
        verbose_name_plural = 'Тип мастеров'

class DateMaster(models.Model):
    #is_active = models.BooleanField(u'Активность',default=True)
    name = models.CharField(u'Мастер',max_length=155, blank=True, null=True, default=None)
    date = models.DateTimeField(u'Дата и время',default=timezone.now)

    def __str__(self):
        return "%s" % self.date

    class Meta:
        verbose_name = 'Время мастера'
        verbose_name_plural = 'Время мастеров'

class Meta:
    verbose_name = 'Тип мастера'
    verbose_name_plural = 'Тип мастеров'

class Master(models.Model):
    name = models.CharField(u'Мастер',max_length=155, blank=True, null=True, default=None)
    descriptions = models.TextField(u'Описание',blank=True, null=True, default=None)
    short_descriptions = models.TextField(u'Стрижки',blank=True, null=True, default=None)
    position = models.CharField(u'Должность',max_length=155,blank=True, null=True, default=None);
    category = models.ForeignKey(MasterCategory,blank=True, null=True, default=None, on_delete=models.CASCADE)
    is_active = models.BooleanField(u'Активность',default=True)
    haircut = models.ForeignKey(Haircut,blank=True, null=True, default=None, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    date = models.DateTimeField(u'Дата и время',default=timezone.now)

    def __str__(self):
        return "%s, %s" % (self.name, self.position)

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'



class MasterImage(models.Model):
    master = models.ForeignKey(Master,blank=True, null=True, default=None,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/master_images/')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
