from django.db import models

# Create your models here.
from dono.models import Dono


class Gatinho(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    cores_do_pelo = (
        ('MARRON','Marron'),
        ('CINZA','Cinza'),
        ('LARANJA','Laranja'),
        ('BEGE','Bege'),
        ('PRETO', 'Preto'),
        ('BRANCO', 'Branco'),
        ('PARDO', 'Pardo'),
    )
    cor_do_pelo = models.CharField(choices=cores, max_length=100)
    dono = models.ManyToManyField(Dono)