import datetime

from django.db import models


class Fornecedor(models.Model):
    cnpj = models.IntegerField('CNPJ', primary_key=True)
    nome = models.CharField('Nome', max_length=50, null=False, blank=False)
    data_vinculo = models.DateField('Data do vínculo', null=False, blank=False)

    class Meta:
        db_table = 'fornecedor'
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return '{0} - {1}'.format(self.cnpj, self.nome)


class Cliente(models.Model):
    cpf = models.IntegerField('CPF', primary_key=True)
    nome = models.CharField('Nome', max_length=50, null=False, blank=False)
    data_vinculo = models.DateField('Data do vínculo', null=False, blank=False)

    class Meta:
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return '{0} - {1}'.format(self.cpf, self.nome)


class Cargo(models.Model):
    cod_cargo = models.IntegerField('Código de Cargo', primary_key=True)
    nome = models.CharField('Nome', max_length=30, null=False, blank=False)
    nv_cargo = models.IntegerField('Nível do Cargo', null=False, blank=False)

    class Meta:
        db_table = 'cargo'
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return '{0} - {1}'.format(self.cod_cargo, self.nome)


class TpProduto(models.Model):
    cod_tp_produto = models.IntegerField('Código do tipo do produto', primary_key=True)
    tipo = models.CharField('Tipo', max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'tp_produto'
        verbose_name = 'Tipo de Produto'
        verbose_name_plural = 'Tipos de Produtos'

    def __str__(self):
        return '{0} - {1}'.format(self.cod_tp_produto, self.tipo)


class Produto(models.Model):
    cod_produto = models.IntegerField('Código do produto', primary_key=True)
    descricao = models.CharField('Descrição', max_length=50, null=False, blank=False)
    cod_tp_produto = models.ForeignKey(TpProduto)
    data_validade = models.DateField('Data de validade', null=False, blank=False)
    valor = models.FloatField('Valor', null=False, blank=False)
    marca = models.CharField('Marca', max_length=20, null=False, blank=False)
    num_lote = models.IntegerField('Número do lote', null=False, blank=False)


    class Meta:
        db_table = 'produto'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return '{0} - {1}'.format(self.cod_produto, self.descricao)


class Estoque(models.Model):
    cod_estoque = models.IntegerField('Código do estoque', primary_key=True)
    quantidade = models.IntegerField('Quantidade', null=False, blank=False)
    dt_atu = models.DateField('Data de atualização', null=False, blank=False)
    cod_produto = models.ForeignKey(Produto)


    class Meta:
        db_table = 'estoque'
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoques'

    def __str__(self):
        return '{0} - {1}'.format(self.cod_estoque, self.cod_produto.descricao)


class TipoContrato(models.Model):
    cod_tp_contrato = models.IntegerField('Código do tipo de contrato', primary_key=True)
    tipo = models.CharField('Tipo', max_length=20, null=False, blank=False)

    class Meta:
        db_table = 'tipo_contrato'
        verbose_name = 'Tipo de Contrato'
        verbose_name_plural = 'Tipos de Contratos'

    def __str__(self):
        return '{0} - {1}'.format(self.cod_tp_contrato, self.tipo)


class Funcionario(models.Model):
    cod_funcionario = models.IntegerField('Código do funcionario', primary_key=True)
    cpf = models.IntegerField('CPF', null=False, blank=False)
    nome = models.CharField('Nome', max_length=20, null=False, blank=False)
    dt_inicio = models.DateField('Data de início', null=False, blank=False)
    dt_fim = models.DateField('Data de fim', null=True)
    cod_cargo = models.ForeignKey(Cargo)
    cod_tp_cargo = models.ForeignKey(TipoContrato)
    salario = models.IntegerField('Salário', null=False, blank=False)


    class Meta:
        db_table = 'funcionario'
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    def __str__(self):
        return '{0} - {1}'.format(self.cod_funcionario, self.nome)


class Contato(models.Model):
    cod_contato = models.IntegerField('Código do contato', primary_key=True)
    cpf_cnpj = models.ForeignKey(Cliente)
    telefone = models.IntegerField('Telefone', null=False, blank=False)
    email = models.CharField('Email', max_length=20, null=False, blank=False)


    class Meta:
        db_table = 'contato'
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return '{0} - {1}'.format(self.cod_contato, self.cpf_cnpj.nome)


class Operacao(models.Model):
    cod_oper = models.IntegerField('Código da operação', primary_key=True)
    cod_prod = models.ForeignKey(Produto)
    dt_oper = models.DateField('Data da operação', null=False, blank=False)
    valor = models.IntegerField('Valor', null=False, blank=False)
    quantidade = models.IntegerField('Quantidade', null=False, blank=False)
    cod_funcionario = models.ForeignKey(Funcionario)


    class Meta:
        db_table = 'operacao'
        verbose_name = 'Operação'
        verbose_name_plural = 'Operações'

    def __str__(self):
        return '{0} - {1}'.format(self.cod_oper, self.cod_prod.descricao)


class Compra(models.Model):
    cod_compra = models.IntegerField('Código da compra', primary_key=True)
    cod_oper = models.ForeignKey(Operacao)
    fornecedor_cnpj = models.ForeignKey(Fornecedor)


    class Meta:
        db_table = 'compra'
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

    def __str__(self):
        return '{0} - {1}'.format(self.cod_compra, self.cod_oper.cod_oper)


class Pedido(models.Model):
    cod_pedido = models.IntegerField('Código da pedido', primary_key=True)
    cliente_cpf = models.ForeignKey(Cliente)


    class Meta:
        db_table = 'pedido'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return '{0} - {1}'.format(self.cod_pedido, self.cliente_cpf.nome)


class Venda(models.Model):
    cod_venda = models.IntegerField('Código da venda', primary_key=True)
    cod_oper = models.ForeignKey(Operacao)
    cod_pedido = models.ForeignKey(Pedido)


    class Meta:
        db_table = 'venda'
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return '{0} - {1}'.format(self.cod_venda, self.cod_pedido.cod_pedido)