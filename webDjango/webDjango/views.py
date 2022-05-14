from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
    return render(request,'index.html',{})#reder recibe tres argumentos, primeero el request, segundo el html que renderizamos y el tercero un diccionario