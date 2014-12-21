# Create your views here.

import datetime
from subprocess import call
import os

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.files import File
from django.conf import settings

from .models import Menu, Service, Poll, Choice, Sitio
from .sendmail import tellafriend
from lib.arreglaacentos import arreglalosacentos


content_path = os.path.join(settings.BASE_DIR, "apps/services/templates/")
services_templates_path = os.path.join(settings.BASE_DIR, "apps/services/templates/services/")
adaptaciones_templates_path = os.path.join(settings.BASE_DIR, "apps/services/templates/adaptacion/")
estabilidad_templates_path = os.path.join(settings.BASE_DIR, "apps/services/templates/estabilidad/")


def print_menus():
    s = ""
    for m in Menu.objects.all():
        s += ('<a href="%s" title="%s">%s</a><br/>' % (m.href, m.name, m.name))
    return s


def show_content(content_filename):
    menus = Menu.objects.all()
    try:
        return render_to_response(content_filename, {'Menus': menus})
    except:
        arreglalosacentos(content_filename)
        return render_to_response(content_filename, {'Menus': menus})


def nodonealready(request):
    return show_content("nodonealready.html")

def tellafriendview(request):
    return show_content("tellafriend.html")


def get_adaptaciones():
    dirs = os.listdir(adaptaciones_templates_path)
    dir_list = []
    i = 0
    for f in dirs:
        if f[-4:] != '.bak':
            filename = f[:f.find(".")]
            truefilename = filename[filename.find("-") + 1:]
            service = Service(href="/informacion/adaptaciones/" + filename, name=truefilename, index=i)
            service.name = service.spanishname()
            i += 1
            dir_list.append(service)
    return dir_list


def adapt(request):
    return render_to_response('services.html', {'Menus': Menu.objects.order_by("index"),
                                                'Services_list': get_adaptaciones()})

def unaadaptacion(request, filename):
    return show_content(filename + ".html")


def getestabilidad():
    dirs = os.listdir(estabilidad_templates_path)
    dir_list = []
    i = 0
    for f in dirs:
        if f[-4:] != '.bak':
            filename = f[:f.find(".")]
            service = Service(href="/informacion/estabilidad/" + filename, name=filename,  index=i)
            i += 1
            dir_list.append(service)
    return dir_list


def estabilidad(request):
    return render_to_response('services.html', {'Menus': Menu.objects.order_by("index"),
                                                'Services_list': getestabilidad()})

def unaestabilidad(request, filename):
    return show_content(filename + ".html")


def contactus(request):
    return show_content("contactus.html")


def inicial(request):
    return show_content("inicial.html")


def mission(request):
    return show_content("mission.html")


def informacion(request):
    return show_content("informacion.html")


def virusremoval(request):
    return show_content(services_templates_path + "virusremoval.html")


def sitioscubanos(request):
    filename = content_path + "Sitios Cubanos.html"
    return render_to_response(filename, {'Menus': Menu.objects.all(),
                                         'Sitios': Sitio.objects.order_by("index")})

def agregarsitio(request):
    try:
        sitiostr = request.POST['otrositio']
        namestr = sitiostr
        if sitiostr:
            if (sitiostr[:7].upper() == 'HTTP://'):
                namestr = sitiostr[7:]
            else:
                namestr = sitiostr
                sitiostr = 'HTTP://' + namestr
            sitio = Sitio(name=namestr, href=sitiostr,  index=proximositio())
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

        return show_content("tellitsuccess.html")
    except Exception, e:
        return render_to_response("telliterror.html", {'Menus': Menu.objects.order_by("index"),
                                                       'ErrorMessage': e.message })


def proximaencuesta():
    ultima = Poll.objects.all().order_by("-indice")[:1]
    return ultima[0].indice + 1


def proximositio():
    ultimo = Sitio.objects.all().order_by("-index")[:1]
    return ultimo[0].index + 1


def todas_encuestas(request):
    latest_poll_list = [poll for poll in Poll.objects.all().order_by('-pub_date')[:15] if poll.id != 1]
    return render_to_response('encuestas.html', {'Menus': Menu.objects.order_by("index"),
                                                 'latest_poll_list': latest_poll_list})


def cmpchoices(ch1,ch2):
    if ch1.votes < ch2.votes:
        return 1
    elif ch1.votes > ch2.votes:
        return -1
    else:
        return 0


def detalleencuestas(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    choices = [ choice for choice in p.choice_set.all() if choice.poll.id == p.id]

    choices.sort(cmpchoices)
    return render_to_response('encuestadetalles.html', {'Menus': Menu.objects.order_by("index"),
                                                        'poll': p, 'choices': choices})


def incrementachoice(request,poll_id,choice):
    p = get_object_or_404(Choice, pk=choice)
    p.votes += 1
    p.save()
    return HttpResponseRedirect(reverse('poll-detail', args=(poll_id,)))


def decrementachoice(request,poll_id,choice):
    p = get_object_or_404(Choice, pk=choice)
    p.votes -= 1
    p.save()
    return HttpResponseRedirect(reverse('poll-detail', args=(poll_id,)))


def agregarchoice(request,poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        choice_str = request.POST.get('otherchoice')
        if choice_str:
            choice = Choice(poll=p, choice=choice_str,  votes=1)
            choice.save()
    finally:
        pass
    return HttpResponseRedirect(reverse('poll-detail', args=(poll_id,)))


def agregarencuesta(request):
    try:
        encuesta_str = request.POST.get('encuestanueva')
        if encuesta_str:
            p = Poll(indice=proximaencuesta(),
                question=encuesta_str,
                pub_date=datetime.datetime.now())
            p.save()
    finally:
        pass
    return HttpResponseRedirect('/encuestas')


def sugerencias(request):
    return HttpResponseRedirect(reverse('poll-detail', args=(1,)))


def Salario(horas_regulares, taxes_horas_regulares, rate_horas_regulares):
    return (horas_regulares * rate_horas_regulares)-(horas_regulares * rate_horas_regulares * float(taxes_horas_regulares))


def Desglose(horas_regulares, taxes_horas_regulares, rate_horas_regulares):
    bruto = horas_regulares * rate_horas_regulares
    taxes = (horas_regulares * rate_horas_regulares * float(taxes_horas_regulares))
    neto = bruto - taxes
    return (bruto,taxes,neto)


def taxes(request):
    hr = float(request.POST.get('hr', '40'))
    thr = float(request.POST.get('thr', '0.12'))
    rhr = request.POST.get('rhr', '10')
    return Desglose(hr, thr, rhr)


def ext(request):
    return show_content('ext.html')


def pasaporte(request):
    return show_content('pasaporte.html')


def CreateStr(reqpost):
    s = ''
    for key in reqpost.keys():
        if (key.find('filename') == -1):
            s += '\n %s=%s' %(key,reqpost[key])
    return s[1:]


def GiveMeKey(fieldname, post):
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
