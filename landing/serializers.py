from django.contrib.auth.models import User, Group
from rest_framework import serializers
from masters.models import Master

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Master
        fields = ['name', 'position', 'date']
