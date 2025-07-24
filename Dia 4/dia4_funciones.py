# Función sin parámetros
def mostrar_bienvenida():
    print("Bienvenido al programa de funciones")

#Función con un parámetro
def saludar_usuario(nombre):
    print(f"Hola, {nombre}")

#Función que retorna un resultado
def multiplicar(x,y):
    return x * y

#Llamadas
mostrar_bienvenida()
saludar_usuario("Hector")
resultado = multiplicar(4,6)
print(resultado)

