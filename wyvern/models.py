from django.db import models

class People(models.Model):
    name = models.CharField(max_length=15)
    role = models.CharField(max_length=15)
    date_created = models.DateTimeField('date created')
    
    def __str__(self):
        return self.name
    
