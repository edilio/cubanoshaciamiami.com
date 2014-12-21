from django.contrib import admin

from .models import TipoDeGasto, PresupuestoDeGasto

admin.site.register(TipoDeGasto)
admin.site.register(PresupuestoDeGasto)