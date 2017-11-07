from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'

class Usuarios(models.Model):
    nome = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)

class Categorias(models.Model):
    nome = models.CharField(max_length=255)
    
class Notas(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    nota = models.CharField(max_length=3000)

class CategoriaNotas(models.Model):
    categorias_id = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    notas_id = models.ForeignKey(Notas, on_delete=models.CASCADE)

class Email(models.Model):
    enderecoEmail = models.CharField(max_length=255)
    usuarios_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
