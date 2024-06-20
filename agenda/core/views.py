from django.shortcuts import redirect, render, HttpResponse

from core.models import Evento

# Create your views here.
#era pra ser local mas deixa data msm 
def Evento_local(request, titulo_evento):
    return HttpResponse(f"A data do evento é: {Evento.objects.get(titulo = titulo_evento).data_evento}")
    
    
def lista_eventos(request):
    # usuario = request.user
    # evento = Evento.objects.filter(usuario=usuario)
    evento = Evento.objects.all()
    dados = {"eventos": evento}
    
    return render(request, "agenda.html", dados)

# def index(request):
#     return redirect("/agenda/")
