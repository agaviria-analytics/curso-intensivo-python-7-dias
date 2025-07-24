## 📘 DÍA 4 – Funciones y Módulos en Python

### 🎯 Objetivo del día  
Aprender a crear funciones personalizadas y usar módulos en Python para reutilizar código y organizar proyectos como lo hacen los profesionales.

---

## 🧠 ¿Qué es una función?

Una función es un bloque de código reutilizable que se puede ejecutar cuando lo necesites.

```python
def saludar(nombre):
    print("Hola", nombre)
```

---

## 🧠 ¿Qué es `return`?

`return` devuelve un valor desde una función:

```python
def cuadrado(n):
    return n * n
```

---

## 🔄 ¿Qué es un módulo?

Un módulo es un archivo `.py` con funciones que puedes importar y usar desde otros scripts.

---

## ✅ Ejemplo completo de módulo

**Archivo: `utilidades.py`**

```python
def calcular_area(base, altura):
    return base * altura

def es_par(numero):
    return "Par" if numero % 2 == 0 else "Impar"

def saludar(nombre):
    return f"Hola, {nombre}!"

def cuadrado(n):
    return n * n
```

**Archivo: `practica_funciones.py`**

```python
from utilidades import calcular_area, es_par

print(calcular_area(5, 3))      # Resultado: 15
print(es_par(8))                # Resultado: Par
```

---

## 🧪 ejercicios_dia4.py – Desarrollo de funciones

```python
from utilidades import calcular_area, es_par, saludar, cuadrado

def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma    

def evaluar_nota(nota):
    if nota < 3:
        return "Reprobado"
    elif nota < 4:
        return "Aprobado"
    else:
        return "Excelente"

print(saludar("Héctor"))
print("Cuadrado de 5:", cuadrado(5))
print("Área del rectángulo 5x3:", calcular_area(5, 3))
print("Número 8:", es_par(8))
print("Suma lista:", sumar_lista([2, 4, 6]))
print("Evaluación nota 4.5:", evaluar_nota(4.5))
```

---

## 🧠 Tips del día

- Usa `def` para crear funciones reutilizables
- Usa `return` cuando la función tenga que devolver un resultado
- Guarda funciones comunes en módulos (`utilidades.py`)
- Importa solo lo necesario (`from modulo import funcion`)
- Ejecuta scripts desde la terminal usando: `python archivo.py`

---


