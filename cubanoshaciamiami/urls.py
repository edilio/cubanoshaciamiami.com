from django.conf.urls import *
from django.http import HttpResponse
from django.contrib import admin

from apps.services.views import *
from apps.presupuesto.views import showpresupuesto


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', inicial),
    url(r'^informacion/$', informacion, name='information'),
    url(r'^informacion/estabilidad/$', estabilidad, name='estabilidad'),
    url(r'^informacion/estabilidad/([A-Za-z 0-9\-]+)/$', unaestabilidad, name='estabilidad-detail'),
    url(r'^informacion/adaptaciones/$', adapt, name='adapt'),
    url(r'^informacion/adaptaciones/([A-Za-z 0-9\-]+)/$', unaadaptacion, name='adapt-detail'),
    url(r'^contactanos/', contactus, name='contactus'),
    url(r'^contactenos/', contactus),
    url(r'^encuestas/$', todas_encuestas),
    url(r'^encuestas/([0-9]+)/$', detalleencuestas, name='poll-detail'),
    url(r'^encuestas/([0-9]+)/opcion/([0-9]+)/up$', incrementachoice),
    url(r'^encuestas/([0-9]+)/opcion/([0-9]+)/down$', decrementachoice),
    url(r'^encuestas/([0-9]+)/agregaropcion/$', agregarchoice),
    url(r'^encuestas/agregar/$', agregarencuesta),
    url(r'^sitios-cubanos/$', sitioscubanos, name='cuban-sites'),
    url(r'^sitios-cubanos/agregar/$', agregarsitio, name='add-cuban-site'),
    url(r'^sugerencias/', sugerencias),
    url(r'^mision/', mission),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tellafriend/', tellafriendview),
    url(r'^tellit/', tellit),
    url(r'^presupuesto/', showpresupuesto),
    url(r'^pasaporte/', pasaporte),
    url(r'^processpasaporte/', processpasaporte),
    url(r'^extjs/', ext),
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain"))

)
