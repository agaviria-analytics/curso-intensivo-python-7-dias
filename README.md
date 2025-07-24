
# 🐍 Curso Intensivo: Dominar los Fundamentos de Python en 7 Días

Este repositorio contiene la ruta de aprendizaje intensiva en Python, diseñada para dominar fundamentos esenciales y aplicarlos a un mini proyecto final.

## 📅 Cronograma de Estudio

| Día | Temas cubiertos |
|-----|------------------|
| Día 1 | `print()`, `input()`, variables, entorno virtual |
| Día 2 | `if`, `elif`, `else`, operadores lógicos |
| Día 3 | Bucles `for`, `while`, listas y diccionarios |
| Día 4 | Funciones, parámetros, módulos |
| Día 5 | Archivos `.txt` y `.csv`, introducción a `pandas` |
| Día 6 | Limpieza y análisis de datos con `pandas` |
| Día 7 | Mini proyecto: limpieza y exportación a Excel con columna calculada |

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
