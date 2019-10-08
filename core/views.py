from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
   return HttpResponse("Use https://ifpitds.pythonanywhere.com/admin para acessar as aplicações")
