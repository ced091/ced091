import logging

from django.shortcuts import render, redirect
from .forms import CommentaireForm
from django.core.mail import EmailMessage
from django.utils import timezone

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Commentaire

logger = logging.getLogger(__name__)

def log_user(request, vue):
    username = request.user.username if request.user.is_authenticated else 'Anonymous'
    current_datetime = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', None)
    if ip_address is None:
        # Si l'en-tête X-Forwarded-For n'est pas disponible, utilisez l'adresse IP par défaut
        ip_address = request.META.get('REMOTE_ADDR', 'unknown')
    else:
        # Séparez les adresses IP si X-Forwarded-For contient plusieurs adresses
        ip_address = ip_address.split(",")[0].strip()
    logger.info(f'[{current_datetime}][{username}][{ip_address}] Accès à la vue {vue}')

# def envoyer_email_apres_soumission(commentaire, **kwargs):
#     message = f"Un nouveau commentaire a été soumis le {commentaire.date_com}.\n Voici son contenu : {commentaire.texte}. \n Sa note  : {commentaire.note}. \n Le pseudo : {commentaire.pseudo} \n Vous pouvez le rendre visible sur le site en cochant la case 'visible' dans le mode admin de votre site/admin.\n Tchuss."
#     email_msg = EmailMessage(
#         subject='Nouvelle soumission de commentaire LIBEIKI', 
#         body=message, 
#         from_email='ikiebil92@hotmail.com',
#         to=["ced091@hotmail.fr",  "libellule_1982@hotmail.com"]
#     )
#     email_msg.send()

def accueil(request):
    log_user(request, "accueil/libeiki")
    commentaires = Commentaire.objects.filter(visible=True)

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
    log_user(request, "reiki")
    return render(request, "libeiki/reiki.html")

def numerologie(request):
    log_user(request, "numerologie")
    return render(request, "libeiki/numerologie.html")

def quisuisje(request):
    log_user(request, "quisuisje")
    return render(request, "libeiki/quisuisje.html")

def massage(request):
    log_user(request, "massage")
    return render(request, "libeiki/massage.html")

def sophrologie(request):
    log_user(request, "sophrologie")
    return render(request, "libeiki/sophrologie.html")

def lignee_reiki(request):
    log_user(request, "lignee_reiki")
    return render(request, "libeiki/lignee-reiki.html")

def contact(request):
    log_user(request, "contact")
    return render(request, "libeiki/contact.html")

def tarif_reiki(request):
    log_user(request, "tarif_reiki")
    return render(request, "libeiki/tarif-reiki.html")

def tarif_numerologie(request):
    log_user(request, "tarif_numerologie")
    return render(request, "libeiki/tarif-numerologie.html")

def tarif_massage(request):
    log_user(request, "tarif_massage")
    return render(request, "libeiki/tarif-massage.html")

def tarif_sophrologie(request):
    log_user(request, "tarif_sophrologie")
    return render(request, "libeiki/tarif-sophrologie.html")

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
    
    log_user(request, "send_commentaire")
    if request.POST:
        form = CommentaireForm(request.POST)
        if form.is_valid():
            comm = form.save()
            print("merci pour votre contribution")
            # envoyer_email_apres_soumission(comm)
            return redirect('libeiki:accueil')
        else:
            print(f"erreurs suivantes : {form.errors}  ")
    else:
        form = CommentaireForm()
            
    context ={
        'form': form,
        'star_data': 5,
    }
    return render(request, "libeiki/commentaire.html", context)

def mentions_legales(request):
    return render(request, "libeiki/mentions_legales.html")
