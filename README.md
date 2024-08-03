# 
# Convertidor de YouTube MP4 a MP3

Este proyecto es una aplicación en Python con PyQt6 que permite convertir videos de YouTube en formato MP4 a archivos MP3.

## Autor

@PetusoTwo

## Descripción

Esta aplicación utiliza PyQt6 para proporcionar una interfaz gráfica que permite a los usuarios ingresar un enlace de YouTube, seleccionar una ruta de destino y convertir el video a formato MP3. Utiliza la biblioteca `pytube` para la descarga del video y la conversión del formato.

## Requisitos

- Python 3.x
- PyQt6
- pytube

  ## Uso

### Interfaz de Usuario

1. **Ingresar Enlace de YouTube:**
   - Introduce el enlace del video de YouTube que deseas convertir en el campo de texto correspondiente.

2. **Elegir Ruta de Destino:**
   - Haz clic en el botón para seleccionar la carpeta donde se guardará el archivo MP3 convertido.

3. **Convertir a MP3:**
   - Haz clic en el botón para iniciar la conversión. La aplicación descargará el video en formato MP4 y lo convertirá a MP3 en la ruta seleccionada.

### Ejecución

- Ejecuta el script de Python para iniciar la aplicación.

Puedes instalar las bibliotecas necesarias usando `pip`:

```bash
pip install PyQt6 pytube
