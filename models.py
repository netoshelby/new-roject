from django.db import models

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Animals(models.Model):
    nome = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    altura = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    sobre = models.CharField(max_length=500)
    image = models.ImageField()
    categoria = models.ManyToManyField(Categoria, related_name='animals')

    def __str__(self):
        return self.nome