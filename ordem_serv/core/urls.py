from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('lista/projeto/', views.lista_projeto, name='lista_projeto'),
    path('novo/projeto/', views.novo_projeto, name='novo_projeto'),
    # path('lista/projeto/', views.lista_projeto, name='lista_projeto'),
    path('nova/ordem/', views.nova_ordem, name='nova_ordem'),
    path('lista/ordem/', views.lista_ordem_de_servico, name='lista_ordem_de_servico'),
    path('lista/geral/projetos/',views.lista_geral_projetos, name='lista_geral_projeto'),
    path('lista/cliente/',views.ListaCliente, name='lista_cliente'),
    path('novo/cliente/', views.NovoCliente, name='novo_cliente'),
    path('salvar/cliente/', views.SalvarCliente, name='salvar_cliente'),
    # path('salvar/contato/', views.SalvarContato, name='salvar_contato'),
    path('lista/contato/<int:pk>/', views.ListaContato, name='lista_contato'),
    path('visualizar/cliente/<int:pk>/', views.visualizarCliente, name='visualizar_cliente'),
    path('salvar/solicitante/', views.SalvarSolicitante, name='salvar_solicitante'),
    path('adicionar/contato/', views.adicionar_contato, name='adicionar_contato'),
    path('edit/cliente/<int:pk>/', views.edit_cliente, name='edit_cliente'),
    path('delete/cliente/<int:pk>/', views.delete_cliente, name='delete_cliente'),
    path('edit/usuario/<int:pk>/', views.edit_usuario, name='edit_usuario'),
    path('cadastro/usuario/', views.cadastroUsuario, name='cadastro_usuario'),
    path('usuario/list/', views.usuarioList, name='usuario_list'),
    path('<str:edit>/usuario/list/', views.usuarioList, name='usuario_list'),
    path('alterar/senha/', views.alterar_senha, name='alterar_senha'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('novo/usuario/', views.novo_usuario, name='novo_usuario'),
    path('', views.home, name='home'),
]
app_name = 'core'
