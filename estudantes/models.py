from django.db import models
from .choices import GENERO_CHOICES, STATUS_CHOICES


class Estudante(models.Model):

    nome = models.CharField(max_length=60)

    data_de_nascimento = models.DateField()

    genero = models.IntegerField(choices=GENERO_CHOICES)

    mae = models.CharField(max_length=60)

    pai = models.CharField(max_length=60)

    email = models.CharField(max_length=60, unique=True)

    celular = models.CharField(max_length=14)

    registro_do_aluno = models.CharField(max_length=11, unique=True)

    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    data_criacao = models.DateTimeField(auto_now_add=True)

    data_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.nome}"


class Meta:
    db_table = "estudantes"
    ordering = ["-data_criacao"]
