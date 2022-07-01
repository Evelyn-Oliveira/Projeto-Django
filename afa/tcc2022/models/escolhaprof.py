from django.db import models
from .trabalho import Trabalho
from .professor import Professor
import datetime
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone
import datetime

class EscolhaProf(models.Model):

    #data = models.DateTimeField('data')
    trabalho = models.ForeignKey(Trabalho,on_delete=models.CASCADE)
    #usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    #print (usuario.username)
    professor = models.ForeignKey(Professor,on_delete=models.CASCADE)
    nota = models.IntegerField('nota', null=True, blank=True)
    #nota = models.DecimalField('nota', max_digits=6, decimal_places=2, null=True, blank=True)
    def __str__(self):
        #return f'Nome Professor: {self.usuario.username}, Titulo :{self.trabalho.titulo}, Nota: {self.nota}'
        return f'Nome Professor: {self.professor.nome}, Titulo: {self.trabalho.titulo}, Nota: {self.nota}'
 