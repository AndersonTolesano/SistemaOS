from django.contrib import admin
from .models import Consultoria, MyUser, EmpresaMatriz, EmpresaFilial, \
    ContatoEmpresa, OrdemServico, Projeto, NovoCliente, ContatoCliente, Solicitante


admin.site.register(Consultoria)
admin.site.register(MyUser)
admin.site.register(EmpresaMatriz)
admin.site.register(EmpresaFilial)
admin.site.register(ContatoEmpresa)
admin.site.register(OrdemServico)
admin.site.register(Projeto)
admin.site.register(NovoCliente)
admin.site.register(ContatoCliente)
admin.site.register(Solicitante)