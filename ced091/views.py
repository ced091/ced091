from django.shortcuts import render
from datetime import datetime

def main(request):
    date_now = datetime.now()
    affichage_date = date_now.strftime("%d-%m-%Y %H:%M:%S")
    context = {
        "date_nom": affichage_date
    }
    return render(request, "ced091/main.html", context)