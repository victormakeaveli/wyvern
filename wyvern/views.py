from django.views.generic import TemplateView, ListView, DetailView
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Client, Wyvern


class HomePageView(TemplateView):
    template_name = 'index.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'

class ClientPageView(ListView):
    template_name = 'clients.html'
    model = Client

def client_detail(request, Client_id):
    client_name = Client.objects.get(name)
    client_age = Client.objects.get(age)
    context = {
        "name": client_name,
        "age": client_age,
    }

    return render(request, "detail.html", context)