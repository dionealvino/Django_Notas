from django.shortcuts import render

# Create your views here.

def teste(request):
    return render(request, 'notas/html_teste.html', {})

def index(request):
	return render(request, 'notas/front/index.html', {})