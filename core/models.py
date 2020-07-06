from django.db import models

class Person(models.Model):
    first_name = models.CharField('Nome', max_length=100)
    last_name = models.CharField('Sobrenome', max_length=100)

    class Meta:
        permissions = (
            ('ver_dashboard', 'Pode acessar tela Dashboard'),
        )

    def __str__(self):
        return self.first_name

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=200)
    possui_estoque = models.BooleanField('Tem no estoque', default=False)

    class Meta:
        permissions = (
            ('change_estoque', 'Alterar produto no estoque'),
        )

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f'{self.quantidade} - {self.produto}'
