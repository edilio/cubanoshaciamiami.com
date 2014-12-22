from os import listdir, path

from cubanoshaciamiami.settings import TEMPLATE_DIRS


def getfilepath(filename):
    for folder in TEMPLATE_DIRS:
        if filename in listdir(folder):
##            print folder
            return folder
    return TEMPLATE_DIRS[2]

def arreglalosacentos(filename):
    filepath = getfilepath(filename)
##    print "fullname: %s" %filepath+filename
    f = open(path.join(filepath, filename))
    text = f.read()
    f.close()
    txta = text.replace("\xe1","&aacute;")
    txte = txta.replace("\xe9","&eacute;")
    txti = txte.replace("\xed","&iacute;")
    txto = txti.replace("\xf3","&oacute;")
    txtu = txto.replace("\xfa","&uacute;")
    final = txtu.replace('\xc3\x91',"&Ntilde;").replace('\xc3\xb1',"&ntilde;") #nn
    final = txtu.replace('\x1DA\x1DD',"&ntilde;")
    final = txtu.replace("'n","&ntilde;")
    f = open(filename,"w")
    f.write(final)
    f.close()

#filename = raw_input("Entre el fichero que va a corregir")
#arreglalosacentos(filename)