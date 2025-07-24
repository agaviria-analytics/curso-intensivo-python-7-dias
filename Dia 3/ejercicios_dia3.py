# Crear una lista con 5 comidas favoritas y mostrar cada una con un for.
comidas = ["Arroz con pollo","Pescado","Hamburguesa","Pastel de pollo","Pizza"]
for comida in comidas:
    print("una de mis comidas favoritas son:",comida)
#comidas la lista completa
# comida el nombre tenporal dentro del bucle...accede a cada elemento    

# Crear una lista de números del 1 al 10 y mostrar:
# Solo los pares
# La suma total de todos los números

numeros = [1,3,8,20,5,6,9,13,33,7]
suma = 0
print("Números pares:")
for numero in numeros:
    if numero %2 == 0:
        print(numero)
    suma += numero
print("La suma total es: ", suma)        

# "Pedir al usuario 3 nombres y agregarlos a una lista usando append()"
nombres =[]

for i in range(3):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)

print("Los nombres ingresados fueron:",nombres)    

# Crear un diccionario con los datos de una mascota (nombre, edad, especie) y mostrarlos uno a uno.
mascota ={
    "nombre": "Lucas",
    "edad" : 8,
    "especie": "perro"
}
for clave in mascota:
    print(clave, ":", mascota[clave])

# Lista de productos con diccionarios
productos = [
    {"nombre": "Arroz", "precio": 2500},
    {"nombre": "Aceite", "precio": 8500},
    {"nombre": "Sal", "precio": 1500}
]

for producto in productos:
    print(f"El producto {producto['nombre']} cuesta {producto['precio']}")

