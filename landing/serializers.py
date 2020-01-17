from django.contrib.auth.models import User, Group
from rest_framework import serializers
from masters.models import Master



class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=1, max_length=80)
    class Meta:
        model = Master
        fields = ['name', 'position','descriptions', 'date', 'is_male']

class MasterCreateUpdateSerializer( serializers.ModelSerializer):
    name = serializers.CharField(min_length=1, max_length=80)
    class Meta:
        model =  Master
        exclude = ()
