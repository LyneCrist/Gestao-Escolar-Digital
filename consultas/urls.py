from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar, name="lista_consultas"),
    path("cadastro/", views.cadastrar, name="cadastra_consulta"),
    path("edita/", views.atualizar, name="edita_consulta"),
    path("exclui/", views.excluir, name="exclui_consulta"),
]
