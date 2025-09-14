from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_lancamento = models.DateField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    diretor = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo
