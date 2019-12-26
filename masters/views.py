from django.shortcuts import render,get_object_or_404
from masters.models import Master


def master(request, id):
    master = get_object_or_404(Master,id=id)
    return render(request, 'masters/master.html', {'master': master})
