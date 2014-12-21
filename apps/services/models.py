from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=30)
    href = models.CharField(max_length=200)
    index = models.IntegerField()

    class Meta:
        ordering = ['index']

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=130)
    href = models.CharField(max_length=200)
    index = models.IntegerField()

    def __str__(self):
        return self.name

    def spanishname(self):
        txta = self.name.replace("'a","&aacute;")
        txte = txta.replace("'e","&eacute;")
        txti = txte.replace("'i","&iacute;")
        txto = txti.replace("'o","&oacute;")
        txtu = txto.replace("'u","&uacute;")
        final = txtu.replace("'N","&Ntilde;").replace("'n", "&ntilde;")
        return final


class Sitio(Service):
    pass


class Poll(models.Model):
    indice = models.IntegerField()
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return unicode(self.question)

    def __unicode__(self):
        return unicode(self.question)


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __str__(self):
        return self.choice


class Category(models.Model):
    name = models.CharField(max_length=100)
    index = models.IntegerField()
    visits = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    index = models.IntegerField()
    visits = models.IntegerField()
    href = models.URLField()
    content = models.TextField()
    autor = models.CharField(max_length=50)
    pub_date = models.DateTimeField('dia publicado')
    mod_date = models.DateTimeField('dia modificado')

    def __str__(self):
        return self.name


