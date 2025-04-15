from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar, name="listar_estudantes"),
    path("cadastro/", views.cadastrar, name="criar_estudante"),
    path("edita/<int:id>", views.atualizar, name="editar_estudante"),
    path("exclui/<int:id>", views.excluir, name="excluir_estudante"),
]
