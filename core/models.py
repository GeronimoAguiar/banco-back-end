from django.db import models

class Conta(models.Model):
    titular = models.CharField(max_length=150)
    conta = models.CharField(primary_key=True, max_length=10)
    tipo = models.CharField(max_length=15)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    limite = models.DecimalField(max_digits=10, decimal_places=2)
    fatura = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.conta
