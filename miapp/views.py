from django.shortcuts import render

def mensaje(request):
    return render(request, 'miapp/mensaje.html')
