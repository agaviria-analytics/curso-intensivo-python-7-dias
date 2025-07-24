# Archivo: ejercicios_dia4.py
# Día 4 – Funciones y módulos

# Importar funciones desde utilidades.py
from utilidades import calcular_area, es_par, saludar, cuadrado

# 3. Función que reciba una lista y retorne la suma total
def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma    

# 4. Función que retorne evaluación según nota
def evaluar_nota(nota):
    if nota < 3:
        return "Reprobado"
    elif nota < 4:
        return "Aprobado"
    else:
        return "Excelente"

# 👇 Pruebas de uso
print(saludar("Héctor"))
print("Cuadrado de 5:", cuadrado(5))
print("Área del rectángulo 5x3:", calcular_area(5, 3))
print("Número 8:", es_par(8))
print("Número 7:", es_par(7))
print("Suma lista:", sumar_lista([2, 4, 6]))
print("Evaluación nota 4.5:", evaluar_nota(4.5))
