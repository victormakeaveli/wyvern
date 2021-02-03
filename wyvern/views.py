from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, TemplateView
from rest_framework import permissions, viewsets

from .models import Client, Kind
from .serializers import ClientSerializer, KindSerializer


class ClientView(viewsets.ModelViewSet): 
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    #restricted permission for this view specifically 
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class KindView(viewsets.ModelViewSet):
    queryset = Kind.objects.all()
    serializer_class = KindSerializer


class HomePageView(generic.TemplateView):
    template_name = 'index.html'
    

    # def get_queryset(self):
    #     counter = CounterViews.objects.last()
        
    #     if not counter:
    #         counter = CounterViews.objects.create()

    #     counter.count += 1
    #     counter.save()

    #     return counter


class ClientPageView(ListView):
    template_name = 'clients.html'
    model = Client


class AboutPageView(TemplateView):
    template_name = 'about.html'


def client_detail(request, client_id):
    client = Client.objects.get(id=client_id)
    kind = Kind.objects.get(id=client_id)
    
    context = { 
        "client_var": client,
        "kind_var" : kind,
        }

    return render(request, "detail.html", context)