class Pasaporte(models.Model):
    Prorroga = models.CharField(max_length=50, db_column=u'Prorroga', blank=True)
    Padre = models.CharField(max_length=50, db_column=u'Padre', blank=True)
    NivelCultural = models.CharField(max_length=50, db_column=u'NivelCultural', blank=True)
    PE3 = models.CharField(max_length=50, db_column=u'PE3', blank=True)
    Habilitacion = models.CharField(max_length=50, db_column=u'Habilitacion', blank=True)
    Femenino = models.CharField(max_length=50, db_column=u'Femenino', blank=True)
    Profesion = models.CharField(max_length=50, db_column=u'Profesion', blank=True)
    Canoso = models.CharField(max_length=50, db_column=u'Canoso', blank=True)
    DireccionRef1 = models.CharField(max_length=50, db_column=u'DireccionRef1', blank=True)
    Masculino = models.CharField(max_length=50, db_column=u'Masculino', blank=True)
    Hasta3 = models.CharField(max_length=50, db_column=u'Hasta3', blank=True)
    Negros = models.CharField(max_length=50, db_column=u'Negros', blank=True)
    PVE = models.CharField(max_length=50, db_column=u'PVE', blank=True)
    Desde2 = models.CharField(max_length=50, db_column=u'Desde2', blank=True)
    PaisActual = models.CharField(max_length=50, db_column=u'PaisActual', blank=True)
    Estado = models.CharField(max_length=50, db_column=u'Estado', blank=True)
    Otros = models.CharField(max_length=50, db_column=u'Otros', blank=True)
    Hasta1 = models.CharField(max_length=50, db_column=u'Hasta1', blank=True)
    CaracteristicasEspeciales = models.CharField(max_length=50, db_column=u'CaracteristicasEspeciales', blank=True)
    CNTomo = models.CharField(max_length=50, db_column=u'CNTomo', blank=True)
    CNRegistroCivil = models.CharField(max_length=50, db_column=u'CNRegistroCivil', blank=True)
    PSE = models.CharField(max_length=50, db_column=u'PSE', blank=True)
    PE6 = models.CharField(max_length=50, db_column=u'PE6', blank=True)
    PVLugar = models.CharField(max_length=50, db_column=u'PVLugar', blank=True)
    TrabajoDireccion = models.CharField(max_length=50, db_column=u'TrabajoDireccion', blank=True)
    Hasta2 = models.CharField(max_length=50, db_column=u'Hasta2', blank=True)
    Desde4 = models.CharField(max_length=50, db_column=u'Desde4', blank=True)
    AO = models.CharField(max_length=50, db_column=u'AO', blank=True)
    Desde5 = models.CharField(max_length=50, db_column=u'Desde5', blank=True)
    PVT = models.CharField(max_length=50, db_column=u'PVT', blank=True)
    Hasta5 = models.CharField(max_length=50, db_column=u'Hasta5', blank=True)
    FechaSolicitudMes = models.CharField(max_length=50, db_column=u'FechaSolicitudMes', blank=True)
    Direccion5Cuba = models.CharField(max_length=50, db_column=u'Direccion5Cuba', blank=True)
    PaisDeResidencia = models.CharField(max_length=50, db_column=u'PaisDeResidencia', blank=True)
    NombreReferenciaenCuba = models.CharField(max_length=50, db_column=u'NombreReferenciaenCuba', blank=True)
    Madre = models.CharField(max_length=50, db_column=u'Madre', blank=True)
    TrabajoTelefono = models.CharField(max_length=50, db_column=u'TrabajoTelefono', blank=True)
    Direccion3Cuba = models.CharField(max_length=50, db_column=u'Direccion3Cuba', blank=True)
    Pardos = models.CharField(max_length=50, db_column=u'Pardos', blank=True)
    Ocupacion2 = models.CharField(max_length=50, db_column=u'Ocupacion2', blank=True)
    PE11 = models.CharField(max_length=50, db_column=u'PE11', blank=True)
    DireccionActual = models.CharField(max_length=50, db_column=u'DireccionActual', blank=True)
    Hasta4 = models.CharField(max_length=50, db_column=u'Hasta4', blank=True)
    ZipActual = models.CharField(max_length=50, db_column=u'ZipActual', blank=True)
    PrimerNombre = models.CharField(max_length=50, db_column=u'PrimerNombre', blank=True)
    EmailActual = models.CharField(max_length=50, db_column=u'EmailActual', blank=True)
    LugarNacimientoPais = models.CharField(max_length=50, db_column=u'LugarNacimientoPais', blank=True)
    Amarilla = models.CharField(max_length=50, db_column=u'Amarilla', blank=True)
    Castanno = models.CharField(max_length=50, db_column=u'Castanno', blank=True)
    FechaSolicitudAnno = models.CharField(max_length=50, db_column=u'FechaSolicitudAnno', blank=True)
    Consulado = models.CharField(max_length=50, db_column=u'Consulado', blank=True)
    Claros = models.CharField(max_length=50, db_column=u'Claros', blank=True)
    SegundoApellido = models.CharField(max_length=50, db_column=u'SegundoApellido', blank=True)
    Ilegal = models.CharField(max_length=50, db_column=u'Ilegal', blank=True)
    FaxActual = models.CharField(max_length=50, db_column=u'FaxActual', blank=True)
    Renovacion = models.CharField(max_length=50, db_column=u'Renovacion', blank=True)
    PVNumero = models.CharField(max_length=50, db_column=u'PVNumero', blank=True)
    LugarActual = models.CharField(max_length=50, db_column=u'LugarActual', blank=True)
    Negra = models.CharField(max_length=50, db_column=u'Negra', blank=True)
    CCV = models.CharField(max_length=50, db_column=u'CCV', blank=True)
    LugarNacimientoProvincia = models.CharField(max_length=50, db_column=u'LugarNacimientoProvincia', blank=True)
    Direccion2Cuba = models.CharField(max_length=50, db_column=u'Direccion2Cuba', blank=True)
    Desde3 = models.CharField(max_length=50, db_column=u'Desde3', blank=True)
    Direccion4Cuba = models.CharField(max_length=50, db_column=u'Direccion4Cuba', blank=True)
    Rojo = models.CharField(max_length=50, db_column=u'Rojo', blank=True)
    CNFolio = models.CharField(max_length=50, db_column=u'CNFolio', blank=True)
    CentroTrabajo = models.CharField(max_length=50, db_column=u'CentroTrabajo', blank=True)
    Desde1 = models.CharField(max_length=50, db_column=u'Desde1', blank=True)
    PrimerApellido = models.CharField(max_length=50, db_column=u'PrimerApellido', blank=True)
    PE4 = models.CharField(max_length=50, db_column=u'PE4', blank=True)
    ValorTramite = models.CharField(max_length=50, db_column=u'ValorTramite', blank=True)
    SegundoNombre = models.CharField(max_length=50, db_column=u'SegundoNombre', blank=True)
    TelefonoActual = models.CharField(max_length=50, db_column=u'TelefonoActual', blank=True)
    TrabajoEmail = models.CharField(max_length=50, db_column=u'TrabajoEmail', blank=True)
    LugarNacimientoCiudad = models.CharField(max_length=50, db_column=u'LugarNacimientoCiudad', blank=True)
    TrabajoPais = models.CharField(max_length=50, db_column=u'TrabajoPais', blank=True)
    Mulata = models.CharField(max_length=50, db_column=u'Mulata', blank=True)
    PE1 = models.CharField(max_length=50, db_column=u'PE1', blank=True)
    Blanca = models.CharField(max_length=50, db_column=u'Blanca', blank=True)
    ViaTramite = models.CharField(max_length=50, db_column=u'ViaTramite', blank=True)
    FechadeNacimientoAnno = models.CharField(max_length=50, db_column=u'FechadeNacimientoAnno', blank=True)
    PVExpedicion = models.CharField(max_length=50, db_column=u'PVExpedicion', blank=True)
    FechadeNacimientoMes = models.CharField(max_length=50, db_column=u'FechadeNacimientoMes', blank=True)
    FechadeSalidaMes = models.CharField(max_length=50, db_column=u'FechadeSalidaMes', blank=True)
    Profesion2 = models.CharField(max_length=50, db_column=u'Profesion2', blank=True)
    Negro = models.CharField(max_length=50, db_column=u'Negro', blank=True)
    NoPasaporte = models.CharField(max_length=50, db_column=u'NoPasaporte', blank=True)
    Estatura = models.CharField(max_length=50, db_column=u'Estatura', blank=True)
    Direccion1Cuba = models.CharField(max_length=50, db_column=u'Direccion1Cuba', blank=True)
    Albina = models.CharField(max_length=50, db_column=u'Albina', blank=True)
    Ocupacion = models.CharField(max_length=50, db_column=u'Ocupacion', blank=True)
    DireccionRef2 = models.CharField(max_length=50, db_column=u'DireccionRef2', blank=True)
    FechadeSalidaDia = models.CharField(max_length=50, db_column=u'FechadeSalidaDia', blank=True)
    Rubio = models.CharField(max_length=50, db_column=u'Rubio', blank=True)
    TrabajoFax = models.CharField(max_length=50, db_column=u'TrabajoFax', blank=True)
    FechadeSalidaAnno = models.CharField(max_length=50, db_column=u'FechadeSalidaAnno', blank=True)
    FechaSolicitudDia = models.CharField(max_length=50, db_column=u'FechaSolicitudDia', blank=True)
    PRE_PSI = models.CharField(max_length=50, db_column=u'PRE_PSI', blank=True)
    TrabajoZip = models.CharField(max_length=50, db_column=u'TrabajoZip', blank=True)
    FechadeNacimientoDia = models.CharField(max_length=50, db_column=u'FechadeNacimientoDia', blank=True)
    TrabajoProvincia = models.CharField(max_length=50, db_column=u'TrabajoProvincia', blank=True)
    PrimeraVez = models.CharField(max_length=50, db_column=u'PrimeraVez', blank=True)
    pdf_filename = models.CharField(max_length=255, db_column=u'PDFFilenam', blank=True)

    def __str__(self):
        return self.PrimerNombre + ' ' + self.PrimerApellido
