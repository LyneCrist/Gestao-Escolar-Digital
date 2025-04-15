from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Paciente
from .forms import PacienteForm

from django.db import connection

from django.db.models import Count


def listar(request):

    context = {}

    context["pacientes"] = Paciente.objects.annotate(
        total_transportes=Count("transporte")
    ).order_by("-data_criacao")

    return render(request, "lista_pacientes.html", context)


def cadastrar(request):

    context = {}

    context["title"] = "Cadastro de Paciente"

    if request.method == "POST":

        context["form"] = PacienteForm(request.POST)

        if context["form"].is_valid():
            try:

                # print(context["form"].cleaned_data)

                context["form"].save()

                messages.success(request, "Paciente cadastrado com sucesso")

                return redirect("criar_paciente")

            except:

                messages.error(
                    request, "Ocorreu um erro durante o registro, tente novamente"
                )

                return render(request, "criar_paciente.html", context)

        context["erros"] = context["form"].errors.as_data()

    else:
        context["form"] = PacienteForm()

    return render(request, "criar_paciente.html", context)


def atualizar(request, id: int):

    context = {}

    paciente = Paciente.objects.get(id=id)

    if request.method == "POST":

        context["form"] = PacienteForm(request.POST, instance=paciente)

        if context["form"].is_valid():

            context["form"].save()

            return redirect("editar_paciente", paciente.pk)

        context["erros"] = context["form"].errors.as_data()

        print(context["erros"])

    context["id"] = paciente.pk

    context["form"] = PacienteForm(instance=paciente)

    return render(request, "editar_paciente.html", context)


def excluir(request, id: int):

    # if request.method == "POST":

    paciente = Paciente.objects.get(id=id)
    paciente.delete()

    return redirect("lista_pacientes")
