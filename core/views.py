from django.shortcuts import render, redirect
from core.models import Evento

# Create your views here.

# def index(request):
#     return redirect('/agenda/')

def lista_eventos(request):

    #evento = Evento.objects.get(id=1)
    evento = Evento.objects.all()
    #usuario = request.user
    #evento = Evento.objects.filter(usuario=usuario)
    print('eventos = {}'.format(evento))
    print(type(evento))
    dados = {'eventos':evento}
    print('os dados são {}'.format(dados))
    return render(request, 'agenda.html', dados)
