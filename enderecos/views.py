from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def listar(request):
    return render(request, 'listar.html')


def cadastrar(request):
    return render(request, 'form.html')


def atualizar(request):
    return render(request, 'form.html')


def excluir(request):
    return render(request, 'listar.html')
