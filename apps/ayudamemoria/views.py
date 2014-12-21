# Create your views here.

import random

def GetRandomPhrases(n):

    allphrases = MemoryPhrase_Answer.objects.all()
    auxlst = range(len(allphrases))
    random.shuffle(auxlst)

    return [allphrases[i] for i in auxlst[:n]]



