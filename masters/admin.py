from django.contrib import admin
from .models import *



class MasterImageInline(admin.TabularInline):

    model = MasterImage
    extra = 0


class MasterCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MasterCategory._meta.fields]

    class Meta:
        model = MasterCategory

admin.site.register(MasterCategory, MasterCategoryAdmin)



class MasterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Master._meta.fields]
    inlines = [MasterImageInline]
    class Meta:
        model = Master

admin.site.register(Master, MasterAdmin)

class MasterImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MasterImage._meta.fields]

    class Meta:
        model = MasterImage

admin.site.register(MasterImage, MasterImageAdmin)
