from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ventas(models.Model):
    nombre = models.DateField()
    valorTotal = models.BigIntegerField()
    tipoPago = models.CharField(max_length=20)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
