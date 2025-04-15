from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def listar(request):
    return render(request, "lista_consultas.html")


def cadastrar(request):
    return render(request, "formulario_consulta.html")


def atualizar(request):
    return render(request, "formulario_consulta.html")


def excluir(request):
    return render(request, "lista_consultas.html")
