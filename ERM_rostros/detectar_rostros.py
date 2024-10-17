import cv2
import numpy as np
from ultralytics import YOLO
import tkinter as tk
from tkinter import simpledialog, messagebox, Scale, Frame
from PIL import Image, ImageTk
import datetime
import os

class AplicacionDeteccionRostros:
    def __init__(self, ventana, titulo_ventana):
        self.ventana = ventana
        self.ventana.title(titulo_ventana)
        self.ventana.resizable(False, False)

        ancho_ventana = 800
        alto_ventana = 700
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)
        self.ventana.geometry(f'{ancho_ventana}x{alto_ventana}+{x}+{y}')

        directorio_actual = os.path.dirname(os.path.abspath(__file__))

        ruta_icono = os.path.join(directorio_actual, 'logos', 'erm.ico')
        icono = Image.open(ruta_icono)
        icono = ImageTk.PhotoImage(icono)
        self.ventana.iconphoto(True, icono)

        ruta_modelo = os.path.join(directorio_actual, 'modelos', 'rostros.pt')
        self.modelo = YOLO(ruta_modelo)

        ruta_logo = os.path.join(directorio_actual, 'logos', 'erm.png')
        self.logo = cv2.imread(ruta_logo, cv2.IMREAD_UNCHANGED)
        self.logo = self.redimensionar_logo(self.logo, 150)

        self.fuente_video = 0
        self.video = None
        self.umbral_confianza = 0.6

        self.lienzo = tk.Canvas(ventana, width=640, height=480)
        self.lienzo.pack(pady=10)

        marco_botones = Frame(ventana)
        marco_botones.pack(fill=tk.X, padx=5, pady=5)
        marco_botones.pack_propagate(False)
        marco_botones.configure(width=800, height=50)

        self.boton_webcam = tk.Button(marco_botones, text="Webcam Local", width=15, command=self.usar_webcam)
        self.boton_webcam.pack(side=tk.LEFT, expand=True)

        self.boton_ip = tk.Button(marco_botones, text="Cámara IP", width=15, command=self.usar_camara_ip)
        self.boton_ip.pack(side=tk.LEFT, expand=True)

        self.boton_rtsp = tk.Button(marco_botones, text="Cámara RTSP", width=15, command=self.usar_camara_rtsp)
        self.boton_rtsp.pack(side=tk.LEFT, expand=True)

        self.boton_captura = tk.Button(marco_botones, text="Capturar", width=15, command=self.capturar)
        self.boton_captura.pack(side=tk.LEFT, expand=True)

        self.deslizador_confianza = Scale(ventana, from_=0, to=100, orient=tk.HORIZONTAL, label="Nivel de Confianza (%)",
                                       command=self.actualizar_confianza, length=700)
        self.deslizador_confianza.set(60)
        self.deslizador_confianza.pack(pady=10)

        self.usar_webcam()

        self.retraso = 15
        self.actualizar()

        self.ventana.mainloop()

    def redimensionar_logo(self, logo, ancho_objetivo):
        relacion_aspecto = logo.shape[1] / logo.shape[0]
        nuevo_ancho = ancho_objetivo
        nuevo_alto = int(nuevo_ancho / relacion_aspecto)
        return cv2.resize(logo, (nuevo_ancho, nuevo_alto))

    def usar_webcam(self):
        self.fuente_video = 0
        self.abrir_fuente_video()

    def usar_camara_ip(self):
        ip = simpledialog.askstring("Cámara IP", "Ingrese la dirección IP de la cámara\n(ej. http://192.168.1.100:8080/video):")
        if ip:
            self.fuente_video = ip
            self.abrir_fuente_video()

    def usar_camara_rtsp(self):
        rtsp = simpledialog.askstring("Cámara RTSP", "Ingrese la URL RTSP de la cámara\n(ej. rtsp://username:password@ip_address:554/stream):")
        if rtsp:
            self.fuente_video = rtsp
            self.abrir_fuente_video()

    def abrir_fuente_video(self):
        if self.video is not None:
            self.video.release()
        self.video = cv2.VideoCapture(self.fuente_video)
        if not self.video.isOpened():
            messagebox.showerror("Error", "No se puede abrir la fuente de video")

    def capturar(self):
        ret, frame = self.video.read()
        if ret:
            ahora = datetime.datetime.now()
            nombre_archivo = ahora.strftime("captura_%Y%m%d_%H%M%S.jpg")
            cv2.imwrite(nombre_archivo, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            messagebox.showinfo("Captura", f"Imagen guardada como '{nombre_archivo}'")

    def actualizar_confianza(self, valor):
        self.umbral_confianza = int(valor) / 100.0

    def actualizar(self):
        ret, frame = self.video.read()
        if ret:
            frame = cv2.resize(frame, (640, 480))
            
            resultados = self.modelo(frame, conf=self.umbral_confianza)
            
            for r in resultados:
                for i, c in enumerate(r.boxes.cls):
                    r.names[int(c)] = 'Rostro'
            
            frame_anotado = resultados[0].plot()
            
            self.agregar_logo(frame_anotado)
            
            self.foto = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame_anotado, cv2.COLOR_BGR2RGB)))
            self.lienzo.create_image(0, 0, image=self.foto, anchor=tk.NW)
        
        self.ventana.after(self.retraso, self.actualizar)

    def agregar_logo(self, frame):
        if self.logo is not None:
            alto, ancho = frame.shape[:2]
            alto_logo, ancho_logo = self.logo.shape[:2]
            
            y_offset = alto - alto_logo - 10
            x_offset = ancho - ancho_logo - 10
            
            if self.logo.shape[2] == 4:
                mascara = self.logo[:, :, 3] / 255.0
                mascara = mascara[:, :, np.newaxis]
                mascara_inv = 1.0 - mascara
                
                logo_bgr = self.logo[:, :, :3]
                roi = frame[y_offset:y_offset+alto_logo, x_offset:x_offset+ancho_logo]
                
                for c in range(0, 3):
                    roi[:, :, c] = roi[:, :, c] * mascara_inv[:, :, 0] + logo_bgr[:, :, c] * mascara[:, :, 0]
                
                frame[y_offset:y_offset+alto_logo, x_offset:x_offset+ancho_logo] = roi
            else:
                frame[y_offset:y_offset+alto_logo, x_offset:x_offset+ancho_logo] = self.logo

raiz = tk.Tk()
app = AplicacionDeteccionRostros(raiz, "Detección de Rostros - Escuela de Robótica Misiones")