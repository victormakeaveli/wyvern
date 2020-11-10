from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from django.http import HttpResponse

from .models import Client, Counter

class HomePageView(TemplateView):
    template_name = 'index.html'


class ClientPageView(ListView):
    template_name = 'clients.html'
    model = Client


class AboutPageView(TemplateView):
    template_name = 'about.html'


def client_detail(request, client_id):
    client = Client.objects.get(id=client_id)
    counter = Counter.objects.last()
    if not counter:
        counter = Counter.objects.create()
    
    counter.count =+ 1
    counter.save()

    context = { 
        "client_var": client,
        "counter_var": counter 
        }

    return render(request, "detail.html", context)
