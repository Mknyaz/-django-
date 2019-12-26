from django.contrib.auth.models import User, Group
from rest_framework import serializers
from landing.models import Subscriber

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['name', 'email', 'date']
