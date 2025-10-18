# Converter-yt-to-mp3: Conversor Web de YouTube a MP3

## Descripción General

Este proyecto implementa una aplicación web para la conversión de enlaces de **YouTube** a archivos de audio en formato **MP3**. La solución utiliza el *framework* **Flask** de Python para el *backend* y la biblioteca **yt-dlp** para el proceso de descarga, extracción y codificación del audio.

La aplicación ofrece una interfaz sencilla para que los usuarios introduzcan una URL de YouTube y reciban un enlace de descarga directa al archivo MP3 resultante.

---

## Características Técnicas Clave

| Característica | Detalle Técnico | Componentes Relevantes |
| :--- | :--- | :--- |
| **Backend** | Servidor web basado en el microframework **Flask**. Maneja solicitudes POST y sirve archivos mediante `send_file`. | `app.py`, `Flask` |
| **Conversión de Audio** | Utiliza la biblioteca **yt-dlp** con un *postprocessor* para extraer el *stream* de audio de mayor calidad. | `yt-dlp`, `FFmpeg` |
| **Formato de Salida** | El audio extraído se codifica a **MP3** con una calidad preferida de **192 kbps**. | Configuración `ydl_opts` en `app.py` |
| **Gestión de Archivos** | Uso de **UUID** para crear directorios temporales aislados por cada conversión, asegurando un proceso de descarga y limpieza eficiente. | `uuid`, `os.makedirs`, `os.rmdir` |
| **Frontend** | Interfaz de usuario minimalista y responsiva, utilizando HTML5, JavaScript (Fetch API) y **Tailwind CSS** para los estilos. | `index.html`, `script.js` |
| **Rutas API** | **`/convert`** (POST para iniciar el proceso) y **`/download/<filename>`** (GET para servir el archivo final). | Decoradores `@app.route` |

---

## Requisitos del Sistema

Para la correcta ejecución de la aplicación, es necesario tener instalados los siguientes componentes:

1.  **Python 3.x**
2.  **pip** (Administrador de paquetes de Python)
3.  **FFmpeg:** Es **esencial** para la conversión de audio a MP3. Debe estar instalado en el sistema operativo y accesible desde la variable de entorno `PATH`.

---

## Instrucciones de Instalación y Despliegue

### 1. Clonación del Repositorio

```bash
git clone [https://github.com/Alexis-mish/Converter-yt-to-mp3.git](https://github.com/Alexis-mish/Converter-yt-to-mp3.git)
cd Converter-yt-to-mp3
