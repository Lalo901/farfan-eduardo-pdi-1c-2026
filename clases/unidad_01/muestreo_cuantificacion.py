import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import data  # Usamos el dataset oficial de la librería

def lab_unidad_1():
    # 1. Carga de imagen estándar (Cameraman es ideal para ver bordes y tonos)
    # Representación de imagen digital 
    img = data.camera() 

    # --- MUESTREO (Sampling: Resolución Espacial)  ---
    # Reducimos la cantidad de píxeles para ver el efecto de pixelado
    factor = 10 
    h, w = img.shape
    img_muestreada = cv2.resize(img, (w // factor, h // factor), interpolation=cv2.INTER_NEAREST)
    # Re-escalamos al tamaño original para comparar visualmente
    img_pixelada = cv2.resize(img_muestreada, (w, h), interpolation=cv2.INTER_NEAREST)

    # --- CUANTIFICACIÓN (Quantization: Resolución Tonal)  ---
    # Reducimos los niveles de gris (de 256 a solo 4 niveles)
    niveles = 4
    # Aplicamos la fórmula de discretización
    img_cuantificada = (img // (256 // niveles)) * (256 // niveles)

    # --- VISUALIZACIÓN ---
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.title("Original (8-bits / 256 niveles)")
    plt.imshow(img, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title(f"Muestreo (Reducción {factor}x)")
    plt.imshow(img_pixelada, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title(f"Cuantificación ({niveles} niveles de gris)")
    plt.imshow(img_cuantificada, cmap='gray')
    plt.axis('off')

    plt.suptitle("Unidad 1: Muestreo y Cuantificación Digital", fontsize=16)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    lab_unidad_1()