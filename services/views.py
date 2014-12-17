# Create your views here.
from django.template.loader import get_template
from django.template import Context, RequestContext
import django_monetize

from django.http import HttpResponse
from django.shortcuts import render_to_response
from cubanoshaciamiami.services.models import Menu, Service, Poll, Choice, Sitio
from cubanoshaciamiami.services.sendmail import tellafriend
from cubanoshaciamiami.arreglaacentos import arreglalosacentos
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime
from django.core.files.storage import default_storage
from django.core.files import File
from subprocess import call
import os


content_path = "/var/www/html/websites/cubanoshaciamiami/templates/"
services_templates_path = "/var/www/html/websites/cubanoshaciamiami/templates/services/"
adaptaciones_templates_path = "/var/www/html/websites/cubanoshaciamiami/templates/adaptacion/"
estabilidad_templates_path = "/var/www/html/websites/cubanoshaciamiami/templates/estabilidad/"

def PrintMenues():
    s = ""
    for m in Menu.objects.order_by("index"):
        s +=('<a href="%s" title="%s">%s</a><br/>' %(m.href,m.name,m.name))
    return s


def showcontent(content_filename):
    try:
        return render_to_response(content_filename, {'Menues':Menu.objects.order_by("index")})
    except:
        arreglalosacentos(content_filename)
        return render_to_response(content_filename, {'Menues':Menu.objects.order_by("index")})


def nodonealready(request):
    return showcontent("nodonealready.html")

def tellafriendview(request):
    return showcontent("tellafriend.html")

def getadaptaciones():
    import os
    dirs = os.listdir(adaptaciones_templates_path)
    dir_list = []
    i = 0
    for file in dirs:
        if file[-4:] <> '.bak':
            filename = file[:file.find(".")]
            truefilename = filename[filename.find("-")+1:]
            service = Service(href="/informacion/adaptaciones/"+filename,name=truefilename,index=i)
            service.name = service.spanishname()
            i += 1
            dir_list.append(service)
    return dir_list

##def getadaptaciones():
##    import os
##
##    Adap =  Article.objects.all().order_by("index")
##    i = 0
##    for file in dirs:
##        filename = file[:file.find(".")]
##        truefilename = filename[filename.find("-")+1:]
##        service = Service(href="/informacion/adaptaciones/"+filename,name=truefilename,index=i)
##        service.name = service.spanishname()
##        i += 1
##        dir_list.append(service)
##    return dir_list

def adaptaciones(request,filename=""):
    if (filename == None) or (filename == ""):
        return render_to_response('services.html', {'Menues':Menu.objects.order_by("index"), 'Services_list': getadaptaciones()})
    else:
        return showcontent(filename+".html")

def unaadaptacion(request,filename):
    return showcontent(filename+".html")

def getestabilidad():
    import os
    dirs = os.listdir(estabilidad_templates_path)
    dir_list = []
    i = 0
    for file in dirs:
        if file[-4:] <> '.bak':
            filename = file[:file.find(".")]
            service = Service(href="/informacion/estabilidad/"+filename,name=filename,index=i)
            i += 1
            dir_list.append(service)
    return dir_list

def estabilidad(request,filename=""):
    if (filename == None) or (filename == ""):
        return render_to_response('services.html', {'Menues':Menu.objects.order_by("index"), 'Services_list': getestabilidad()})
    else:
        return showcontent(filename+".html")

def unaestabilidad(request,filename):
    return showcontent(filename+".html")

def contactus(request):
    return showcontent("contactus.html")

def inicial(request):
    return showcontent("inicial.html")

def mission(request):
    return showcontent("mission.html")

def  informacion(request):
    return showcontent("informacion.html")

def virusremoval(request):
    return showcontent(services_templates_path +"virusremoval.html")

def sitioscubanos(request):
    filename = content_path +"Sitios Cubanos.html"
    return render_to_response(filename, {'Menues':Menu.objects.order_by("index"), 'Sitios':Sitio.objects.order_by("index")})

def agregarsitio(request):
    try:
        sitiostr = request.POST['otrositio']
        namestr = sitiostr
        if (sitiostr <> "") and (sitiostr <> None):
            if (sitiostr[:7].upper() == 'HTTP://'):
                namestr = sitiostr[7:]
            else:
                namestr = sitiostr
                sitiostr = 'HTTP://' + namestr
            sitio = Sitio(name = namestr, href = sitiostr,  index = proximositio())
            sitio.save()
    finally:
        pass
    return HttpResponseRedirect('/sitioscubanos/')


def tellit(request):
    try:
        friendname = request.POST['friendName']
        friendmail = request.POST['email']
        myname = request.POST['senderName']
        mymail = request.POST['senderEmail']
        msg  = request.POST['message']
        try:
            copy = (request.POST['sendCopy'] == "yes")
        except:
            copy = False

        tellafriend(friendname,friendmail,myname,mymail,msg,copy)

        return showcontent("tellitsuccess.html")
    except Exception, e:
        return render_to_response("telliterror.html", {'Menues':Menu.objects.order_by("index"), 'ErrorMessage' : e.message })

