from typing import Any
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    grupo = models.CharField(max_length=255)

    def get_atributtes(self):
        return {'nome':self.nome, 'email':self.email, 'grupo':self.grupo}

    def __str__(self) -> str:
        return self.nome