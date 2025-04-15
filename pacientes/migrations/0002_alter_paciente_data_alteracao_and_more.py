# Generated by Django 5.0.4 on 2024-04-17 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pacientes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paciente",
            name="data_alteracao",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="paciente",
            name="data_criacao",
            field=models.DateTimeField(auto_created=True),
        ),
        migrations.AlterField(
            model_name="paciente",
            name="ponto_referencia",
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name="paciente",
            name="rua",
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name="paciente",
            name="telefone",
            field=models.CharField(max_length=15),
        ),
    ]
