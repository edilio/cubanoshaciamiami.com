from django.db import models

# Create your models here.

class TipoDeGasto(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PresupuestoDeGasto(models.Model):
    tipo_de_gasto = models.ForeignKey(TipoDeGasto)
    cantidad = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_de_gasto.name
