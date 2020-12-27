from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('Client', views.ClientView)
router.register('Kind', views.KindView)

urlpatterns = [
        # path('', include(router.urls)),

        path('', views.HomePageView.as_view(), name='home'),

        path('clients/', views.ClientPageView.as_view(), name='clients'),
        path('about/', views.AboutPageView.as_view(), name='about'),
        path('<int:client_id>/', views.client_detail, name='detail'),
]
