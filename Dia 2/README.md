# 📘 DÍA 2 – Condicionales y Operadores en Python

🎯 **Objetivo del día**  
Aprender a controlar el flujo del programa usando estructuras condicionales (`if`, `elif`, `else`), junto con operadores de comparación y operadores lógicos para tomar decisiones inteligentes.

---

## 🔣 Operadores de comparación

| Operador | Significado     | Ejemplo (a = 5, b = 3) |
|----------|------------------|------------------------|
| `==`     | Igual            | `a == b` → False       |
| `!=`     | Distinto de      | `a != b` → True        |
| `<`      | Menor que        | `a < b` → False        |
| `>`      | Mayor que        | `a > b` → True         |
| `<=`     | Menor o igual    | `a <= b` → False       |
| `>=`     | Mayor o igual    | `a >= b` → True        |

---

## 🔗 Operadores lógicos

| Operador | Función                                  | Ejemplo                                       |
|----------|------------------------------------------|-----------------------------------------------|
| `and`    | Ambas condiciones deben ser verdaderas   | `edad > 18 and ciudad == "Medellín"`          |
| `or`     | Al menos una debe ser verdadera          | `ciudad == "Bogotá" or ciudad == "Cali"`      |
| `not`    | Niega la condición                       | `not activo` → Invierte el valor lógico       |

---

## 💻 Script base – `dia2_condicionales.py`

### Evaluar si un número es positivo, negativo o cero
```python
numero = int(input("Ingrese un número: "))

if numero > 0:
    print("El número es positivo")
elif numero == 0:
    print("El número es cero")
else:
    print("El número es negativo")
```

### Validar edad para votar
```python
edad = int(input("¿Cuál es tu edad?: "))
if edad >= 18:
    print("Puedes votar")
else:
    print("Aún no puedes votar")
```

### Verificación de usuario y contraseña
```python
usuario = input("Usuario: ")
contrasena = input("Contraseña: ")

if usuario == "admin" and contrasena == "1234":
    print("Acceso permitido")
else:
    print("Acceso denegado")
```

---

## 🧠 Tips del día

- Siempre valida la entrada del usuario (`input()`) antes de hacer cálculos.
- Usa `elif` cuando tengas múltiples condiciones que no se deben solapar.
- Para comparar texto, puedes usar `.lower()` y evitar errores por mayúsculas.
- El operador `%` (módulo) es útil para saber si un número es par o múltiplo.
- Evalúa primero los errores o casos límites para hacer tu programa más robusto.
