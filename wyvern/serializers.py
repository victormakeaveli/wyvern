from rest_framework import serializers
from .models import Client, Kind

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'url', 'name', 'age', 'date_created', 'email', 'kind')
    

class KindSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kind
        fields = ('id', 'name')

