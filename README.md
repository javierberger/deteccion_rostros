# Detector de Rostros - Escuela de Robótica Misiones

Este proyecto es una aplicación de detección de rostros en tiempo real utilizando YOLOv11 y OpenCV, desarrollada para la Escuela de Robótica de Misiones.

## Características

- Detección de rostros en tiempo real utilizando YOLOv11
- Interfaz gráfica de usuario con Tkinter
- Soporte para múltiples fuentes de video (webcam local, cámara IP, cámara RTSP)
- Ajuste de nivel de confianza para la detección
- Captura de imágenes con fecha y hora
- Visualización de logo personalizado en la transmisión de video

## Requisitos

- Python 3.7+
- OpenCV
- NumPy
- Ultralytics 8.3.14 (para YOLOv11)
- Tkinter
- Pillow

Para instalar todas las dependencias, ejecute:

```
pip install -r requirements.txt
```

**Nota:** Este proyecto utiliza Ultralytics versión 8.3.14 específicamente. Asegúrese de tener esta versión instalada para garantizar la compatibilidad con YOLOv11 y el código del proyecto.

## Estructura del Proyecto

```
ERM_rostros/
├── detector_rostros.py
├── logos/
│   ├── erm.ico
│   └── erm.png
└── modelos/
    └── rostros.pt
```

## Uso

1. Asegúrese de tener todos los requisitos instalados.
2. Coloque su modelo YOLOv11 entrenado (`rostros.pt`) en la carpeta `modelos/`.
3. Coloque sus archivos de logo (`erm.ico` y `erm.png`) en la carpeta `logos/`.
4. Ejecute el script:

```
python detector_rostros.py
```

5. Use los botones de la interfaz para seleccionar la fuente de video y capturar imágenes.
6. Ajuste el nivel de confianza usando el deslizador.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abra un issue primero para discutir qué le gustaría cambiar.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)
