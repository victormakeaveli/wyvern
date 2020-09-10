from django.urls import path

from . import views

urlpatterns = [
        path('', views.HomePageView.as_view(), name='home'),
        path('guys/', views.GuysPageView.as_view(), name='guys'),
        path('about/', views.AboutPageView.as_view(), name='about'),
]