from django.contrib import admin
from .models import *

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "date"]
    search_fields = ('name','email', "date")

    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)
