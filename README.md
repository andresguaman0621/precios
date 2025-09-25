# Sistema de Toma de Precios

Aplicación web Flask para la gestión y toma de precios de productos agrícolas.

## Características

- ✅ Interfaz web intuitiva con tabla de productos
- ✅ Filtros de búsqueda por categoría, código y nombre
- ✅ Edición de precios actuales en tiempo real
- ✅ Función "Nueva toma de precios" para ciclos recurrentes
- ✅ Persistencia de datos en JSON
- ✅ 189 productos precargados organizados por categorías

## Instalación Local

```bash
# Clonar el repositorio
git clone <tu-repositorio>
cd precios

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python app.py
```

La aplicación estará disponible en `http://localhost:5000`

## Despliegue en Railway

1. Conecta tu repositorio GitHub a Railway
2. Railway detectará automáticamente la configuración Python
3. La aplicación se desplegará usando los archivos:
   - `Procfile`: Comando de inicio
   - `requirements.txt`: Dependencias Python
   - `runtime.txt`: Versión de Python
   - `railway.json`: Configuración de Railway

## Uso

1. **Ver productos**: La tabla muestra todos los productos con sus datos
2. **Filtrar**: Usa los filtros superiores para buscar productos específicos
3. **Tomar precios**: Ingresa valores en la columna "Precio Actual"
4. **Guardar**: Usa "Guardar Todos los Cambios" para persistir los datos
5. **Nueva toma**: "Nueva Toma de Precios" mueve precios actuales → anteriores

## Estructura de Datos

Cada producto tiene:
- `codigo`: Código único del producto
- `estado`: Estado especial (vacío o "x")
- `categoria`: FRUTAS, HORTALIZAS, ABASTOS, TUBERCÚLOS
- `nombre_completo`: Nombre descriptivo del producto
- `peso_kg`: Peso en kilogramos
- `precio_anterior`: Precio de la toma anterior
- `precio_actual`: Precio de la toma actual (editable)

## Tecnologías

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript vanilla
- **Datos**: JSON para persistencia
- **Despliegue**: Railway con Gunicorn