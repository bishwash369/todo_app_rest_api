from django.db import models

# Create your models here.

class Employee(models.Model):
    #id = models.Field(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Task(models.Model):
    #id = models.Field(primary_key=True)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=True, blank=True,null=True)
    employee = models.ForeignKey('Employee', related_name='tasks', on_delete=models.CASCADE, default = "D")

      
    def __str__(self):
        return self.title