from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar, name="listar_transportes"),
    path(
        "paciente_transportes/<int:id>",
        views.paciente_transportes,
        name="paciente_transportes",
    ),
    path("cadastrar/<int:paciente_id>", views.cadastrar, name="criar_transporte"),
    path("editar/<int:id>", views.editar, name="editar_transporte"),
    path("cancelar/<int:id>", views.cancelar, name="cancelar_transporte"),
    path("finalizar/<int:id>", views.finalizar, name="finalizar_transporte"),
]
