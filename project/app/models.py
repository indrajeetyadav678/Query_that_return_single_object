from django.db import models

# Create your models here.

class Studentmodel(models.Model):
    Name=models.CharField(max_length=200)
    City=models.CharField(max_length=200)
    Email=models.EmailField()
    Contact=models.IntegerField()
    def __str__(self):
        return self.Name
    


