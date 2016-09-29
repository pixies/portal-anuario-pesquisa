from django.shortcuts import render
from .models import Pesquisador 

# Create your views here.

def todos_pesquisadores(request):
	context = {}

	context['pesquisadores'] = Pesquisador.objects.all()

	return render (request, 'todos.html', context)

def pesquisador(request, id_pesquisador):
	pass

def editar_pesquisador(request, id_pesquisador):
	pass

def remover_pesquisador(request, id_pesquisador):
	pass