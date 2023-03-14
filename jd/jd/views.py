from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader

# def saludar(request):
#   doc_externo=open("C:/Users/user/Desktop/django/jd/jd/plantillas/cabecera.html")
#    plt=Template(doc_externo.read())
#    doc_externo.close()
#    cxt=Context()
#    documento=plt.render(cxt)
#    return HttpResponse(documento)

def fecha(request):
    fechaActual=datetime.datetime.now()
    documento="""<HTML>
                      <HEAD>
                            <TITLE> Estuctura basica</TITLE>
                      </HEAD>
                      <BODY>
                           <H1>actualiso esta vista facha %s</H1> 
                      </BODY>
                 </HTML>""" %fechaActual
    return HttpResponse(documento)

def calculo(request, fechaNacimiento, fechaFutura):
    agnoActual=datetime.datetime.now().year
    edadActual=agnoActual-fechaNacimiento
    edadFutura=fechaFutura-fechaNacimiento

    FechaActual=datetime.datetime.now()

    doc_externo=open("C:/Users/user/Desktop/django/jd/jd/plantillas/cabecera.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    cxt=Context({"agnoActual":agnoActual,
                 "AgnoDeNacimiento":fechaNacimiento,
                 "edad": edadActual,
                 "edadFutura": edadFutura,
                 "FechaActual": FechaActual})
    

    documento=plt.render(cxt)

    return HttpResponse(documento)
    
def tareasEnlista(request):
    Tareas=["Aprender sobre internet", "Aprender HTML", "Aprender css", "Practicar python", "Aprender Django", "Construir mi propio sitio Wed"]
    #doc_externo=open("C:/Users/user/Desktop/django/jd/jd/plantillas/inicio.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()

    doc_externo=loader.get_template("inicio.html")
    #cxt=Context({"listado":Tareas})
    documento=doc_externo.render({"listado":Tareas})
    return HttpResponse(documento)

def game(request):
    FechaActualll=datetime.datetime.now()
    doc_externo=loader.get_template("games.html")
    documento=doc_externo.render({"FechaActualll": FechaActualll})
    return HttpResponse(documento)

def musica(request):
    FechaActualll=datetime.datetime.now()
    doc_externo=loader.get_template("musica.html")
    documento=doc_externo.render({"FechaActualll": FechaActualll})
    return HttpResponse(documento)
    
