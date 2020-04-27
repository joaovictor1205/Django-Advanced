from django.db import models

class Person(models.Model):
    first_name = models.CharField('Nome', max_length=100)
    last_name = models.CharField('Sobrenome', max_length=100)

    def __str__(self):
        return self.first_name
