import pandas as pd

# Paso 1: Leer archivo Excel
df=pd.read_excel("datos_ventas_dia7.xlsx",sheet_name="Sheet1")

# Paso 2: Convertir precio a numérico y limpiar valores faltantes
df["precio_unitario"]=pd.to_numeric(df["precio_unitario"],errors="coerce")
df["precio_unitario"]=df["precio_unitario"].fillna(0)
df["cliente"]=df["cliente"].fillna("Validar dato")

# Paso 3: Estandarizar nombres
df["producto"]=df["producto"].str.title()
df["cliente"]=df["cliente"].str.title()

# Paso 4: Calcular columna total
df["Total_ventas"]=df["cantidad"]*df["precio_unitario"]

# Paso 5: Exportar archivo limpio
print("\nArchivo listo y guardado")
df.to_excel('archivo_ventas_limpio.xlsx',index=False,engine='openpyxl')

# Verificar si hay NaN restantes
# print("\n Valores faltantes por columan")
# print(df.isnull().sum())

# Validar que el total esté bien calculado (opcional)
# print(df[["cantidad", "precio_unitario", "Total_ventas"]])

# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.columns)
