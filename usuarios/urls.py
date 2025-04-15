from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('cadastro/', views.cadastrar, name="cadastro_usuario"),
    path('lista/', views.listar, name="lista_usuarios"),
]
