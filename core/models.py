from django.db import models

class Conta(models.Model):
    titular = models.CharField(max_length=150)
    conta = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=15)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    limite = models.DecimalField(max_digits=10, decimal_places=2)
    fatura = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField()


    def __str__(self):
        return self.titular
