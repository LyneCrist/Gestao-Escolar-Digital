from django.db import models

MOTIVO_CHOICES = (
    (0, "--Selecione--"),
    (1, "Retorno"),
    (2, "Exames"),
    (3, "Quimioterapia"),
    (4, "Internação"),
    (5, "Procedimento"),
    (6, "Radioterapia"),
    (7, "Primeira-Consulta"),
    (8, "Outros"),
)

STATUS_CHOICES = ((1, "Agendado"), (2, "Cancelado"), (3, "Realizado"))

AGENDAMENTO_FIXO_CHOICES = ((1, "Sim"), (2, "Não"))

GENERO_CHOICES = ((1, "Feminino"), (2, "Masculino"), (3, "Outros"))
