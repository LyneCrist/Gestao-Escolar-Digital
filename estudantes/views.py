from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from .forms import EstudanteForm
from .models import Estudante


def listar(request):

    context = {}

    context["estudantes"] = Estudante.objects.annotate(
        total_transportes=Count("transporte")
    ).order_by("-data_criacao")

    return render(request, "lista_estudantes.html", context)


def cadastrar(request):

    context = {}

    context["title"] = "Cadastro de Estudante"

    if request.method == "POST":

        context["form"] = EstudanteForm(request.POST)

        if context["form"].is_valid():
            try:

                # print(context["form"].cleaned_data)

                context["form"].save()

                messages.success(request, "Estudante cadastrado com sucesso")

                return redirect("criar_estudante")

            except:

                messages.error(
                    request, "Ocorreu um erro durante o registro, tente novamente"
                )

                return render(request, "criar_estudante.html", context)

        context["erros"] = context["form"].errors.as_data()

    else:
        context["form"] = EstudanteForm()

    return render(request, "criar_estudante.html", context)


def atualizar(request, id: int):

    context = {}

    estudante = Estudante.objects.get(id=id)

    if request.method == "POST":

        context["form"] = EstudanteForm(request.POST, instance=estudante)

        if context["form"].is_valid():

            context["form"].save()

            return redirect("editar_estudante", estudante.pk)

        context["erros"] = context["form"].errors.as_data()

        print(context["erros"])

    context["id"] = estudante.pk

    context["form"] = EstudanteForm(instance=estudante)

    return render(request, "editar_estudante.html", context)


def excluir(request, id: int):

    estudante = Estudante.objects.get(id=id)
    estudante.delete()

    return redirect("lista_estudantes")
