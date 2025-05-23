# Generated by Django 5.0.4 on 2025-05-15 03:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("pacientes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transporte",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nota", models.FloatField(blank=True, null=True)),
                ("descricao_motivo", models.CharField(max_length=60)),
                ("materia", models.CharField(max_length=60)),
                ("observacao", models.CharField(max_length=60)),
                (
                    "status",
                    models.IntegerField(
                        choices=[(1, "Agendado"), (2, "Cancelado"), (3, "Realizado")],
                        default=1,
                    ),
                ),
                ("data_criacao", models.DateTimeField(auto_now_add=True)),
                ("data_alteracao", models.DateTimeField(auto_now=True)),
                (
                    "paciente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pacientes.paciente",
                    ),
                ),
            ],
            options={
                "db_table": "transportes",
                "ordering": ["-data_criacao"],
            },
        ),
    ]
