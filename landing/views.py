from django.shortcuts import render,get_object_or_404
from .forms import SubscriberForm
from masters.models import Master
from rest_framework import viewsets
from landing.serializers import UserSerializer

def landing(request):
    if request.method=="POST":
        form=SubscriberForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
    else:
        form=SubscriberForm()
    # form = SubscriberForm(request.POST or None)
    # if request.method=="POST" and form.is_valid():
    #     print(request.POST)
    #     print(form.cleaned_data)
    #     data = form.cleaned_data
    #     print(data["name"])
    #     new_form = form.save()
    return render(request, 'landing/landing.html', {'form': form})

def home(request):
    masters_men = Master.objects.filter(is_active=True, category__id=1)
    masters_women = Master.objects.filter(is_active=True, category__id=2)
    return render(request, 'landing/home.html', locals())

def contact(request):
    return render(request, 'landing/contact.html', {'values': ['Вопросы можно задавать по телефону', '8-903-184-08-18']})

def about(request):
    return render(request, 'landing/about.html', {'values': 1})




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Master.objects.all()
    serializer_class = UserSerializer
