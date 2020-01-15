from django import forms
from .models import *
import datetime

class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = ('name', 'email', 'date', 'master')
