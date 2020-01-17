from django.shortcuts import render,get_object_or_404
from masters.models import Master
from rest_framework import viewsets
from landing.serializers import UserSerializer, MasterCreateUpdateSerializer
from rest_framework.response import Response
def master(request, id):
    master = get_object_or_404(Master,id=id)
    return render(request, 'masters/master.html', {'master': master})

def master_list(request):
    masters = Master.objects.all()
    return render(request, 'landing/masterlist.html', {'masters':masters})

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Master.objects.all()
    serializer_class = UserSerializer

class ActionSerializedViewSet(viewsets.ModelViewSet):
    action_serializers = {}

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]

        return self.serializer_class

class MastersViewSet(ActionSerializedViewSet):
    serializer_class =UserSerializer
    queryset = Master.objects.all()

    action_serializers = {
        'list': UserSerializer,
        'create':MasterCreateUpdateSerializer,
        'update': MasterCreateUpdateSerializer,
    }

    def get_queryset(self):
        queryset = self.queryset
        return queryset
