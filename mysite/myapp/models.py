from django.db import models
from django.utils import timezone
from .functions import validate_file_extension


class UploadForm(models.Model):
    data = models.DateTimeField(default=timezone.now())
    arquivo = models.FileField(upload_to="media", validators=[validate_file_extension])

    class Meta:
        ordering = ['data']

    def __str__(self):
        return f"{self.arquivo}"


class TransacoesImportacao(models.Model):
    Tipo = models.CharField(max_length=1)
    Data = models.CharField(max_length=8)
    Valor = models.CharField(max_length=10)
    CPF = models.CharField(max_length=11)
    Cartao = models.CharField(max_length=12)
    Hora = models.CharField(max_length=6)
    Dono_da_Loja = models.CharField(max_length=14)
    Nome_da_loja = models.CharField(max_length=19)

    class Meta:
        ordering = ['Tipo']

    def __str__(self):
        return f"{self.Tipo}"


class TipoTransacoesEntity(models.Model):
    Descricao = models.CharField(max_length=100)
    Natureza = models.CharField(max_length=50)
    Sinal = models.CharField(max_length=1)

    def __str__(self):
        return "%s %s" % (self.Descricao, self.Natureza)


class TransacoesEntity(models.Model):
    Tipo = models.ForeignKey(TipoTransacoesEntity, on_delete=models.CASCADE)
    Data = models.DateField()
    Valor = models.CharField(max_length=10)
    CPF = models.CharField(max_length=11)
    Cartao = models.CharField(max_length=12)
    Hora = models.TimeField()
    Dono_da_Loja = models.CharField(max_length=14)
    Nome_da_loja = models.CharField(max_length=19)
    Total = models.FloatField(default=0)


def Total(self):
    self.Total = + self.Valor + 1
    return self.Total


'''def __str__(self):
    return "%s %s %s %s" % (self.Tipo, self.Data, self.Valor, self.Total)'''
