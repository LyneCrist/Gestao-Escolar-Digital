from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name="logout"),
    path('cadastro/', views.cadastrar, name="cadastro_usuario"),
    path('lista/', views.listar, name="lista_usuarios"),
]
