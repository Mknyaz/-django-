from django.shortcuts import render,get_object_or_404, redirect
from .forms import SubscriberForm
from masters.models import Master
from rest_framework import viewsets
from landing.serializers import UserSerializer


def landing(request, id):
    # message = 'Провал'
    master = get_object_or_404(Master, id=id)
    if request.method=="POST":
        form=SubscriberForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            landing.master = master
            data.save()
            # message = 'Успех'

            # if subscriber.busy==True:
            #     return render(request, 'landing/success.html', {'form': form})
            # else:
            #     return render(request, 'landing/success.html', {'form': form})
            # # return redirect('master', id=master.id)
    else:
        form=SubscriberForm()

    return render(request, 'landing/landing.html', {'form': form})

def home(request):
    masters_men = Master.objects.filter(is_active=True, category__id=1)
    masters_women = Master.objects.filter(is_active=True, category__id=2)
    return render(request, 'landing/home.html', locals())

def contact(request):
    return render(request, 'landing/contact.html', {'values': ['Вопросы можно задавать по телефону', '8-903-184-08-18']})

def about(request):
    return render(request, 'landing/about.html', {'values': 1})

def master(request, id):
    master = get_object_or_404(Master,id=id)
    return render(request, 'masters/master.html', {'master': master})

def success(request):
    return render(request, 'landing/success.html', locals())
def error(request):
    return render(request, 'landing/error.html', locals())
def master_list(request):
    masters = Master.objects.all()
    return render(request, 'master.html', {'masters':masters})
def handler404(request, exception, template_name="error.html"):
    response = render_to_response("error.html")
    response.status_code = 404
    return response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Master.objects.all()
    serializer_class = UserSerializer
