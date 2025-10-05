from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    productos = [
        {"nombre": "Paleta de Mango", "precio": 35.00, "sabor": "Frutal"},
        {"nombre": "Paleta de Chocolate", "precio": 40.00, "sabor": "Cremoso"},
        {"nombre": "Paleta de Fresa con Leche", "precio": 38.50, "sabor": "Cremoso"},
        {"nombre": "Paleta de Coco", "precio": 37.00, "sabor": "Frutal"},
        {"nombre": "Paleta de Tamarindo", "precio": 32.00, "sabor": "Ácido"},
    ]
    contexto = {'productos': productos}
    return render(request, 'index.html', contexto)