# Create your views here.


from django.template.loader import get_template
from django.template import Context, RequestContext

from django.http import HttpResponse
from django.shortcuts import render_to_response

from cubanoshaciamiami.services.models import Menu
from cubanoshaciamiami.presupuesto.models import PresupuestoDeGasto, TipoDeGasto

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


content_path = "C:/Projects/cubanoshaciamiami/templates/"
presupuesto_templates_path = "C:/Projects/cubanoshaciamiami/templates/presupuesto/"

def PrintMenues():
    s = ""
    for m in Menu.objects.order_by("index"):
        s +=('<a href="%s" title="%s">%s</a><br/>' %(m.href,m.name,m.name))
    return s


def showpresupuesto(request):
    try:
        Presupuesto = PresupuestoDeGasto.objects.all()
        total = sum([eval(p.cantidad) for p in Presupuesto])
    except:
        Presupuesto = PresupuestoDeGasto()
        total = 0

    return render_to_response("presupuesto.html", {'Menues':Menu.objects.order_by("index"), 'Presupuesto':Presupuesto, 'total':total})




