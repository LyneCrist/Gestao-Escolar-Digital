from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name="lista_enderecos"),
    path('cadastro/', views.cadastrar, name="cadastro_endereco"),
    path('edita/', views.atualizar, name="edita_endereco"),
    path('exclui/', views.excluir, name="exclui_endereco"),
]
