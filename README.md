# 📚 Índice Invertido con Streamlit

Aplicación web interactiva para la construcción y visualización de un **índice invertido**, implementando dos enfoques clásicos de indexación utilizados en sistemas de recuperación de información.

---

## 🚀 Características

- **Dos métodos de indexado:**
  - ✅ **Arreglos Ordenados**: Indexado incremental documento por documento
  - ✅ **Algoritmo Fast-Inv**: Construcción por lotes para múltiples documentos
- **Tokenización automática:**
  - Conversión a minúsculas
  - Eliminación de caracteres no alfabéticos
- **Visualización clara:**
  - Tabla interactiva con términos, frecuencia y documentos asociados
- **Operaciones CRUD completas:**
  - **Crear:** Indexar documentos individuales o por lotes
  - **Leer:** Búsqueda interactiva de términos
  - **Eliminar:** Eliminación eficiente de términos del índice
- **Estadísticas en tiempo real:**
  - Términos únicos
  - Total de postings
  - Documentos indexados
  - Promedios por término
- **Interfaz intuitiva:**
  - Panel lateral para configuración y operaciones
  - Diseño responsivo y fácil de usar

---

## 🛠️ Tecnologías Utilizadas

### 🔹 Dependencias principales
- **Python 3.8+**
- **Streamlit (v1.24+)** – Framework para aplicaciones web interactivas
- **Pandas (v2.0+)** – Manipulación y visualización de datos

### 🔹 Bibliotecas estándar
- `bisect` – Inserciones eficientes en listas ordenadas
- `collections.defaultdict` – Diccionarios con valores por defecto
- `re` – Expresiones regulares para tokenización
- `json` – Manejo de datos estructurados (extensible)

---

## 📦 Instalación y Configuración

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/EbrickM/Sistemas-extraclase
cd Sistemas-extraclase
```

### 2️⃣ Crear un entorno virtual (recomendado)
```bash
python -m venv venv
```

Activar entorno virtual:

- **Windows**
```bash
venv\Scripts\activate
```

- **Mac / Linux**
```bash
source venv/bin/activate
```

### 3️⃣ Instalar dependencias
```bash
pip install streamlit pandas
```

### 4️⃣ Ejecutar la aplicación
```bash
streamlit run indice_invertido.py
```

---

## 🎯 Uso de la Aplicación

### 🧩 Método 1: Arreglos Ordenados
1. Selecciona **"Arreglos Ordenados"** en el panel lateral
2. Ingresa un ID numérico para el documento
3. Escribe o pega el texto del documento
4. Haz clic en **"Agregar Documento"**
5. Repite el proceso para más documentos

### ⚡ Método 2: Fast-Inv (Procesamiento por Lotes)
1. Selecciona **"Fast-Inv"** en el panel lateral
2. Ingresa múltiples documentos (uno por línea)
3. Haz clic en **"Construir Índice Fast-Inv"**
4. El sistema indexará todos los documentos simultáneamente

### 🔎 Operaciones Adicionales
- **Buscar términos:** Usa el campo de búsqueda
- **Eliminar términos:** Ingresa un término y presiona el botón correspondiente
- **Visualización:** La tabla principal muestra:
  - Término
  - Frecuencia
  - Lista de documentos asociados

---

## 📊 Ejemplo de Salida

Tabla del índice invertido:

| Término | Frecuencia | Documentos |
|--------|------------|------------|
| gato   | 3          | [1, 3, 5]  |
| perro  | 2          | [2, 4]     |
| casa   | 1          | [1]        |

Estadísticas mostradas:
- **Términos únicos:** 15
- **Total de postings:** 42
- **Documentos indexados:** 10
- **Promedio postings/término:** 2.8

---

## 🏗️ Estructura del Código

### 📌 Clase Principal: `SimpleIndex`
- `tokenize()` – Divide el texto en tokens
- `add_document()` – Indexación incremental con arreglos ordenados
- `fast_inv_build()` – Construcción por lotes con Fast-Inv
- `remove_term()` – Eliminación de términos del índice
- `get_statistics()` – Cálculo de métricas del índice

### 🖥️ Interfaz de Usuario (Streamlit)
- **Panel lateral:** Configuración y entrada de datos
- **Área principal:** Tabla del índice y estadísticas
- **Estado de sesión:** Persistencia de datos entre interacciones

---

## 📈 Aplicaciones Prácticas

- 🔍 Motores de búsqueda
- 📄 Análisis de textos y corpus documentales
- 🤖 Sistemas de recomendación basados en contenido
- 🧠 Procesamiento de Lenguaje Natural (NLP)
- 🎓 Proyectos académicos de recuperación de información

---

## 🔄 Comparación de Métodos

| Característica | Arreglos Ordenados | Fast-Inv |
|----------------|-------------------|----------|
| Enfoque | Incremental | Por lotes |
| Eficiencia | Ideal para actualizaciones frecuentes | Ideal para indexación inicial |
| Complejidad | O(log n) por inserción | O(n log n) |
| Caso de uso | Flujo continuo de documentos | Corpus completo |

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas!

1. Haz un **fork** del proyecto
2. Crea una nueva rama  
   ```bash
git checkout -b feature/NuevaFuncionalidad
   ```
3. Realiza tus cambios y haz commit  
   ```bash
git commit -m "Agrega nueva funcionalidad"
   ```
4. Sube la rama  
   ```bash
git push origin feature/NuevaFuncionalidad
   ```
5. Abre un **Pull Request**

---

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT**.  
Consulta el archivo `LICENSE` para más información.

---

## 🔗 Enlaces

- 📂 Repositorio: https://github.com/EbrickM/Sistemas-extraclase  
- 🌐 Streamlit: https://streamlit.io  
- 📘 Pandas: https://pandas.pydata.org  

---

## ✨ Autor

Proyecto desarrollado con fines académicos para el estudio de **sistemas de recuperación de información**.

---

💬 *¿Tienes preguntas o sugerencias? Abre un issue en el repositorio.*
