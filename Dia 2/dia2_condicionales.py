# #Evaluar si un numero es positivo
numero=int(input("Ingrese un numero: "))

if numero > 0:
    print("El número es positivo")
elif numero == 0:
    print("El número es cero") 
else:
    print("El número es negativo")


# verificar si una persona puede votar
edad =int(input("Cual es tu edad :"))

if edad >=18:
    print("Puede votar")
else:
    print("Aún no puede votar")

# Validar usuario y contraseña
usuario=input("Usuario: ")
password=input("Contraseña: ")

if usuario=="admin" and password=="1234":
    print("Acceso permitido")
else:
    print("Acceso denegado")


