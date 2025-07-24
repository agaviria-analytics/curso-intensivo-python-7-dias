# Archivo: utilidades.py
# Funciones reutilizables

def calcular_area(base, altura):
    return base * altura

def es_par(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

def saludar(nombre):
    return f"Hola, {nombre}!"

def cuadrado(n):
    return n * n