def proximaencuesta():
    ultima = Poll.objects.all().order_by("-indice")[:1]
    return ultima[0].indice + 1

def proximositio():
    ultimo = Sitio.objects.all().order_by("-index")[:1]
    return ultimo[0].index + 1

def todas_encuestas(request):
    latest_poll_list = [poll for poll in Poll.objects.all().order_by('-pub_date')[:15] if poll.id<>1]
    return render_to_response('encuestas.html', {'Menues':Menu.objects.order_by("index"), 'latest_poll_list' : latest_poll_list })

def cmpchoices(ch1,ch2):
    if ch1.votes < ch2.votes:
        return 1
    elif ch1.votes > ch2.votes:
        return -1
    else:
        return 0

def detalleencuestas(request,poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    choices = [ choice for choice in p.choice_set.all() if choice.poll.id == p.id]

    choices.sort(cmpchoices)
    return render_to_response('encuestadetalles.html', {'Menues':Menu.objects.order_by("index"), 'poll': p, 'choices' : choices})

def incrementachoice(request,poll_id,choice):
    p = get_object_or_404(Choice, pk=choice)
    p.votes += 1
    p.save()
    return HttpResponseRedirect(reverse('cubanoshaciamiami.services.views.detalleencuestas', args=(poll_id,)))


def decrementachoice(request,poll_id,choice):
    p = get_object_or_404(Choice, pk=choice)
    p.votes -= 1
    p.save()
    return HttpResponseRedirect(reverse('cubanoshaciamiami.services.views.detalleencuestas', args=(poll_id,)))

def agregarchoice(request,poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        choicestr = request.POST['otherchoice']
        if (choicestr <> "") and (choicestr <> None):
            choice = Choice(poll = p, choice = choicestr,  votes = 1)
            choice.save()
    finally:
        pass
    return HttpResponseRedirect(reverse('cubanoshaciamiami.services.views.detalleencuestas', args=(poll_id,)))

def agregarencuesta(request):
    try:
        encuestastr = request.POST['encuestanueva']
        if (encuestastr <> "") and (encuestastr <> None):
            p = Poll(indice = proximaencuesta(),
                question = encuestastr,
                pub_date = datetime.datetime.now())
            p.save()
    finally:
        pass
    return HttpResponseRedirect('/encuestas')


def sugerencias(request):
    return HttpResponseRedirect(reverse('cubanoshaciamiami.services.views.detalleencuestas', args=(1,)))


def Salario(horas_regulares,taxes_horas_regulares,rate_horas_regulares):
    return (horas_regulares * rate_horas_regulares)-(horas_regulares * rate_horas_regulares * float(taxes_horas_regulares))

def Desglose(horas_regulares,taxes_horas_regulares,rate_horas_regulares):
    bruto = horas_regulares * rate_horas_regulares
    taxes = (horas_regulares * rate_horas_regulares * float(taxes_horas_regulares))
    neto = bruto - taxes
    return (bruto,taxes,neto)

def taxes(request):
    try:
        hrstr = request.POST['hr']
        if (hrstr <> "") and (hrstr <> None):
            hr = float(hrstr)
        else:
            hr = 40
        thrstr = request.POST['thr']
        if (thrstr <> "") and (hrstr <> None):
            thr = float(hrstr)
        else:
            thr = 0.12
        hrstr = request.POST['rhr']
        if (rhrstr <> "") and (hrstr <> None):
            rhr = float(hrstr)
        else:
            rhr = 10
        rslt = Desglose(hr,thr,rhr)
    finally:
        pass
    return

def ext(request):
    return showcontent('ext.html')

def pasaporte(request):
    return showcontent('pasaporte.html')

def CreateStr(reqpost):
    s = ''
    for key in reqpost.keys():
        if (key.find('filename') == -1):
            s += '\n %s=%s' %(key,reqpost[key])
    return s[1:]

def GiveMeKey(fieldname,post):
    for key in post.keys():
        if fieldname == key:
            return key
    return fieldname


def processpasaporte(request):
    data = request.POST
    primernombre = GiveMeKey('PrimerNombre',data)
    primerapellido = GiveMeKey('PrimerApellido',data)
    filename = 'c:/windows/temp/temp%s.txt' % (data['pdfFileName'])
    pdffile = 'C:\\AppServ\\www\\wmedia\\pdfs\\pasaporte%s.pdf' % (data['pdfFileName'])

    if os.path.isfile(pdffile):
        os.remove(pdffile)

    f = open(filename,'w')
    myfile = File(f)

    S = CreateStr(data)
    S += '\n %s=%s' %('pdf_filename',pdffile)
    myfile.write(S)
    f.close()

    call('c:/windows/temp/CreatePdf.exe ' + filename + ' 1')
    return HttpResponseRedirect('/wmedia/pdfs/pasaporte%s.pdf' % (data['pdfFileName']))
