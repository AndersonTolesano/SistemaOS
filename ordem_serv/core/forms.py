from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from .choices import (STATUS_NIVEL, STATUS_STATUS, STATUS_SLA, STATUS_ATIVO, STATUS_ATENDIMENTO)
from datetime import date

class UserCreatiomForm(UserCreationForm):
    first_name = forms.CharField(
        label = 'Nome',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Nome',
            }
        )
    )

    last_name = forms.CharField(
        label = 'Sobrenome',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control', 'placeholder': 'Sobrenome'
            }
        )
    )

    email = forms.CharField(
        label= 'Email',
        widget = forms.EmailInput(
            attrs = {
                'class': 'form-control', 'placeholder': 'Email'
            }
        )
    )

    password1 = forms.CharField(
        label= 'Senha',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Confirmar senha'
            }
        )
    )

    password2 = forms.CharField(
        label='Confirmar senha',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Confirmar senha'
            }
        )
    )

    celular = forms.CharField(
        label='Celular',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control phone_cell', 'placeholder': 'Celular com DDD'
            }
        )
    )

    nivel = forms.ChoiceField(
        label='nivel',
        choices=STATUS_NIVEL,
        widget=forms.Select(
            attrs={
                'class': 'form-control', 'placeholder': 'Nivel'
            }
        )
    )

    status = forms.ChoiceField(
        label='status',
        choices=STATUS_STATUS,
        widget=forms.Select(
            attrs={
                'class': 'form-control', 'placeholder': 'Status'
            }
        )
    )

    class Meta:
        model = models.MyUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'celular', 'nivel', 'status']


class EditUserCreatiomForm(forms.ModelForm):
    first_name = forms.CharField(
        label = 'Nome',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Nome',
            }
        )
    )

    last_name = forms.CharField(
        label = 'Sobrenome',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control', 'placeholder': 'Sobrenome'
            }
        )
    )

    email = forms.CharField(
        label= 'Email',
        widget = forms.EmailInput(
            attrs = {
                'class': 'form-control', 'placeholder': 'Email', 'readonly': 'readonly'
            }
        )
    )

    password1 = forms.CharField(
        label= 'Senha',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Confirmar senha'
            }
        )
    )

    password2 = forms.CharField(
        label='Confirmar senha',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Confirmar senha'
            }
        )
    )

    celular = forms.CharField(
        label='Celular',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control phone_cell', 'placeholder': 'Celular com DDD'
            }
        )
    )

    nivel = forms.ChoiceField(
        label='nivel',
        choices=STATUS_NIVEL,
        widget=forms.Select(
            attrs={
                'class': 'form-control', 'placeholder': 'Nivel'
            }
        )
    )

    status = forms.ChoiceField(
        label='status',
        choices=STATUS_STATUS,
        widget=forms.Select(
            attrs={
                'class': 'form-control', 'placeholder': 'Status'
            }
        )
    )

    class Meta:
        model = models.MyUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'celular', 'nivel', 'status']


class NovoClienteForm(forms.ModelForm):
    razao_social = forms.CharField(
        label='Razao Social',
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control', 'placeholder': 'Razao Social'
            }
        )
    )

    fantasia = forms.CharField(
        label='Fantasia',
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control', 'placeholder': 'Fantasia'
            }
        )
    )

    fone1= forms.CharField(
        label='Fone 1',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Fone 1'
            }
        )
    )

    fone2 = forms.CharField(
        label='Comercial',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Comercial'
            }
        )
    )

    celular = forms.CharField(
        label='Celular',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Celular'
            }
        )
    )

    email = forms.CharField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Email'
            }
        )
    )

    cnpj = forms.CharField(
        label='CNPJ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'CNPJ'
            }
        )
    )

    ie = forms.CharField(
        label='IE',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'IE'
            }
        )
    )

    ativo = forms.ChoiceField(
        label='Ativo',
        choices=STATUS_ATIVO,
        widget=forms.Select(
            attrs={
                'class': 'form-control', 'placeholder': 'Nao'
            }
        )
    )

    class Meta:
        model = models.NovoCliente
        fields = ['razao_social', 'fantasia', 'fone1', 'fone2', 'celular', 'email', 'cnpj', 'ie', 'ativo']


class ContatoClienteForm(forms.ModelForm):
    nome = forms.CharField(
        label='Nome',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Nome', 'id':'id_nome_contato'
            }
        )
    )

    telefone = forms.CharField(
        label='Telefone',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Telefone', 'id':'id_telefone_contato'
            }
        )
    )

    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Email', 'id':'id_email_contato'
            }
        )
    )

    class Meta:
        model = models.ContatoCliente
        fields = ['nome', 'telefone', 'email']


