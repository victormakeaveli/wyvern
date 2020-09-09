from django.db import models

class People(models.Model):
    name = models.CharField(max_length=12)
    role = models.CharField(max_length=11)
    date_created = models.DateTimeField('date created')
    
    def __str__(self):
        return self.name
    
