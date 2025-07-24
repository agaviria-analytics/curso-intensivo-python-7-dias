
# 🐍 Curso Intensivo: Dominar los Fundamentos de Python en 7 Días

Este repositorio contiene la ruta de aprendizaje intensiva en Python, diseñada para dominar fundamentos esenciales y aplicarlos a un mini proyecto final.

## 📅 Cronograma de Estudio

### 📚 Accede al contenido del curso por días

| Día | Tema | Enlace |
|-----|------|--------|
| Día 1 | `print()`, `input()`, variables, entorno virtual | [Día 1](./Dia%201/README.md) |
| Día 2 | Condicionales (`if`, `elif`, `else`) y operadores |[Día 2](./Dia%202/README.md) |
| Día 3 | Bucles `for`, `while`, listas y diccionarios | [Día 3](./Dia%203/README.md) |
| Día 4 | Funciones, módulos, parámetros | [Día 4](./Dia%204/README.md) |
| Día 5 | Archivos `.txt`, `.csv` y pandas | [Día 5](./Dia%205/README.md) |
| Día 6 | Limpieza y análisis de datos | [Día 6](./Dia%206/README.md) |
| Día 7 | Mini proyecto + Exportación a Excel | [Día 7](./Dia%207/README.md) |


---

## 🔧 Tips técnicos clave

- Crear entorno virtual: `python -m venv venv`
- Activar entorno: `venv\Scripts\activate` (Windows)
- Instalar pandas: `pip install pandas openpyxl`
- Leer archivo Excel:
  ```python
  pd.read_excel("archivo.xlsx", engine="openpyxl")
  ```
- Convertir texto a numérico:
  ```python
  pd.to_numeric(columna, errors="coerce")
  ```
- Validar limpieza:
  ```python
  df.isnull().sum()
  df.info()
  df.describe()
  ```
- Aplicar formato texto:
  ```python
  df["columna"] = df["columna"].str.title()
  ```
- Exportar a Excel:
  ```python
  df.to_excel("archivo_limpio.xlsx", index=False, engine="openpyxl")
  ```

---

## ✅ Recomendaciones finales

- Comentar el código por bloques para su comprensión.
- Aplicar limpieza antes del análisis.
- Documentar los proyectos con README detallados.
- Subir los avances a GitHub como parte del portafolio profesional.

---

🎓 **Este repositorio está diseñado para mostrar dominio progresivo en Python, ideal para roles de Analista de Datos Junior.**
