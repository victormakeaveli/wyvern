from django.views.generic import TemplateView, ListView
from django.shortcuts import render

from .models import Client, Counter

class HomePageView(TemplateView):
    template_name = 'index.html'
    counter = Counter.objects.last()

    def counting(request, self):    
        if not self.counter:
            self.counter = Counter.objects.create()

        self.counter.count += 1
        self.counter.save()

        context = {
            "counter_var": self.counter,
        }

        return render(request, self.template_name, context)
    

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
