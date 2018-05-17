from django.contrib import admin
from cadastros.models import Estabelecimento, CategoriaProduto, Produtos

# Register your models here.
admin.site.register(Estabelecimento)
admin.site.register(CategoriaProduto)
admin.site.register(Produtos)
