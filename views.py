from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse(f"<h1>ITS Academy Terni - Homepage(modifica)</h1>")
