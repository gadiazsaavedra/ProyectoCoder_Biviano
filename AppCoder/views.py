from AppCoder.models import Familiar
from django.http import HttpResponse
from django.template import loader

#from django.shortcuts import render

# Create your views here.


def visualizar_familiares(request) -> HttpResponse:
    template = loader.get_template("familiares.html")
    familiar1 = Familiar(
        nombre="Esteban", pariente="padre", edad=74, fecha_nacimiento="07-15-1948"
    )
    familiar2 = Familiar(
        nombre="Gladys", pariente="madre", edad=70, fecha_nacimiento="04-30-1952"
    )
    familiar3 = Familiar(
        nombre="Verónica", pariente="hija", edad=30, fecha_nacimiento="05-15-1992"
    )
    familiar4 = Familiar(
        nombre="Javier", pariente="hijo", edad=34, fecha_nacimiento="03-30-1988"
    )
    contexto = {
        "familiar1": familiar1,
        "familiar2": familiar2,
        "familiar3": familiar3,
        "familiar4": familiar4,
    }
    res = template.render(contexto)
    return HttpResponse(res)
    # return render(request, "AppCoder/familiares.html", contexto)
