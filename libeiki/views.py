from django.shortcuts import render

def accueil(request):
    return render(request, "libeiki/accueil.html")

def reiki(request):
    return render(request, "libeiki/reiki.html")

def quisuisje(request):
    return render(request, "libeiki/quisuisje.html")