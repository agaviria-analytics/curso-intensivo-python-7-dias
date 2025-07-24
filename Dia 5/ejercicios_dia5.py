# Leer un archivo txt
# with open("datos_personales.txt", "r", encoding="utf-8") as f:
#     contenido = f.read()
#     print("Contenido del archivo TXT:")
#     print(contenido)

# Leer un archivo csv
import pandas as pd

archivo = "productos.csv"
df=pd.read_csv(archivo,encoding="utf-8")
print("\nPrimeras filas del archivo productos.csv")
print(df.head())
print(df.columns) 
print(df["precio"].mean())
print(df[df["precio"]>5000])
