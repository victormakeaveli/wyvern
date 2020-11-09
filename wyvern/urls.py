from django.urls import path

from . import views


urlpatterns = [
        path('', views.HomePageView.as_view(), name='home'),
        path('clients/', views.ClientPageView.as_view(), name='clients'),
        path('about/', views.AboutPageView.as_view(), name='about'),
        path('<int:client_id>/', views.client_detail, name='detail'),
]
