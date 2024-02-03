from django.shortcuts import render
from .forms import CommentaireForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Commentaire

def accueil(request):
    commentaires = Commentaire.objects.all()

    # Définissez le nombre d'éléments par page
    elements_par_page = 5

    # Initialisez l'objet Paginator avec la liste des commentaires et le nombre d'éléments par page
    paginator = Paginator(commentaires, elements_par_page)

    # Obtenez le numéro de la page à partir des paramètres de requête
    page = request.GET.get('page')
    try:
        # Obtenez les commentaires pour la page spécifiée
        commentaires_page = paginator.page(page)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, affichez la première page
        commentaires_page = paginator.page(1)
    except EmptyPage:
        # Si la page est hors de portée (par exemple, 9999), affichez la dernière page
        commentaires_page = paginator.page(paginator.num_pages)
    context = {
        "commentaires": commentaires_page
    }
    return render(request, "libeiki/accueil.html", context)

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
