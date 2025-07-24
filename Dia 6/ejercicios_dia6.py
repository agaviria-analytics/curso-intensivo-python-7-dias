import pandas as pd

# 1️⃣ Leer archivo CSV con codificación correcta
df = pd.read_csv("ventas_sucias.csv", encoding="utf-8")

# 2️⃣ Convertir columna "precio_unitario" a numérico
# Si encuentra errores (como textos o vacíos), los convierte en NaN
df["precio_unitario"] = pd.to_numeric(df["precio_unitario"], errors="coerce")

# 3️⃣ Reemplazar los NaN con un valor por defecto (0)
# Esto conserva la fila, pero asigna 0 si no había precio
df["precio_unitario"] = df["precio_unitario"].fillna(0)


# 3️⃣ Reemplazar los NaN con un valor por defecto (0)
# Esto conserva la fila, pero asigna 0 si no había precio
df["cliente"] = df["cliente"].fillna("Validar cliente")

# 4️⃣ Mostrar primeras filas
print("Vista previa del archivo sucio:")
print(df.head())

# 5️⃣ Información general: columnas, tipos y datos no nulos
print("\n📌 Información general del archivo:")
print(df.info())

# 6️⃣ Estadísticas descriptivas (solo para columnas numéricas)
print("\n📌 Estadísticas descriptivas:")
print(df.describe())
