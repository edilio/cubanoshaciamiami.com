from django.contrib import admin

from .models import Menu, Service, Sitio
from .models import Poll, Choice, Category, Article


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Indice',               {'fields': ['indice']}),
        (None,               {'fields': ['question']}),
        ('Information de Fecha', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Menu)
admin.site.register(Service)
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
admin.site.register(Sitio)
admin.site.register(Article)
admin.site.register(Category)
