# 📘 DÍA 1 – Fundamentos de Python

## 🎯 Objetivo del día
Aprender a crear un entorno virtual y dominar los conceptos más básicos de Python: `print()`, `input()`, comentarios, tipos de datos y ejecución de scripts.

---

## 🔧 ¿Qué es un entorno virtual y para qué sirve?

Un entorno virtual es un espacio aislado para instalar librerías sin afectar otros proyectos.

| Ventaja | Explicación |
|--------|-------------|
| 🧼 Aislamiento | Cada proyecto tiene sus propias versiones |
| 💥 Evita conflictos | Puedes usar diferentes versiones de librerías |
| 📁 Organización | Todo queda dentro de la carpeta `venv` |
| 💼 Profesionalismo | Es lo que se usa en entornos reales |

### 👉 Comandos para crear y activar

```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows
venv\Scripts\activate

💻 Script base – dia1_fundamentos.py
# Comentario de ejemplo
print("¡Hola, mundo!")

# Tipos de datos
nombre = "Héctor"
edad = 50
altura = 1.75
activo = True

print("Nombre:", nombre)
print("Edad:", edad)
print("¿Activo?", activo)

ciudad = input("¿En qué ciudad vives?: ")
print("Saludos desde", ciudad)

🧠 Explicación de conceptos
Elemento	Ejemplo	Descripción
print()	print("Hola")	Muestra un mensaje
Comentario	# Esto no se ejecuta	Explicación interna
input()	input("Ingresa algo")	Recoge texto del usuario
Tipos de datos	str, int, float, bool	Cadena, entero, decimal, lógico

🧑‍🏫 Tips del día

    💬 Comenta siempre tu código: ayuda a entenderlo después.

    🧠 Usa nombres claros para tus variables (nunca x, a, b sin sentido).

    🧪 Practica con distintos valores para ver el resultado.

    🎯 input() devuelve texto. Si vas a hacer operaciones matemáticas, convierte con int() o float().