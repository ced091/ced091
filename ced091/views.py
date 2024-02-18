import logging

from django.shortcuts import render
from datetime import datetime

from django.utils import timezone

from datetime import datetime, timedelta

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

def main(request):
    log_user(request, "main")
    date_now = datetime.now()
    affichage_date = date_now.strftime("%d-%m-%Y %H:%M:%S")
    context = {
        "date_nom": affichage_date
    }
    return render(request, "ced091/main.html", context)