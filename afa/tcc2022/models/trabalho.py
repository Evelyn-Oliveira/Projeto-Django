from django.db import models 
from .subarea import SubArea

class Trabalho(models.Model):
    titulo = models.CharField('titulo',max_length=40)
    resumo = models.TextField('resumo')
    subarea = models.ForeignKey(SubArea, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Trabalho: {self.titulo}, Resumo:{self.resumo}, Área: {self.subarea.area.tema}, SubArea: {self.subarea.subarea}'

