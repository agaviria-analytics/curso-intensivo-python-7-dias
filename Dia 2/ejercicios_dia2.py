# 1. Verificar si un número ingresado es par o impar
numero = int(input("Ingrese el número: "))
if numero %2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")  


# 2. Preguntar al usuario su edad y si tiene cédula, y verificar si puede entrar a una discoteca
edad = int(input("por favor ingrese su edad : "))
cedula = input("Tiene cedula:? (si/no): ")

if edad >=18 and cedula.lower() == "si" :
    print("Puede ingresar a la discoteca")
else:
    print("No puede ingresar")    

#3. Validar si un estudiante aprueba:
nota = float(input("Ingrese la nota del estudiante (0 a 5):"))
if nota >=3.0:
    print("El estudiante aprobo curso")
else:
    print("El estudiante Reprobo")   

# 4. Calificación con elif:
# 0 - 2.9 → "Insuficiente"
# 3.0 - 3.9 → "Aceptable"
# 4.0 - 4.5 → "Bueno"
# 4.6 - 5.0 → "Excelente"

calificacion = float(input("Digite la calificación (0 a 5): "))
if calificacion < 0 or calificacion > 5 :
    print("Calificacion invalida debe estar entre 0 y 5. ")
elif calificacion <= 2.9:
    print("Insuficiente")
elif calificacion <= 3.9:
    print("Aceptable")  
elif calificacion <= 4.5:
    print("Bueno")
else:
    print("Excelente")          
       