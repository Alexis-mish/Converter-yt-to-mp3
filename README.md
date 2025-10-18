# Converter-yt-to-mp3: Conversor Web de YouTube a MP3

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-black.svg)](https://flask.palletsprojects.com/)
[![Conversión](https://img.shields.io/badge/Tool-yt--dlp%20%26%20FFmpeg-red.svg)]()

## Visión General

Este proyecto implementa una aplicación web eficiente para la conversión directa de **enlaces de YouTube a archivos de audio en formato MP3**. La solución está desarrollada en **Python** utilizando el microframework **Flask** para el *backend* y la poderosa biblioteca **yt-dlp** (junto con FFmpeg) para manejar la extracción y codificación del audio.

El objetivo es proporcionar una herramienta sencilla y rápida para obtener la pista de audio de cualquier video de YouTube con una calidad de audio predefinida.

---

## Características Técnicas Clave

| Componente | Herramienta | Descripción |
| :--- | :--- | :--- |
| **Backend** | Flask | Servidor web ligero para gestionar las peticiones POST de conversión y la entrega de archivos MP3. |
| **Extractor** | yt-dlp | Utilizado para descargar el *stream* de audio de mejor calidad. |
| **Codificación** | FFmpeg | Esencial para el *post-procesamiento* que convierte el audio extraído al formato **MP3** con una calidad de **192 kbps**. |
| **Arquitectura** | UUID | Generación de identificadores únicos para crear directorios temporales aislados, garantizando la seguridad y la limpieza de archivos después de cada conversión. |
| **Frontend** | HTML, JS, Tailwind CSS | Interfaz de usuario intuitiva que maneja las solicitudes de conversión mediante **Fetch API** (AJAX). |

---

## Estructura del Proyecto

La aplicación mantiene una estructura estándar de Flask:

Converter-yt-to-mp3/ ├── app.py # Lógica del servidor, rutas y manejo de yt-dlp. ├── downloads/ # Directorio donde se guardan los archivos MP3 finales. ├── static/ │ └── script.js # Lógica JavaScript para la interacción con la API. └── templates/ └── index.html # Interfaz de usuario principal.
