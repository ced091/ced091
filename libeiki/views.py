from django.shortcuts import render
from .forms import CommentaireForm

from django.views.decorators.csrf import csrf_protect

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

def generer_star_rating(value):
    return [
        {
            'index': x,
            'active': x <= value,
            'value': x / 2,
            'checked': x / 2 == value,
        }
        for x in range(1, 11)
    ]

@csrf_protect
def send_commentaire(request):
    
    print(request.POST)
    if request.POST:
        form = CommentaireForm(request.POST)
        if form.is_valid():
            form.save()
            print("merci pour votre contribution")
            return render(request, "libeiki/accueil.html")
        else:
            print(f"erreurs suivantes : {form.errors}  ")
    else:
        form = CommentaireForm()
            
    context ={
        'form': form,
        'star_data': 5,
    }
    return render(request, "libeiki/commentaire.html", context)
