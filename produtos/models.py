from django.db import models

class Produto(models.Model):
    nome_id = models.CharField(unique=True, max_length=255)
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=5000)
    preco = models.CharField(max_length=255)
    email_cliente = models.EmailField(unique=True, null=True)

    def __str__(self) -> str:
        return self.nome