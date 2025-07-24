# 🧼 Día 6 – Limpieza de Datos con Pandas

En este ejercicio realizamos un flujo completo de limpieza básica de datos a partir de un archivo `CSV` sucio llamado `ventas_sucias.csv`.

---

## 📂 1. Lectura del archivo

Se utiliza `pandas.read_csv()` con codificación UTF-8 para cargar el archivo:

```python
df = pd.read_csv("ventas_sucias.csv", encoding="utf-8")
```

---

## 🧪 2. Conversión de tipos

Detectamos que `precio_unitario` viene como texto (tipo object), por lo que lo convertimos a numérico:

```python
df["precio_unitario"] = pd.to_numeric(df["precio_unitario"], errors="coerce")
```

- Los errores o textos vacíos se convierten en `NaN`.
- Este paso es importante para luego aplicar cálculos y estadísticas.

---

## 🧹 3. Limpieza de valores faltantes

### a. En `precio_unitario`:

Se reemplazan los valores `NaN` por **0** como valor por defecto (si no se conoce el precio):

```python
df["precio_unitario"] = df["precio_unitario"].fillna(0)
```

> 📌 También podríamos eliminarlos directamente con:
> ```python
> df.dropna(subset=["precio_unitario"])
> ```

---

### b. En `cliente`:

Detectamos un registro con cliente vacío (`NaN`). En vez de eliminarlo, se le asigna una etiqueta de validación:

```python
df["cliente"] = df["cliente"].fillna("Validar cliente")
```

> ✅ Esta técnica es común en entornos empresariales cuando se necesita **conservar la fila pero marcarla para revisión** por parte del área operativa.

---

## 👀 4. Exploración del DataFrame

### Estructura general:

```python
print(df.info())
```

### Primeras filas:

```python
print(df.head())
```

### Estadísticas descriptivas:

```python
print(df.describe())
```

---

## 📌 Conclusiones

- Aprendimos a detectar y tratar valores `NaN` con `fillna()` y `dropna()`.
- Aplicamos una conversión segura de datos numéricos.
- Simulamos una validación realista de registros vacíos, útil en entornos de negocio.

---

👨‍💻 *Este ejercicio forma parte del Curso Intensivo de Python – Fundamentos Día 6.*
