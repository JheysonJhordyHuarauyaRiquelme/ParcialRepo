# Imagen base
FROM python:3.12-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos de requerimientos
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar toda la aplicación
COPY . .

# Exponer el puerto
EXPOSE 8080

# Ejecutar FastAPI con uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
