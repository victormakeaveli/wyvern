from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import People
class HomePageView(TemplateView):
    template_name = 'index.html'

def Detail(request, people_pk):
    return HttpResponse 