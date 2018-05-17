from django.db import models
from django.utils import timezone

# Create your models here.
class Empresa(models.Model):

    class Meta:
        db_table='TB_EMPRESA'

    id_empresa = models.IntegerField(primary_key=True, db_column='ID_EMPRESA')
    cnpj = models.CharField(max_length=14, db_column='DS_CNPJ')
    razao_social = models.CharField(max_length=100, db_column='DS_RAZAO_SOCIAL')
    logradouro = models.CharField(max_length=100, db_column='DS_ENDERECO_LOGRADOURO')
    numero = models.IntegerField(db_column='NR_ENDERECO_NUMERO')
    bairro = models.CharField(max_length=40, db_column='DS_ENDERECO_BAIRRO')
    cidade = models.CharField(max_length=80, db_column='DS_ENDERECO_CIDADE')
    estado = models.CharField(max_length=40, db_column='DS_ENDERECO_ESTADO')
    cep = models.IntegerField(db_column='NR_ENDERECO_CEP')
    telefone = models.CharField(max_length=14, db_column='DS_TELEFONE')

    def __str__(self):
        return self.razao_social

class Funcionario(models.Model):

    class Meta:
        db_table='TB_FUNCIONARIO'

    id_funcionario = models.IntegerField(primary_key=True, db_column='ID_FUNCIONARIO')
    cpf = models.CharField(max_length=11, db_column='DS_CPF')
    nome = models.CharField(max_length=100, db_column='DS_NOME')
    sexo = models.CharField(max_length=10, db_column='DS_SEXO')
    data_nascimento = models.DateTimeField(db_column='DT_NASCIMENTO')
    logradouro = models.CharField(max_length=100, db_column='DS_ENDERECO_LOGRADOURO')
    numero = models.IntegerField(db_column='NR_ENDERECO_NUMERO')
    bairro = models.CharField(max_length=40, db_column='DS_ENDERECO_BAIRRO')
    cidade = models.CharField(max_length=80, db_column='DS_ENDERECO_CIDADE')
    estado = models.CharField(max_length=40, db_column='DS_ENDERECO_ESTADO')
    cep = models.IntegerField(db_column='NR_ENDERECO_CEP')
    telefone = models.CharField(max_length=14, db_column='DS_TELEFONE')
    empresa = models.ForeignKey('Empresa', db_column='ID_EMPRESA', on_delete='CASCADE')

    def __str__(self):
        return self.nome

class TipoBeneficio(models.Model):

    class Meta:
        db_table='TB_TIPO_BENEFICIO'

    id_tipo_beneficio = models.IntegerField(primary_key=True, db_column='ID_TIPO_BENEFICIO')
    descricao = models.CharField(max_length=100, db_column='DS_TIPO_BENEFICIO')

    def __str__(self):
        return self.descricao

class Beneficio(models.Model):

    class Meta:
        db_table='TB_BENEFICIO'

    id_beneficio = models.IntegerField(primary_key=True, db_column='ID_BENEFICIO')
    numero_cartao = models.BigIntegerField(db_column='NR_CARTAO')
    saldo = models.DecimalField(max_digits=18, decimal_places=2, db_column='VL_SALDO')
    empresa = models.ForeignKey('Empresa', db_column='ID_EMPRESA', on_delete='CASCADE')
    funcionario = models.ForeignKey('Funcionario', db_column='ID_FUNCIONARIO', on_delete='CASCADE')
    tipo_beneficio = models.ForeignKey('TipoBeneficio', db_column='ID_TIPO_BENEFICIO', on_delete='CASCADE')

    def __str__(self):
        return self.numero_cartao
