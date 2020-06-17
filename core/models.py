from django.db import models

class Person(models.Model):
    first_name = models.CharField('Nome', max_length=100)
    last_name = models.CharField('Sobrenome', max_length=100)

    def __str__(self):
        return self.first_name

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=200)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f'{self.quantidade} - {self.produto}'
