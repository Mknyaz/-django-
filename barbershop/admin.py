from django.contrib import admin
from .models import *

class MasterInBarbershopInline(admin.TabularInline):
    model = MasterInBarbershop
    extra = 0

class BarbershopAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Barbershop._meta.fields]
    inlines = [MasterInBarbershopInline]
    class Meta:
        model = Barbershop

admin.site.register(Barbershop, BarbershopAdmin)

class MasterInBarbershopAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MasterInBarbershop._meta.fields]

    class Meta:
        model = MasterInBarbershop

admin.site.register(MasterInBarbershop, MasterInBarbershopAdmin)

class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)
