from django.contrib.auth import views, authenticate
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from . import models
from .forms import UserCreatiomForm, NovoClienteForm, InserirNovaOrdemForm, NovoProjetoForm, ContatoClienteForm, SolicitanteForm, EditUserCreatiomForm
from django.views.decorators.csrf import csrf_exempt


#usuário#
def home(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect(reverse('login'))
    
    
def novo_usuario(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                usuario = form.save(commit=False)
                usuario.save()
                return HttpResponseRedirect(reverse('https://google.com.br'))
        else:
            form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'registration/novo_usuario.html', context)
    else:
        return HttpResponseRedirect(reverse('core:home'))
    
    
def usuarios(request):
    if request.user.is_authenticated:
        usuarios = models.MyUser.objects.all()
        context = {
            'usuarios': usuarios
        }
        return render(request, 'registration/usuarios.html', context)
    else:
        return HttpResponseRedirect(reverse('core:home'))
    
    
def alterar_senha(request):
    if request.user.is_authenticated:
        error = False
        success = False
        if request.method == 'POST':
            old_password = request.POST.get('old_password', None)
            new_password1 = request.POST.get('new_password1', None)
            new_password2 = request.POST.get('new_password2', None)
            if not request.user.check_password(old_password):
                error = True
            elif new_password1 != new_password2:
                error = True
            else:
                usuario = models.MyUser.objects.get(pk=request.user.pk)
                usuario.set_password(new_password1)
                usuario.save()
                success = True
        context = {
            'error': error,
            'success': success
        }
        return render(request, 'registration/alterar_senha.html', context)
    else:
        return HttpResponseRedirect(reverse('core:home'))
    
    
def usuarioList(request, edit=False):
    usuario = models.MyUser.objects.all()
    context = {
        'usuario': usuario,
        'edit': edit
    }
    return render(request, 'usuario_list.html', context)


def cadastroUsuario(request):
    novoUsuario = UserCreatiomForm()
    error = False
    success = False
    if request.method == 'POST':
        novoUsuario = UserCreatiomForm(request.POST)
        if novoUsuario.is_valid():
            novoUsuario.save()
            success = True
        else:
            error = novoUsuario.errors

    context = {
        'error': error,
        'form': novoUsuario,
        'success': success
    }
    return render(request, 'cadastro_usuario.html', context)


def NovoCliente(request):
    contatoCliente = ContatoClienteForm()
    novoCliente = NovoClienteForm()

    context = {
        'form': novoCliente,
        'contato': contatoCliente
    }
    return render(request, 'novo_cliente.html', context)


def adicionar_contato (request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                form = SolicitanteForm(request.POST)
                if form.is_valid():
                    contato = form.save(commit=False)
                    contato.cliente = request.session.get('id_cliente')
                    contato.save()
                    request.session['id_cliente'] = ''
                
                response = {'sucesso': True}
                return JsonResponse(response, safe=False)
            except Exception as e:
                print(e)
                response = {'error': True}
                return JsonResponse(response, safe=False)


@csrf_exempt
def SalvarCliente(request):
    if request.method == 'POST':
        razaoSocial = request.POST.get('razaoSocial', None)
        fantasia = request.POST.get('fantasia', None)
        fone1 = request.POST.get('fone1', None)
        fone2 = request.POST.get('fone2', None)
        celular = request.POST.get('celular', None)
        email = request.POST.get('email', None)
        cnpj = request.POST.get('cnpj', None)
        ie = request.POST.get('ie', None)
        ativo = request.POST.get('ativo', None)

        if not razaoSocial or not fantasia or not fone1 or not email or not cnpj:
            response={'error': True}
            return JsonResponse(response, safe=False)

        try:
            novoCliente = models.NovoCliente.objects.filter(
                cnpj=cnpj
            )
            if novoCliente:
                response = {
                    'existe': True
                }
                return JsonResponse(response, safe=False)

            models.NovoCliente.objects.create(
                razao_social=razaoSocial,
                fantasia=fantasia,
                fone1=fone1,
                fone2=fone2,
                celular=celular,
                email=email,
                cnpj=cnpj,
                ie=ie,
                ativo=ativo
            )
            response={'sucesso': True}
            return JsonResponse(response, safe=False)
        except Exception as e:
            print(e)
            response={'falha': True}
            return JsonResponse(response, safe=False)


@csrf_exempt
def SalvarSolicitante(request):
    if request.method == 'POST':
        cliente = models.NovoCliente.objects.get(id=int(request.session.get('id_cliente')))
        btnnome = request.POST.get('nome', None)
        btnemail = request.POST.get('email', None)
        btntelefone = request.POST.get('telefone', None)
        btnsetor = request.POST.get('setor', None)
        print(request.session.get('id_cliente'))
        try:
            models.Solicitante.objects.create(
                nome=btnnome,
                email=btnemail,
                telefone=btntelefone,
                setor=btnsetor,
                cliente=cliente
            )
            response = {'sucesso': True}
            return JsonResponse(response, safe=False)
        except Exception as e:
            print(e)
            response = {'error': True}
            return JsonResponse(response, safe=False)


def ListaCliente(request, edit=False):
    clientes = models.NovoCliente.objects.all()
    
    context={
        'clientes': clientes,
        'edit': edit
    }
    return render(request, 'lista_clientes.html', context)


def ListaContato(request, pk):
    print(pk)
    request.session['id_cliente'] = str(pk)
    solicitantes = models.Solicitante.objects.filter(cliente=pk)
    contato = SolicitanteForm()
    
    context={
        'form': solicitantes,
        'contato': contato
    }
    return render(request, 'adicionar_contato.html', context)


def edit_cliente(request, pk):
    if request.user.is_authenticated:
        cliente = models.NovoCliente.objects.get(pk=pk)
        if request.method == 'POST':
            form = NovoClienteForm(request.POST, instance=cliente)
            if form.is_valid():
                form.save()
                return redirect('core:lista_cliente', edit=True)
        else:
            form = NovoClienteForm(instance=cliente)

        context = {
            'form': form,
            'edit': True
        }
        return render(request, 'novo_cliente.html', context)
    else:
        return HttpResponseRedirect(reverse('core:home'))


def delete_cliente (request, pk):
    if request.user.is_authenticated:
        if pk:
            models.NovoCliente.objects.filter(pk=pk).update(
                ativo=False
            )
            context={
                'cliente': 'cliente', 'edit': 'True'
            }
        return render(request, 'lista_clientes.html', context=context)
    else:
        return HttpResponseRedirect(reverse('core:lista_cliente'))


def visualizarCliente (request, pk):
    cliente = models.NovoCliente.objects.filter(pk=pk)
    solicitante = models.Solicitante.objects.filter(pk=pk)
    context = {
        'cliente': cliente,
        'solicitante': solicitante
    }
    return render (request, 'visualizar_cliente.html', context)


def edit_usuario(request, pk):
    if request.user.is_authenticated:
        usuario = models.MyUser.objects.get(pk=pk)
        if request.method == 'POST':
            form = EditUserCreatiomForm(request.POST, instance=usuario)
            if form.is_valid():
                form.save()
                return redirect('core:usuario_list', edit=True)
        else:
            form = EditUserCreatiomForm(instance=usuario)

        context = {
            'form': form,
            'edit': True
        }
        return render (request, 'cadastro_usuario.html', context)
    else:
        return HttpResponseRedirect(reverse('core:home'))


def nova_ordem(request):
    if request.user.is_authenticated:
        form = InserirNovaOrdemForm()
        error = False
        success = False
        if request.method == 'POST':
            form = InserirNovaOrdemForm(request.POST)
            if form.is_valid():
                novaOrdem = form.save(commit=False)
                novaOrdem.usuario = request.user
                novaOrdem.save()
                success = True
            else:
                error = form.errors
        context={
            'form': form,
            'error': error,
            'success': success
        }
        return render(request, 'nova_ordemservico.html', context)


def lista_ordem_de_servico(request):
    ordemDeServico = models.OrdemServico.objects.all()
    context={
        'ordemDeServico':ordemDeServico
    }
    return render(request, 'lista_ordem_de_servico.html', context)


def novo_projeto(request):
    if request.user.is_authenticated:
        form = NovoProjetoForm()
        sucesso = False
        error = False
        if request.method == 'POST':
            form = NovoProjetoForm(request.POST)
            if form.is_valid():
                projeto = form.save(commit=False)
                projeto.usuario = request.user
                projeto.save()
                sucesso = True
            else:
                error = form.errors
        context={
            'form':form,
            'sucesso':sucesso,
            'error':error
        }
        return render(request, 'novo_projeto.html', context)


def lista_projeto (request, pk):
    print(pk)
    request.session['id_cliente'] = str(pk)
    listaProjeto = models.Projeto.objects.filter(cliente=pk)
    projeto = NovoProjetoForm()

    context = {
        'listaProjeto': listaProjeto,
        'projeto': projeto
    }
    return render (request, 'novo_projeto.html', context)


def lista_geral_projetos(request):
        # listaProjetos = models.Projeto.objects.all()
        #     context={
        #         'listaProjeto':listaProjetos
        #     }
        return render(request, 'lista_geral_projeto.html')









