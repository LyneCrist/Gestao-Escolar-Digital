from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar, name="listar_condicoes"),
    path("cadastrar/<int:paciente_id>", views.cadastrar, name="criar_condicao"),
    path("editar/<int:id>", views.atualizar, name="editar_condicao"),
    path("excluir/<int:id>", views.excluir, name="excluir_condicao"),
]
