from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tarefa(models.Model):
    PRIORIDADES = [
        ('alta','Alta'),
        ('media', 'Média'),
        ('baixa', 'Baixa'),
    ]

    nome = models.CharField(max_length=100)
    prioridade = models.CharField(max_length=10, choices=PRIORIDADES)
    prazo = models.DateField()
    categoria = models.CharField(max_length=50)
    dono = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.prioridade})"