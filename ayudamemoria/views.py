# Create your views here.

from django.template.loader import get_template
from django.template import Context, RequestContext

from django.http import HttpResponse
from django.shortcuts import render_to_response
from cubanoshaciamiami.ayudamemoria.models import Category, MemoryPhrase_Answer

import random

def GetRandomPhrases(n):

    allphrases = MemoryPhrase_Answer.objects.all()
    auxlst = range(len(allphrases))
    random.shuffle(auxlst)

    return [allphrases[i] for i in auxlst[:n]]



