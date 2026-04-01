import py5
from skimage import data, img_as_ubyte
import cv2
import numpy as np

# Variables globales
img_rgb = None
final_py5_img = None

def setup():
    global img_rgb
    py5.size(451, 300)  # Dimensiones exactas de data.chelsea() que trae skimage
    py5.window_title("Unidad 2: Opacidad Interactiva - Gris Claro/Oscuro")

    # Cargar la imagen original en color y asegurar que sea de 8 bits (2^8 = 256 valores (del 0 al 255).)
    img_rgb = img_as_ubyte(data.chelsea())

def draw():
    global final_py5_img
    # Limitar el mouse_x para que no se salga de los bordes y se mantenga dentro del lienzo o canvas
    mx = py5.constrain(py5.mouse_x, 0, py5.width)
    center_x = py5.width / 2

    # Calcular el factor de mezcla 'alpha' [0, 1] y 'dirección' [-1, 1]
    # d es la distancia normalizada del centro [-1, 1]
    # d = -1 (borde izquierdo), d = 0 (centro), d = 1 (borde derecho)
    d = (mx - center_x) / center_x
    alpha = abs(d) # Cuán gris debe ser la imagen (de 0 a 1)
    
    # Crear una copia de la imagen original para manipularla
    img_copia = img_rgb.copy()

    # Crear versión en escala de grises para el cálculo (300, 451, 1)
    img_gray = cv2.cvtColor(img_copia, cv2.COLOR_RGB2GRAY)
    
    #  Izquierda (Gris Claro) y Derecha (Gris Oscuro)
    if d > 0:
        # Mouse a la Derecha: Opaca con Gris Oscuro (multiplicamos el gris original por 0.5)
        # Necesitamos que img_gray sea de 3 canales para mezclar con Color
        gray_target = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB)
        gray_target = (gray_target * 0.5).astype(np.uint8)
    else:
        # Mouse a la Izquierda: Opacar con Gris Claro (multiplicamos el gris por 1.5, clip a 255)
        gray_target = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB)
        # Usamos clip para no pasarnos de 255
        gray_target = np.clip((gray_target * 1.5).astype(np.uint16), 0, 255).astype(np.uint8)

    # mezcla Lineal Vectorizada usando NumPy: 
    # imagen_final = Color * (1-alpha) + GrisTarget * alpha
    img_mezclada = (img_copia * (1.0 - alpha) + gray_target * alpha).astype(np.uint8)
    
    #Convertir RGB (3 canales) a RGBA (4 canales) para py5 (para evitar el ValueError)
    img_rgba = cv2.cvtColor(img_mezclada, cv2.COLOR_RGB2RGBA)
    
    # Convertir el array de NumPy a imagen de py5 y mostrar
    final_py5_img = py5.create_image_from_numpy(img_rgba)
    py5.image(final_py5_img, 0, 0)

    # texto informativo en pantalla
    py5.fill(255)
    py5.text_size(16)
    lado_texto = "Derecha (Gris Oscuro)" if d > 0 else "Izquierda (Gris Claro)"
    if alpha < 0.02: lado_texto = "Centro (Color Original)"
    py5.text(f"Mezcla: {alpha:.2f} - Lado: {lado_texto}", 15, 25)

if __name__ == "__main__":
    py5.run_sketch()