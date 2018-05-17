# coding: utf-8--

from django.db import models

# Create your models here.


class Estabelecimento(models.Model):
    nome_estabelecimento = models.CharField(
        max_length=100, verbose_name="Nome do estabelecimento")
    endereco = models.CharField(
        max_length=100, verbose_name="Endereço do estabelecimento")

    class Meta:
        verbose_name_plural = "Estabelecimentos"
        ordering = ('nome_estabelecimento',)

    def __str__(self):
        return '{0}'.format(self.nome_estabelecimento)


class CategoriaProduto(models.Model):
    categoria = models.CharField(
        max_length=50, verbose_name="Categoria de produto")


class Produtos(models.Model):
    nome_produto = models.CharField(
        max_length=100, verbose_name="Nome do produto")
    descricao_produto = models.CharField(max_length=300,
                                         verbose_name="Descrição do produto")
    categoria = models.OneToOneField(CategoriaProduto,
                                     on_delete=models.CASCADE,
                                     primary_key=True,
                                     related_name='Categoria_Produto')
