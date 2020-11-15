from django.db import models
from django.utils import timezone

class Client(models.Model):
    """
    simple client class
    
    name
    email
    age
    date_created 

    """

    name = models.CharField(max_length=50,)
    email = models.EmailField(max_length=50)
    age = models.PositiveIntegerField()
    date_created = models.DateTimeField(timezone.now())
    
    def __str__(self):
        return self.name

    __repr__ = __str__


class CounterViews(models.Model):
    """
    Count the visitors
    """
    
    count = models.IntegerField(default=0)  

    def __str__(self):
        return self.name

    __repr__ = __str__


    