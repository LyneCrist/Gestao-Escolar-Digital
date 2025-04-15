from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar, name="listar_pacientes"),
    path("cadastro/", views.cadastrar, name="criar_paciente"),
    path("edita/<int:id>", views.atualizar, name="editar_paciente"),
    path("exclui/<int:id>", views.excluir, name="excluir_paciente"),
]
