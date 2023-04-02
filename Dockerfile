# Seleccionamos la imagen base de Python 3
FROM python:3

# Establecemos el directorio de trabajo de la aplicación en el contenedor
WORKDIR /app

# Copiamos los archivos de la aplicación a la imagen
COPY . /app

# Instalamos las dependencias de la aplicación
RUN pip install -r requirements.txt

# Exponemos el puerto en el que se ejecuta la aplicación
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
