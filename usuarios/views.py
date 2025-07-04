from django.shortcuts import render
from .models import RegistroUsuario
from .utils import obtener_ip_cliente, geolocalizar_ip

def registrar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        ip = obtener_ip_cliente(request)
        geo = geolocalizar_ip(ip)
        
        RegistroUsuario.objects.create(
            nombre=nombre,
            email=email,
            ip=ip,
            ciudad=geo['ciudad'],
            pais=geo['pais']
        )
        
        return render(request, 'registro.html')
    
    return render(request, 'registro.html')
# Create your views here.
