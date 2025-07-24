## 📘 DÍA 3 – Bucles, Listas y Diccionarios en Python

### 🎯 Objetivo del día  
Dominar estructuras de datos fundamentales (`listas`, `diccionarios`) y recorrerlas usando bucles (`for`, `while`) para automatizar procesos repetitivos.

---

### 🔁 Bucles

#### 🔹 `for`
```python
for i in range(5):
    print("Iteración:", i)
```
- `range(5)` genera: `0, 1, 2, 3, 4`
- Se usa para recorrer listas, rangos o cadenas

#### 🔹 `while`
```python
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1
```
- Se ejecuta **mientras la condición sea verdadera**

---

### 📦 Listas
Colección ordenada y modificable:
```python
comidas = ["Pizza", "Arepa", "Tamal"]
print(comidas[0])        # Accede al primer elemento
comidas.append("Arroz")  # Agrega al final
```

---

### 🔑 Diccionarios
Estructura de pares clave–valor:
```python
mascota = {
    "nombre": "Lucas",
    "edad": 8,
    "especie": "perro"
}
```

Recorrido:
```python
for clave, valor in mascota.items():
    print(f"{clave.capitalize()}: {valor}")
```

---

## 🧪 Ejercicios prácticos – `ejercicios_dia3.py`

### ✅ 1. Mostrar comidas favoritas
```python
comidas = ["Arroz con pollo", "Pescado", "Hamburguesa", "Pastel de pollo", "Pizza"]
for comida in comidas:
    print("Una de mis comidas favoritas es:", comida)
```

---

### ✅ 2. Números pares y suma total
```python
numeros = [1, 3, 8, 20, 5, 6, 9, 13, 33, 7]
suma = 0

print("Números pares:")
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
    suma += numero

print("La suma total es:", suma)
```

---

### ✅ 3. Agregar nombres con `append()`
```python
nombres = []

for i in range(3):
    nombre = input("Ingresa un nombre: ")
    nombres.append(nombre)

print("Los nombres ingresados fueron:", nombres)
```

---

### ✅ 4. Diccionario de mascota
```python
mascota = {
    "nombre": "Lucas",
    "edad": 8,
    "especie": "perro"
}

for clave, valor in mascota.items():
    print(f"{clave.capitalize()}: {valor}")
```

---

### ✅ 5. Lista de productos con diccionarios
```python
productos = [
    {"nombre": "Arroz", "precio": 2500},
    {"nombre": "Aceite", "precio": 8500},
    {"nombre": "Sal", "precio": 1500}
]

for producto in productos:
    print(f"El producto {producto['nombre']} cuesta {producto['precio']}")
```

---

## 🧠 Tips del día

- Usa `for` para recorrer listas y `for clave, valor in dict.items()` para diccionarios.
- `.append()` agrega elementos a una lista.
- `%` no puede aplicarse a una lista completa, solo a cada número individual.
- Si haces un `while`, asegúrate de que la condición cambie para evitar bucles infinitos.
- Usa `capitalize()` para mostrar claves de diccionario con la primera letra en mayúscula.

---


