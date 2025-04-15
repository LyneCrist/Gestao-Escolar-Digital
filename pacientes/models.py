from click import option
from django.db import models
from .utils import AGENDAMENTO_FIXO_CHOICES, GENERO_CHOICES


class Paciente(models.Model):

    class Status(models.IntegerChoices):
        ATIVO = 1, "Ativo"
        INATIVO = 2, "Inativo"

    nome = models.CharField(max_length=60)

    data_de_nascimento = models.DateField()

    genero = models.IntegerField(choices=GENERO_CHOICES)

    cartao_sus = models.CharField(max_length=15, unique=True)

    agendamento_fixo = models.IntegerField(choices=AGENDAMENTO_FIXO_CHOICES)

    telefone = models.CharField(max_length=13)

    rua = models.CharField(max_length=60)

    numero = models.CharField(max_length=7)

    complemento = models.CharField(max_length=60, null=True)

    ponto_referencia = models.CharField(max_length=60, null=True)

    status = models.IntegerField(default=Status.ATIVO)

    data_criacao = models.DateTimeField(auto_now_add=True)

    data_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        db_table = "pacientes"
        ordering = ["-data_criacao"]
