from django.conf.urls.defaults import *
from django.http import HttpResponse
from cubanoshaciamiami.services.views import contactus, mission, todas_encuestas, detalleencuestas
from cubanoshaciamiami.services.views import inicial, informacion, tellafriendview, tellit, nodonealready
from services.views import estabilidad, unaestabilidad, adaptaciones, unaadaptacion
from services.views import incrementachoice, decrementachoice, agregarchoice, agregarencuesta
from services.views import sugerencias, sitioscubanos, agregarsitio
from services.views import pasaporte
from services.views import processpasaporte, ext

from presupuesto.views import showpresupuesto

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$',inicial),
    (r'^informacion/$', informacion),
    (r'^informacion/estabilidad/$', estabilidad),
    (r'^informacion/estabilidad/([A-Za-z 0-9\-]+)/$', unaestabilidad),
    (r'^informacion/adaptaciones/$', adaptaciones),
    (r'^informacion/adaptaciones/([A-Za-z 0-9\-]+)/$', unaadaptacion),
    (r'^contactanos/', contactus),
    (r'^contactenos/', contactus),
    (r'^encuestas/$', todas_encuestas),
    (r'^encuestas/([0-9]+)/$', detalleencuestas),
    (r'^encuestas/([0-9]+)/opcion/([0-9]+)/up$', incrementachoice),
    (r'^encuestas/([0-9]+)/opcion/([0-9]+)/down$', decrementachoice),
    (r'^encuestas/([0-9]+)/agregaropcion/$', agregarchoice),
    (r'^encuestas/agregar/$', agregarencuesta),
    (r'^sitioscubanos/$', sitioscubanos),
    (r'^sitioscubanos/agregar/$', agregarsitio),
    (r'^sugerencias/', sugerencias),
    (r'^mision/', mission),
    url(r'^admin/', include(admin.site.urls)),
    (r'^tellafriend/', tellafriendview),
    (r'^tellit/', tellit),
    (r'^presupuesto/', showpresupuesto),
    (r'^pasaporte/', pasaporte),
    (r'^processpasaporte/', processpasaporte),
    (r'^extjs/', ext),
    (r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain"))

)
