# Leer archivo txt
with open("mensaje.txt", "w", encoding="utf-8") as f:
    f.write("Hola desde Python\nEste es un archivo de texto")

with open("mensaje.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
    print("Contenido del archivo TXT:")
    print(contenido)

# Leer CSV con pandas
import pandas as pd
df = pd.read_csv("ventas.csv", encoding="utf-8")
print("\nPrimeras filas del archivo CSV:")
print(df.head())    