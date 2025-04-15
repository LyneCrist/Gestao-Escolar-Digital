from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuarios.forms import UsuarioForm


def index(request):

    # context = {}

    # form = UsuarioForm()

    # context["form"] = form

    return render(request, "form.html")


def login(request):
    # if request.method == "POST":
    # form = RegisterForm(request.POST)
    # return super().metho

    return render(request, "login.html")


# @login_required(login_url='/auth/login')


def logout(request):
    return render(request, "login.html")


# @login_required(login_url='/auth/login')


def listar(request):

    return render(request, "lista.html")


# @login_required(login_url='/auth/login')


def cadastrar(request):

    return render(request, "forms.html")


# @login_required(login_url='/auth/login')


def editar(request, id):

    return render(request, "forms.html")


# @login_required(login_url='/auth/login')


def excluir(request, id):

    return render(request, "lista.html")