class SolicitanteForm(forms.ModelForm):
    nome = forms.CharField(
        label='Nome',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Nome', 'id': 'id_nome'
            }
        )
    )

    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Email', 'id': 'id_email'
            }
        )
    )

    telefone = forms.CharField(
        label='Telefone',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Telefone', 'id': 'id_telefone'
            }
        )
    )

    setor = forms.CharField(
        label='Setor',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Setor', 'id': 'id_setor'
            }
        )
    )

    class Meta:
        model = models.Solicitante
        fields = ['nome', 'email', 'telefone', 'setor']


class InserirNovaOrdemForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        label='Cliente',
        queryset=models.NovoCliente.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control', 'placeholder': 'Cliente'
            }
        )
    )

    tipoDeAtendimento = forms.ChoiceField(
        label='Tipo de atendimento',
        choices= STATUS_ATENDIMENTO,
        widget= forms.Select(
            attrs={
                'class': 'form-control', 'placeholder': 'Tipo de Atendimento'
            }
        )
    )

    responsavel = forms.CharField(
        label='Responsavel',
        widget= forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Responsavel'
            }
        )
    )

    analista = forms.CharField(
        label='Analista',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Analista'
            }
        )
    )

    solicitante = forms.CharField(
        label='Solicitante',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Solicitante'
            }
        )
    )

    dataAtendimento = forms.DateField(
        label='Data de atendimento',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Data de atendimento'
            }
        )
    )

    hora_entrada = forms.TimeField(
        label='Hora de entrada',
        widget=forms.TimeInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Hora de entrada'
            }
        )
    )

    hora_saida = forms.TimeField(
        label='Hora de saida',
        widget=forms.TimeInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Hora de saida'
            }
        )
    )

    translado = forms.CharField(
        label='Translado',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Translado'
            }
        )
    )

    descritivo = forms.CharField(
        label='Descritivo',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control', 'placeholder': 'Descritivo'
            }
        )
    )

    class Meta:
        model = models.OrdemServico
        exclude = ['usuario']
        fields = ['cliente', 'tipoDeAtendimento', 'responsavel', 'analista', 'solicitante',
                  'dataAtendimento','hora_entrada', 'hora_saida', 'translado', 'descritivo']


class NovoProjetoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        label= 'Cliente',
        queryset= models.NovoCliente.objects.all(),
        widget = forms.Select(
            attrs={
                'class': 'form-control col-sm-12', 'placeholder': 'Cliente'
            }
        )
    )

    nome_projeto = forms.CharField(
        label = 'Nome do Projeto',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Nome do Projeto'
            }
        )
    )

    inicio = forms.DateTimeField(
        label = 'Inicio',
        widget= forms.DateInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Inicio'
            }
        )
    )

    termino = forms.DateTimeField(
        label='Termino',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Termino'

            }
        )
    )

    status = forms.ChoiceField(
        label = 'Status',
        choices = STATUS_STATUS,
        widget = forms.Select(
            attrs={
                'class': 'form-control', 'placeholder': 'Status'
            }
        )
    )

    tipo_atendimento = forms.ChoiceField(
        label= 'Tipo de Atendimento',
        choices= STATUS_ATENDIMENTO,
        widget= forms.Select(
            attrs= {
                'class': 'form-control', 'placeholder': 'Tipo de Atendimento'
            }
        )
    )

    paga_almoco = forms.ChoiceField(
        required=False,
        label= 'Paga almoço?',
        choices = STATUS_ATIVO,
        widget = forms.Select(
            attrs={
                'class': 'form-control', 'placeholder': 'Paga almoço?'
            }
        )
    )

    paga_translado = forms.ChoiceField(
        required=False,
        label = 'Paga Translado?',
        choices = STATUS_ATIVO,
        widget = forms.Select(
            attrs={
                'class': 'form-control', 'placeholder': 'Paga translado?'
            }
        )
    )

    tempo_viagem = forms.CharField(
        label = 'Tempo de Viagem',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control', 'placeholder': 'Tempo de viagem'
            }
        )
    )

    valor_hora = forms.CharField(
        label = 'Valor da Hora',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control', 'placeholder': 'Valor da Hora'
            }
        )
    )

    observacoes = forms.CharField(
        label= 'Observações',
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control', 'placeholder': 'Observações'
            }
        )
    )

    class Meta:
        model = models.Projeto
        exclude= ['usuario']
        fields = ['cliente', 'nome_projeto', 'inicio', 'termino', 'status', 'tipo_atendimento',
                  'paga_almoco', 'paga_translado', 'tempo_viagem', 'valor_hora', 'observacoes' ]

