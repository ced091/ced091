from django.http import JsonResponse

from station_meteo.capteur_temp import reading_data

def refresh_data(request):
    data = reading_data()
    refresh_data = {
        "temp": str(round(data.temperature,2)),
        "pression": str(round(data.pressure,2)),
        "humidity": str(round(data.humidity,2)),
    }
    return JsonResponse(refresh_data)






