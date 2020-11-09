from django.views.generic import TemplateView, ListView, DetailView
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Client, Counter

class HomePageView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'main_page'

class ClientPageView(ListView):
    template_name = 'clients.html'
    
    def get_queryset(self):
        """
        im trying to show a counter
        """
            
        counter = Counter.objects.last()
        if not counter:
            counter = Counter.objects.create()
        
        counter.count =+ 1
        counter.save()

        return counter
    
class AboutPageView(TemplateView):
    template_name = 'about.html'

def client_detail(request, client_id):
    client = Client.objects.get(id=client_id)
    context = { "client_var": client }

    return render(request, "detail.html", context)

