from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="/transportes/")),
    path("transportes/", include("transportes.urls")),
    path("pacientes/", include("pacientes.urls")),
    path("condicoes/", include("condicoes.urls")),
    path("estudantes/", include("estudantes.urls")),
    # path("consultas/", include("consultas.urls")),
    # path("enderecos/", include("enderecos.urls")),
    # path("auth/", include("usuarios.urls")),
]
