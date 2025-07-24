
# 🐍 Día 7 – Mini Proyecto: Limpieza y Exportación de Ventas a Excel

Este mini proyecto cierra el curso **"Dominar los Fundamentos de Python en 7 Días"**, realizando un flujo completo con `pandas`:
- Lectura de archivo Excel sucio
- Limpieza de datos
- Estandarización
- Cálculo de columna total
- Exportación final a un nuevo archivo limpio

---

## 📂 Estructura de Archivos

- `datos_ventas_dia7.xlsx`: archivo original con errores
- `mini_proyecto.py`: script de limpieza
- `archivo_ventas_limpio.xlsx`: archivo generado limpio
- `README.md`: este archivo

---

## ✅ Pasos realizados

### 1. Leer el archivo Excel
```python
df = pd.read_excel("datos_ventas_dia7.xlsx", sheet_name="Sheet1")
```

📌 **TIP IMPORTANTE:** Si aparece el error  
`ImportError: Missing optional dependency 'openpyxl'`  
es porque `pandas` usa `openpyxl` para leer archivos `.xlsx`.

✅ Solución:
```bash
pip install openpyxl
```

---

### 2. Convertir columnas a numéricas
```python
df["precio_unitario"] = pd.to_numeric(df["precio_unitario"], errors="coerce").fillna(0)
```
- Se convierte la columna a numérica.
- Los errores o celdas vacías se convierten en `NaN`.
- Luego, se reemplazan por 0.

---

### 3. Rellenar datos faltantes y normalizar texto
```python
df["cliente"] = df["cliente"].fillna("Validar dato")
df["producto"] = df["producto"].str.title()
df["cliente"] = df["cliente"].str.title()
```
- Los valores faltantes en `cliente` se etiquetan como `"Validar dato"`.
- Se capitalizan los nombres (`str.title()`).

---

### 4. Crear columna calculada `Total_ventas`
```python
df["Total_ventas"] = df["cantidad"] * df["precio_unitario"]
```

---

### 5. Exportar archivo limpio
```python
df.to_excel("archivo_ventas_limpio.xlsx", index=False, engine="openpyxl")
```
- Se exporta sin índice.
- Se recomienda incluir `engine="openpyxl"` para evitar errores.

---

## 🧠 Verificaciones opcionales
```python
print(df.isnull().sum())   # Verificar valores nulos
print(df.head())           # Ver vista previa
print(df.info())           # Validar tipos
```

---

## ✅ Resultado Final
Archivo limpio y listo para análisis o carga en Power BI: `archivo_ventas_limpio.xlsx`.

---

🎯 Este ejercicio refuerza los conceptos clave del análisis con `pandas`, dejando un ejemplo profesional y completo.

