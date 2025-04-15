from django.db import models
from pacientes.models import Paciente


class Condicao(models.Model):

    CONDICAO_FISICA_CHOICES = (
        (1, "Deambula"),
        (2, "Não deambula"),
        (3, "Acamado"),
        (4, "Cadeirante"),
        (5, "Traqueostomizado"),
        (6, "Uso de Oxigênio Contínuo"),
        (7, "Outros"),
    )

    ACOMPANHANTE_CHOICES = ((1, "Sim"), (2, "Não"))

    CUIDADO_ESPECIAL_CHOICES = ((1, "Sim"), (2, "Não"))

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    condicao_fisica = models.IntegerField(choices=CONDICAO_FISICA_CHOICES)

    descricao_condicao = models.CharField(max_length=60, null=True)

    acompanhante = models.IntegerField(choices=ACOMPANHANTE_CHOICES)

    cuidado_especial = models.IntegerField(choices=CUIDADO_ESPECIAL_CHOICES)

    data_criacao = models.DateTimeField(auto_now_add=True)

    data_alteracao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "condicoes"
        ordering = ["-data_criacao"]
