#from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from .forms import SignUpForm
from django.core.exceptions import ValidationError

def check_username(request):
    username = request.GET.get('username', '')
    exists = get_user_model().objects.filter(username__iexact=username).exists()
    return JsonResponse({'exists': exists})

def signup_view(request):
    try:
        if request.method == 'POST':
            print("Dados recebidos:", request.POST)  # Debug
            
            form = SignUpForm(request.POST)
            if form.is_valid():
                try:
                    user = form.save()
                    login(request, user)
                    user.tipo_usuario = form.cleaned_data['tipo_usuario']
                    user.terms_accepted = form.cleaned_data['terms_accepted']
                    user.save()

                    return redirect('lista_pacientes')  # Nome da URL, não do template
                
                except IntegrityError as e:
                    print(f"Erro de banco de dados: {str(e)}")
                    form.add_error(None, "Erro ao criar conta. Tente novamente.")
                
                except ValidationError as e:
                    print(f"Erro de validação: {str(e)}")
                    form.add_error(None, e.messages)
            
            else:
                print("Erros no formulário:", form.errors)  # Debug
                return render(request, 'login.html', {
                    'form': form,
                    'form_errors': form.errors
                })
        
        else:
            form = SignUpForm()
        
        return render(request, 'login.html', {'form': form})
    
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")
        # Em produção, redirecione para uma página de erro
        return render(request, 'login.html', {
            'form': SignUpForm(),
            'error_message': "Ocorreu um erro inesperado. Tente novamente."
        })

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('senha')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_pacientes.html')  # Altere para sua URL
    return render(request, 'login.html')

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
