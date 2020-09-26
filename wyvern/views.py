from django.views.generic import TemplateView, ListView, DetailView
from django.template import loader
from django.shortcuts import render

from .models import Client, Wyvern


class HomePageView(TemplateView):
    template_name = 'index.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'

class ClientPageView(ListView):
    template_name = 'clients.html'
    model = Client

def client_detail(request, client_id):
    client = Client.objects.get(id=client_id)
    context = { "client_var": client }

    return render(request, "detail.html", context)