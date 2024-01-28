from django.shortcuts import render

def accueil(request):
    return render(request, "libeiki/accueil.html")

def reiki(request):
    return render(request, "libeiki/reiki.html")

def numerologie(request):
    return render(request, "libeiki/numerologie.html")

def quisuisje(request):
    return render(request, "libeiki/quisuisje.html")

def visage(request):
    return render(request, "libeiki/visage.html")

def sophrologie(request):
    return render(request, "libeiki/sophrologie.html")

def lignee_reiki(request):
    return render(request, "libeiki/lignee-reiki.html")

def contact(request):
    return render(request, "libeiki/contact.html")