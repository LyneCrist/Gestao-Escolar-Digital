from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import TransporteForm
from .models import Transporte
from .core import TransporteCore
from .errors import CancelarTransporteError
from .choices import STATUS_CHOICES

from pacientes.models import Paciente
from django.contrib import messages
from django.db.models import F
from django.db.models import QuerySet
from utils.choice_utils import filter_status_choices


def listar(request):

    transportes = (
        Transporte.objects.annotate(
            nome=F("paciente__nome"),
            data=F("data_de_transporte"),
            horario=F("horario_de_atendimento"),
        )
        .values(
            "pk",
            "nome",
            "data",
            "horario",
            "status",
        )
        .order_by("-data_criacao")[:5]
    )

    context = {
        "transportes": map(
            lambda transporte: filter_status_choices(transporte, STATUS_CHOICES),
            transportes,
        )
    }

    return render(request, "lista_transportes.html", context)


def paciente_transportes(request, id: int):

    context = {}

    transportes: QuerySet[Transporte] = Transporte.objects.filter(paciente=id)

    context["nome"] = transportes[0].paciente.nome

    context["transportes"] = transportes

    return render(request, "paciente_transportes.html", context)


def cadastrar(request, paciente_id: int):

    paciente: Paciente = Paciente.objects.get(id=paciente_id)

    context = {}

    context["title"] = "Cadastra Transporte"
    context["paciente_id"] = paciente.pk
    context["nome"] = paciente.nome
    context["cod_sus"] = paciente.cartao_sus

    if request.method == "POST":

        context["form"] = TransporteForm(request.POST)

        if context["form"].is_valid():
            try:

                # print(context["form"].cleaned_data)

                novo_transporte: Transporte = context["form"].save(commit=False)

                novo_transporte.paciente = paciente

                novo_transporte.save()

                # messages.success(request, "Transporte cadastrado com sucesso")

                # return redirect("listar_por_paciente", paciente_id=paciente.pk)
                return redirect("listar_pacientes")

            except Exception as exc:

                messages.error(
                    request, "Ocorreu um erro durante o registro, tente novamente"
                )

                return render(request, "criar_transporte.html", context)

        context["errors"] = context["form"].errors.as_data()

    else:
        context["form"] = TransporteForm()

    return render(request, "criar_transporte.html", context)


def editar(request, id: int):

    context = {}

    transporte = Transporte.objects.get(id=id)

    if request.method == "POST":

        context["form"] = TransporteForm(request.POST, instance=transporte)

        if context["form"].is_valid():

            context["form"].save()

            return redirect("editar_condicao", transporte.pk)

        context["erros"] = context["form"].errors.as_data()

    context["id"] = transporte.pk
    context["nome"] = transporte.paciente.nome
    context["cod_sus"] = transporte.paciente.cartao_sus
    context["form"] = TransporteForm(instance=transporte)

    return render(request, "editar_transporte.html", context)


def cancelar(request, id):

    try:

        transporte = Transporte.objects.get(id=id)

        if request.method == "GET":

            return render(request, "cancelar_transporte.html", {"id": transporte.pk})

        TransporteCore().validar_cancelamento(
            datetime.combine(
                transporte.data_de_transporte, transporte.horario_de_atendimento
            )
        )

        transporte.status = 2

        transporte.save()

        return redirect("listar_transportes")

    except CancelarTransporteError as exc:

        messages.error(request, f"{exc.message}\n{exc.description}")

        return redirect("listar_transportes")


def finalizar(request, id: int):

    # if request.method == "POST":

    # transporte = Transporte.objects.get(id=id)
    # transporte.delete()

    return redirect("finalizar_transporte")
