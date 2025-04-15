from django.shortcuts import render, redirect
from condicoes.forms import CondicaoForm
from .models import Condicao
from pacientes.models import Paciente

from django.contrib import messages


def listar(request):

    context = {}

    context["condicoes"] = Condicao.objects.all()[:15]

    return render(request, "lista_condicoes.html", context)


def cadastrar(request, paciente_id: int):

    context = {}

    context["title"] = "Cadastra Condição"

    if request.method == "POST":

        context["form"] = CondicaoForm(request.POST)

        if context["form"].is_valid():
            try:

                # print(context["form"].cleaned_data)

                context["form"].save()

                messages.success(request, "Condição cadastrada com sucesso")

                return redirect("listar_condicoes")

            except:

                messages.error(
                    request, "Ocorreu um erro durante o registro, tente novamente"
                )

                return render(request, "criar_condicao.html", context)

        context["erros"] = context["form"].errors.as_data()

    else:

        paciente = Paciente.objects.get(id=paciente_id)
        context["paciente"] = paciente
        context["paciente_id"] = paciente.pk
        context["form"] = CondicaoForm()

    return render(request, "criar_condicao.html", context)


def atualizar(request, id: int):

    context = {}

    condicao = Condicao.objects.get(id=id)

    if request.method == "POST":

        context["form"] = CondicaoForm(request.POST, instance=condicao)

        if context["form"].is_valid():

            context["form"].save()

            return redirect("editar_condicao", condicao.pk)

        context["erros"] = context["form"].errors.as_data()

        print(context["erros"])

    context["id"] = condicao.pk

    context["form"] = CondicaoForm(instance=condicao)

    return render(request, "editar_condicao.html", context)


def excluir(request, id: int):

    # if request.method == "POST":

    condicao = Condicao.objects.get(id=id)
    condicao.delete()

    return redirect("listar_condicoes")
