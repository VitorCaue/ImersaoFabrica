from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

class Compra(models.Model):
    peca = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)

class Compra1(models.Model):
    peca = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)

class Compra2(models.Model):
    peca = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)

class Compra3(models.Model):
    peca = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)