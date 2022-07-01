from django.db import models

class Area(models.Model):
    tema = models.CharField('tema',max_length=40)

    def __str__(self):
        return f'Area: {self.tema}'

