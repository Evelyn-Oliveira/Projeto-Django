from django.db import models
from .area import Area

class SubArea(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    subarea=models.CharField('subarea',max_length=30)
    
    def __str__(self):
        return f'SubArea: {self.subarea} Area:{self.area.tema}'

