# Appium Mobile App Testing – YouTube

Este proyecto contiene una serie de pruebas automatizadas realizadas con **Appium** para la aplicación móvil de **YouTube**, utilizando **Python** como lenguaje principal.

## Objetivo

Automatizar acciones comunes en la app de YouTube como abrir la app, buscar un video, desplazarse en los resultados y reproducir videos específicos.

## Pruebas Implementadas

- `test_open_youtube.py` – Verifica que la app se abra correctamente.
- `test_search_video.py` – Realiza una búsqueda de videos.
- `test_scroll_results.py` – Realiza scroll vertical para ver más resultados.
- `test_play_video.py` – Toca el primer video de la lista para reproducirlo.
- `test_play_minecraft_trailer.py` – Busca y reproduce el tráiler oficial de la película de Minecraft.

## Tecnologías Utilizadas

- Appium
- Python 3
- Selenium WebDriver
- Emulador Android (AVD)
- Visual Studio Code

## Cómo Ejecutar

1. Asegúrate de tener el servidor de Appium corriendo (`http://localhost:4723`).
2. Conecta un emulador o dispositivo Android.
3. Ejecuta cualquier script:

```bash
python3 test_open_youtube.py