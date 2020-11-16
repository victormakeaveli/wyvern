from django.views.generic import TemplateView, ListView, View
from django.shortcuts import render

from .models import Client, CounterViews

class HomePageView(TemplateView):
    template_name = 'index.html'
    

class ClientPageView(ListView):
    template_name = 'clients.html'
    model = Client


class AboutPageView(TemplateView):
    template_name = 'about.html'


def client_detail(request, client_id):
    client = Client.objects.get(id=client_id)

    context = { 
        "client_var": client,
        }

    return render(request, "detail.html", context)

def base_html_counter(request):
    counter = CounterViews.objects.last()
    if not counter:
        counter = CounterViews.objects.create()

    counter.count += 1
    counter.save()

    return render(request, "base.html", {"counter":counter})
    
