from django.db import models

# Create your models here.

class Studentmodel(models.Model):
    Name=models.CharField(max_length=200)
    City=models.CharField(max_length=200)
    Email=models.EmailField()
    Contact=models.IntegerField()
    def __str__(self):
        return self.Name
    

class Marksheetmodel(models.Model):
    Name=models.CharField(max_length=200)
    Math=models.IntegerField()
    Science=models.IntegerField()
    Social_science=models.IntegerField()
    Hindi=models.IntegerField()
    English=models.IntegerField()
    Total_marks=models.IntegerField()
    Percentage=models.IntegerField()
    def __str__(self):
        return self.Name
