# Generated by Django 5.0.4 on 2025-04-17 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Paciente",
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
                ("nome", models.CharField(max_length=60)),
                ("data_de_nascimento", models.DateField()),
                (
                    "genero",
                    models.IntegerField(
                        choices=[(1, "Feminino"), (2, "Masculino"), (3, "Outros")]
                    ),
                ),
                ("cartao_sus", models.CharField(max_length=15, unique=True)),
                (
                    "agendamento_fixo",
                    models.IntegerField(choices=[(1, "Sim"), (2, "Não")]),
                ),
                ("telefone", models.CharField(max_length=13)),
                ("rua", models.CharField(max_length=60)),
                ("numero", models.CharField(max_length=7)),
                ("complemento", models.CharField(max_length=60, null=True)),
                ("ponto_referencia", models.CharField(max_length=60, null=True)),
                ("status", models.IntegerField(default=1)),
                ("data_criacao", models.DateTimeField(auto_now_add=True)),
                ("data_alteracao", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "pacientes",
                "ordering": ["-data_criacao"],
            },
        ),
    ]
