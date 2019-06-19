from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Employee(models.Model):
    e_name = CharField(max_length=10)
    e_add = CharField(max_length=10)
    e_dept = CharField(max_length=15)
    def __str__(self):
        return self.e_name