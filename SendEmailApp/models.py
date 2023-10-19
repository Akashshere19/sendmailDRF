from datetime import date
from django.db import models
from rest_framework import serializers

# Create your models here.
class Employee(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    imp_date = models.DateField()
    event_name = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return self.name  

class EventTemplate(models.Model):
    # employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event_namefor = models.CharField(max_length=50)       
    template = models.CharField(max_length=200)

    def __str__(self):
        return self.event_namefor





class EmployeeNameSerializer(serializers.Serializer):
    name = serializers.CharField()        