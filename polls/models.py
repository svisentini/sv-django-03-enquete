import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    #
    def __str__(self):
        return self.question_text
    #
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #
    def __str__(self):
        return self.choice_text

# ===================================================================================
# Teste para o catalogo

class TipoJoia(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Joia(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    descricao = models.TextField()
    preco_compra = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField()
    foto = models.ImageField(upload_to='joias/', blank=True, null=True)
    tipo = models.ForeignKey(TipoJoia, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"
