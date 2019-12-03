from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from core.choices import (STATUS_OS, STATUS_PROJETO, STATUS_EQUIPE, STATUS_NIVEL, STATUS_STATUS, STATUS_SLA,
                          STATUS_ATIVO, TIPO_CONTATO_CHOICES, STATUS_ATENDIMENTO)
#from cloudinary.models import CloudinaryField


class NovoCliente(models.Model):
    razao_social = models.TextField(
        max_length=255,
        blank=True,
        null=True
    )

    fantasia = models.TextField(
        max_length=255,
        blank=True,
        null=True
    )

    fone1 = models.TextField(
        max_length=255,
        blank=True,
        null=True
    )

    fone2 = models.TextField(
        max_length=255,
        blank=True,
        null=True
    )

    celular = models.TextField(
        max_length=255,
        blank=True,
        null=True
    )

    email = models.EmailField(
        max_length=255,
        blank=True,
        null=True
    )

    cnpj = models.TextField(
        unique=True,
        max_length=255,
        blank=True,
        null=True
    )

    ie = models.TextField(
        max_length=255,
        blank=True,
        null=True
    )

    ativo = models.CharField(
        default='Nao',
        max_length=1,
        choices=STATUS_ATIVO
    )

    def __str__(self):
        return "{} - {} - {}".format(self.razao_social, self.fantasia, self.fone1)

    def __repr__(self):
        return "{} - {} - {}".format(self.razao_social, self.fantasia, self.fone1)


class ContatoCliente(models.Model):
    nome = models.TextField(
        max_length=255,
        blank=True,
        null=True
    )

    telefone = models.TextField(
        max_length=255,
        blank=True,
        null=True
    )

    Email = models.EmailField(
        max_length=255,
        blank=True,
        null=True
    )
    
class Contato(models.Model):
    tipo = models.CharField(
        choices=TIPO_CONTATO_CHOICES,
        max_length=3,
        default='1',
    )
    
    contato = models.CharField(
        verbose_name=_('Contato'),
        max_length=255,
        blank=True, null=True,
        help_text=('informe o contato'),
    )

    def __str__(self):
        return self.contato('contato')

    def __repr__(self):
        return self.contato



class Consultoria(models.Model):
    razao_social = models.CharField(
        max_length=255, 
        blank=True, null=True
    )
    
    cnpj = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    fantasia = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    nome = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    telefone = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    email = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    
class EmailUserManager(BaseUserManager):
    def create_user(self, *args, **kwargs):
        email = kwargs["email"]
        email = self.normalize_email(email)
        password = kwargs["password"]
        kwargs.pop("password")

        if not email:
            raise ValueError(_('Necessário um email válido'))

        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
    
class MyUser(PermissionsMixin, AbstractBaseUser):
    first_name = models.CharField(
        verbose_name=_('Nome'),
        max_length=255,
        blank=False,
        help_text=_('Informe seu nome'),
    )

    last_name = models.CharField(
        verbose_name=_('Sobrenome'),
        max_length=255,
        blank=False,
        help_text=_('Informe seu sobrenome'),
    )

    email = models.EmailField(
        verbose_name=_('Email'),
        unique=True,
    )

    telefone = models.CharField(
        verbose_name=_('telefone'),
        max_length=255,
        blank=True, null=True,
        help_text=_('Informe o numero de celular'),
    )
    
    celular = models.CharField(
        verbose_name=_('Celular'),
        max_length=255,
        blank=True, null=True,
        help_text=_('Informe o número do celular'),
    )

    consultoria = models.ForeignKey(
        Consultoria,
        on_delete=models.DO_NOTHING,
        blank=True, null=True,
    )

    equipe = models.CharField(
        default='5',
        max_length=1,
        choices=STATUS_EQUIPE)

    #photo = CloudinaryField(
    #   'image',
    #    blank=True, null=True,
    #    width_field='image_width', height_field='image_height',
    #)

    cpf = models.CharField(
        verbose_name=_('CPF'),
        max_length=255,
        blank=True, null=True,
        help_text=_('Informe seu CPF'),
    )

    nivel = models.CharField(
        default='4',
        max_length=1,
        choices=STATUS_NIVEL)

    status = models.CharField(
        default='2',
        max_length=1,
        choices=STATUS_STATUS)

    reset_pass = models.BooleanField(default=False)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    objects = EmailUserManager()

    
class EmpresaMatriz(models.Model):
    empresa = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    nome = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    razao_social = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    cnpj = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    fantasia = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    endereco = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    complemento = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    bairro = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    cidade = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    cep = models.CharField(
        max_length=255, 
        blank=True, 
        null=True)
    
    uf = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )


class EmpresaFilial(models.Model):
    razao_social = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    cnpj = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    fantasia = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    nome = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    empresa_matriz = models.ForeignKey\
        (EmpresaMatriz, blank=True, null=True, on_delete=models.DO_NOTHING)
    
    endereco = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    bairro = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    cidade = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    uf = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    
class ContatoEmpresa(models.Model):
    cliente = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    contato = models.CharField(
        max_length=255, 
        blank=True, null=True
    )
    
    telefone = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )
    
    email = models.CharField(
        max_length=255, 
        blank=True, 
        null=True)

class Solicitante(models.Model):
    cliente = models.ForeignKey \
        (NovoCliente,
         blank=True,
         null=True,
         on_delete=models.DO_NOTHING)

    nome = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    email = models.EmailField(
        max_length=255,
        blank=True,
        null=True
    )

    telefone = models.TextField(
        max_length=255,
        blank=True,
        null=True
    )

    setor = models.TextField(
        max_length=255,
        blank=True,
        null=True
    )

    def __str__(self):
        return "{} - {} - {}".format(self.nome, self.telefone, self.setor)

    def __repr__(self):
        return "{} - {} - {}".format(self.nome, self.telefone, self.setor)
    
class OrdemServico(models.Model):
    data = models.DateTimeField(
            auto_now_add=True
    )
    
    cliente = models.ForeignKey(
        NovoCliente,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    
    tipoDeAtendimento = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    
    responsavel = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    analista = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    
    solicitante = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    
    dataAtendimento = models.DateField(
        blank=True,
        null=True
    )
    
    hora_entrada = models.TimeField(
        blank=True, 
        null=True
    )
    
    hora_saida = models.TimeField(
        blank=True, 
        null=True
    )
    
    translado = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    
    descritivo = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )

    usuario = models.ForeignKey(
        MyUser,
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING
    )

    apagado = models.BooleanField(default=False)
    
    
class Projeto(models.Model):
    cliente = models.ForeignKey(
        NovoCliente,
         blank=True,
         null=True,
         on_delete=models.DO_NOTHING
    )

    tipo_atendimento = models.CharField(
        default='1',
        max_length=1,
choices=STATUS_ATENDIMENTO
    )

    nome_projeto = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    
    inicio = models.DateTimeField(
        blank=True, 
        null=True
    )
    
    termino = models.DateTimeField(
        blank=True, 
        null=True
    )

    status = models.CharField(
        default='1',
        max_length=1,
        choices=STATUS_STATUS
    )
    
    paga_almoco = models.CharField(
        default='1',
        max_length=1,
        choices=STATUS_ATIVO
    )
    
    paga_translado = models.CharField(
        default='1',
        max_length=1,
        choices=STATUS_ATIVO
    )
    
    tempo_viagem = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )


    valor_hora = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    
    anexo = models.FileField(
        blank=True, 
        null=True
    )
    
    observacoes = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )

    valor_fechado = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    usuario = models.ForeignKey(
        MyUser,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
    )

    apagado = models.BooleanField(default=False)