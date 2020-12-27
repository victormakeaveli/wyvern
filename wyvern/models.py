from django.db import models

class Kind(models.Model):
    """
    The kind of Client.
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    __repr__ = __str__

class Client(models.Model):
    """
    Simple clients class
    
    name
    email
    age
    date_created
    

    """

    name = models.CharField(max_length=50,)
    email = models.EmailField(max_length=50)
    age = models.PositiveIntegerField()
    date_created = models.DateTimeField()
    kind = models.ManyToManyField(Kind)
    
    def __str__(self):
        return self.name

    __repr__ = __str__

class CounterViews(models.Model):
    """

    Count the visitors

    count
    """
    
    count = models.IntegerField(default=0)  
