from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def about(request):
    return HttpResponse("<h2>Sobre Nosotros</h2>")    
