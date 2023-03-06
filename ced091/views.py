from django.shortcuts import render
from datetime import datetime

def main(request):
    date_now = datetime.now()
    context = {
        "date_nom": str(date_now)
    }
    return render(request, "ced091/main.html", context)