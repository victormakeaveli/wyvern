from django.views.generic import TemplateView, ListView, DetailView
from .models import People
class HomePageView(TemplateView):
    template_name = 'index.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'

class GuysPageView(ListView):
    template_name = 'listguys.html'
    
    model = People
    