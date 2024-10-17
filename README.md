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

## Instalación

1. Clone este repositorio:
   ```
   git clone https://github.com/tu-usuario/ERM_rostros.git
   ```
2. Navegue al directorio del proyecto:
   ```
   cd ERM_rostros
   ```
3. Instale las dependencias:
   ```
   pip install -r requirements.txt
   ```
4. Asegúrese de tener el modelo YOLOv11 (`rostros.pt`) en la carpeta `modelos/`.
5. Verifique que los archivos de logo (`erm.ico` y `erm.png`) estén en la carpeta `logos/`.

## Guía de Usuario

### Iniciando la Aplicación

1. Abra una terminal o línea de comandos.
2. Navegue hasta el directorio del proyecto.
3. Ejecute el siguiente comando:
   ```
   python detector_rostros.py
   ```
4. La aplicación se iniciará y verá la ventana principal con la transmisión de video y los controles.

### Selección de Fuente de Video

La aplicación permite utilizar tres tipos de fuentes de video:

1. **Webcam Local**:
   - Haga clic en el botón "Webcam Local".
   - La aplicación comenzará a mostrar el video de la webcam de su dispositivo.

2. **Cámara IP**:
   - Haga clic en el botón "Cámara IP".
   - Aparecerá un cuadro de diálogo.
   - Ingrese la dirección URL de su cámara IP (por ejemplo, http://192.168.1.100:8080/video).
   - Haga clic en "OK" para conectarse a la cámara IP.

3. **Cámara RTSP**:
   - Haga clic en el botón "Cámara RTSP".
   - Aparecerá un cuadro de diálogo.
   - Ingrese la URL RTSP de su cámara (por ejemplo, rtsp://username:password@ip_address:554/stream).
   - Haga clic en "OK" para conectarse a la cámara RTSP.

### Ajuste del Nivel de Confianza

- Utilice el deslizador "Nivel de Confianza (%)" para ajustar la sensibilidad de la detección de rostros.
- Mover el deslizador hacia la derecha aumenta el umbral de confianza, resultando en menos detecciones pero más precisas.
- Mover el deslizador hacia la izquierda disminuye el umbral, permitiendo más detecciones pero posiblemente algunas falsas.

### Captura de Imágenes

1. Haga clic en el botón "Capturar" para tomar una instantánea del video actual.
2. La imagen se guardará automáticamente en el directorio del proyecto.
3. El nombre del archivo incluirá la fecha y hora de la captura (por ejemplo, "captura_20231017_153045.jpg").
4. Aparecerá un mensaje confirmando que la imagen ha sido guardada.

### Visualización de Detecciones

- Los rostros detectados se mostrarán en la transmisión de video con rectángulos alrededor.
- El logo de la Escuela de Robótica de Misiones se mostrará en la esquina inferior derecha del video.

### Cierre de la Aplicación

- Para cerrar la aplicación, simplemente cierre la ventana principal.
- Esto detendrá la transmisión de video y liberará los recursos utilizados.

## Solución de Problemas

- Si la webcam no se inicia, verifique que no esté siendo utilizada por otra aplicación.
- Para problemas con cámaras IP o RTSP, asegúrese de que la URL sea correcta y que la cámara esté accesible desde su red.
- Si la detección de rostros no funciona como se espera, intente ajustar el nivel de confianza.

## Explicación del Código

El código principal está contenido en la clase `AplicacionDeteccionRostros`. Aquí se explican sus componentes principales:

### Inicialización (`__init__`)
- Configura la ventana principal de la aplicación.
- Carga el modelo YOLOv11, el icono de la aplicación y el logo.
- Inicializa la interfaz de usuario con botones y un deslizador.

### Métodos principales
- `usar_webcam()`, `usar_camara_ip()`, `usar_camara_rtsp()`: Permiten cambiar la fuente de video.
- `capturar()`: Captura y guarda una imagen del video actual.
- `actualizar()`: Método principal que procesa cada frame de video:
  1. Lee un frame del video.
  2. Aplica el modelo YOLOv11 para detectar rostros.
  3. Dibuja los resultados en el frame.
  4. Agrega el logo a la imagen.
  5. Muestra el frame procesado en la interfaz.

### Procesamiento de video
- `actualizar_confianza()`: Ajusta el umbral de confianza para la detección.
- `agregar_logo()`: Añade el logo de la escuela al frame de video.

### Interfaz gráfica
- Utiliza Tkinter para crear una interfaz de usuario intuitiva.
- Incluye botones para seleccionar la fuente de video y capturar imágenes.
- Un deslizador permite ajustar dinámicamente el nivel de confianza de la detección.

El flujo principal del programa está en un bucle continuo (`self.ventana.mainloop()`), que actualiza la interfaz y procesa el video en tiempo real.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abra un issue primero para discutir qué le gustaría cambiar.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)
