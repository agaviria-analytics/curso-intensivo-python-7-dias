## 📘 DÍA 5 – Lectura de Archivos TXT y CSV con Python y Pandas

### 🎯 Objetivo del día  
Aprender a trabajar con archivos `.txt` y `.csv` en Python, usando funciones nativas y la librería `pandas`, fundamental para el análisis de datos.

---

## 🧾 Leer archivos `.txt` en Python

### ✅ Escribir archivo de texto
```python
with open("datos_personales.txt", "w", encoding="utf-8") as f:
    f.write("Nombre: Pepito Pérez\n")
    f.write("Edad: 30\n")
    f.write("Ciudad: Medellín\n")
```

### ✅ Leer archivo de texto
```python
with open("datos_personales.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())
```

---

## 📄 Leer archivos `.csv` con Pandas

### ✅ Código básico
```python
import pandas as pd

df = pd.read_csv("productos.csv", encoding="utf-8")
print(df.head())
```

### ✅ Estructura de `productos.csv` de ejemplo
```
nombre,precio
Arroz,2500
Aceite,8500
Leche,4000
Chocolate,9500
```

---

## 💻 Script completo – `ejercicios_dia5.py`

```python
# 1. Crear archivo datos_personales.txt y escribir información
with open("datos_personales.txt", "w", encoding="utf-8") as f:
    f.write("Nombre: Pepito Pérez\n")
    f.write("Edad: 30\n")
    f.write("Ciudad: Medellín\n")

# 2. Leer archivo línea por línea
print("Contenido de datos_personales.txt:")
with open("datos_personales.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())

# 3. Leer archivo productos.csv
import pandas as pd
df = pd.read_csv("productos.csv", encoding="utf-8")

# 4. Mostrar primeras 3 filas
print("\nPrimeras 3 filas del CSV:")
print(df.head(3))

# 5. Filtrar productos con precio > 5000
print("\nProductos con precio mayor a 5000:")
print(df[df["precio"] > 5000])
```

---

## 🧠 Tips del día

- Usa `open()` para trabajar con archivos `.txt`
- Usa `pandas.read_csv()` para leer archivos `.csv`
- Siempre especifica `encoding="utf-8"` para evitar errores de acentos
- Puedes usar `df.head()` para ver los primeros registros y `df[df["col"] > x]` para filtrar datos
- Guarda los archivos `.csv` en la misma carpeta del script para evitar errores de ruta

---