from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include
from usuarios import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="/auth/login/", permanent=True)),
    path("transportes/", include("transportes.urls")),
    path("pacientes/", include("pacientes.urls")),
    path("condicoes/", include("condicoes.urls")),
    path("estudantes/", include("estudantes.urls")),
    # path("consultas/", include("consultas.urls")),
    # path("enderecos/", include("enderecos.urls")),
    path("auth/", include("usuarios.urls")),
    path('auth/signup/', views.signup_view, name='signup'),
    path('auth/check_username/', views.check_username, name='check_username'),
    #path('pacientes/', include('listar_pacientes.urls', namespace='pacientes')),
]
