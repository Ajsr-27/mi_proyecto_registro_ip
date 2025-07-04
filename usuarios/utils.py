import requests

def obtener_ip_cliente(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def geolocalizar_ip(ip):
    try:
        response = requests.get(f'https://ipapi.co/{ip}/json')
        data = response.json()
        return {
            'ciudad': data.get('city'),
            'pais': data.get('country_name')
        }
    except:
        return {'ciudad': None, 'pais': None}