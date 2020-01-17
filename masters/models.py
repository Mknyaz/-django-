from django.db import models
from django.utils import timezone
from django.template.defaultfilters import truncatewords
from django.urls import reverse
from .managers import MasterManager, MasterMenManager, MasterWomenManager
# class Haircut(models.Model):
#     name = models.CharField(u'название стрижки',max_length=50, blank=True, null=True, default=None)
#     price = models.DecimalField(u'цена',max_digits=10, decimal_places=2,default=None)
#     is_active = models.BooleanField(default=True)
#     def __str__(self):
#         return "%s, %s" % (self.name, self.price)
#
#     class Meta:
#         verbose_name = 'Стрижка'
#         verbose_name_plural = 'Стрижки'

class MasterCategory(models.Model):
    name = models.CharField(u'Мастер',max_length=155, blank=True, null=True, default=None)
    # is_active = models.BooleanField(u'Активность',default=True)
    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Тип мастера'
        verbose_name_plural = 'Тип мастеров'

# class DateMaster(models.Model):
#     is_active = models.BooleanField(u'Активность',default=True)
#     name = models.CharField(u'Мастер',max_length=155, blank=True, null=True, default=None)
#     date = models.DateTimeField(u'Дата и время',default=timezone.now)
#
#     def __str__(self):
#         return "%s" % self.date
#
#     class Meta:
#         verbose_name = 'Время мастера'
#         verbose_name_plural = 'Время мастеров'
#


class Master(models.Model):
    name = models.CharField(u'Мастер',max_length=155, blank=False, null=False, default=None)
    descriptions = models.CharField(u'Описание',blank=False, null=False, max_length=155, default="")
    # short_descriptions = models.TextField(u'Стрижки',blank=False, null=False, default=None)
    position = models.CharField(u'Должность',max_length=155,blank=False, null=False, default="");
    # category = models.ForeignKey(MasterCategory,blank=True, null=True, default=None, on_delete=models.CASCADE)
    is_active = models.BooleanField(u'Активность',default=True)
    # haircut = models.CharField(u'Стрижка',max_length=155,blank=False, null=False, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    date = models.DateTimeField(u'Дата и время',default=timezone.now)
    is_male = models.BooleanField(u'Муж?',default=True)


    objects = MasterManager()
    men = MasterMenManager()
    women = MasterWomenManager()
    # qwe = MasterCategory.id
    # def save(self, * args, ** kwargs):
    #     masters_men = Master.objects.filter(is_active=True, category__id=1)
    #     masters_women = Master.objects.filter(is_active=True, category__id=2)
    #     if masters_women:
    #         is_male=False
    #     super().save(*args, ** kwargs)
    #
    # masters_men = objects.filter(is_active=True, category__id=1)
    # masters_women = objects.filter(is_active=True, category__id=2)


    def get_absolute_url(self):
         return reverse('master', args=[str(self.id)])

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
