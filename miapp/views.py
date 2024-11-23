from django.shortcuts import render

def grafica(request):
    # Datos para la gráfica
    context = {
        'labels': ['Enero', 'Febrero', 'Marzo'],  # Etiquetas dinámicas
        'data': [10, 20, 30],  # Datos dinámicos
    }
    return render(request, 'grafica.html', context)
