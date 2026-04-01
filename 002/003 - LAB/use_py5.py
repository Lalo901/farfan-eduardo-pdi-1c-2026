import py5
from skimage import data, img_as_ubyte
import cv2

# Variables globales
img_original = None
py5_img = None

def setup():
    global img_original
    # Chelsea tiene 300 de alto por 451 de ancho
    py5.size(451, 300)  
    py5.window_title("Unidad 2: Cuantización Interactiva")
    
    # Cargar imagen (Devuelve shape: 300, 451, 3)
    img_original = img_as_ubyte(data.chelsea())

def draw():
    global py5_img
    
    # 1. Mapear la posición X del mouse a niveles de color (2 a 64)
    niveles = int(py5.remap(py5.mouse_x, 0, py5.width, 2, 64))
    niveles = max(2, niveles) # Evitar división por cero
    
    # 2. Cuantización (Reducción de colores)
    factor = 256 // niveles
    img_cuantizada = (img_original // factor) * factor
    
    # 3. SOLUCIÓN AL ERROR: Convertir RGB (3 canales) a RGBA (4 canales)
    img_rgba = cv2.cvtColor(img_cuantizada, cv2.COLOR_RGB2RGBA)
    
    # 4. Crear imagen py5 y mostrarla
    py5_img = py5.create_image_from_numpy(img_rgba)
    py5.image(py5_img, 0, 0)
    
    # 5. Texto en pantalla
    py5.fill(255)
    py5.text_size(16)
    py5.text(f"Niveles de color: {niveles}", 15, 25)

if __name__ == "__main__":
    py5.run_sketch()