from django.contrib import admin
from django.utils.translation import ugettext_lazy

from .models import (
    Cliente,
    Cargo,
    Compra,
    Contato,
    Estoque,
    Fornecedor,
    Funcionario,
    Operacao,
    Pedido,
    Produto,
    TipoContrato,
    TpProduto,
    Venda
)


class MarketfyAdmin(admin.AdminSite):
    site_title = ugettext_lazy('Marketfy')

    site_header = ugettext_lazy('Marketfy')

    index_title = ugettext_lazy('Marketfy')

marketfy_admin = MarketfyAdmin()

marketfy_admin.register(Cliente)
marketfy_admin.register(Cargo)
marketfy_admin.register(Compra)
marketfy_admin.register(Contato)
marketfy_admin.register(Estoque)
marketfy_admin.register(Fornecedor)
marketfy_admin.register(Funcionario)
marketfy_admin.register(Operacao)
marketfy_admin.register(Pedido)
marketfy_admin.register(Produto)
marketfy_admin.register(TipoContrato)
marketfy_admin.register(TpProduto)
marketfy_admin.register(Venda)
