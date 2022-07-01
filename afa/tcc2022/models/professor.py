from django.db import models

class Professor(models.Model):
    nome = models.CharField('nome',max_length=30)
    senha = models.CharField('senha',max_length=10)

    def __str__(self):
        return f'Professor: {self.nome} Senha: {self.senha}'

