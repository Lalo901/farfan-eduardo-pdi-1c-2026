# Resumen Técnico: Muestreo y Cuantificación Digital (Unidad 1)

[cite_start]Este documento sintetiza la primera experiencia de laboratorio sobre la **representación de imágenes digitales** como artefactos sociotécnicos complejos[cite: 11, 46].

## 1. Muestreo (Sampling): Discretización Espacial
[cite_start]El muestreo define la **resolución espacial** de la imagen[cite: 46].
* **Concepto:** Es el proceso de capturar muestras de luz en puntos específicos de una grilla ($x, y$).
* **Efecto Observado:** Al reducir el factor de muestreo en el script (ej. de 512px a 51px), la imagen pierde nitidez y aparece el **pixelado** (aliasing).
* [cite_start]**Impacto:** Determina la capacidad del sistema para representar detalles finos del entorno relevante[cite: 23].

## 2. Cuantificación (Quantization): Discretización Tonal
[cite_start]La cuantificación define la **resolución tonal** o de brillo[cite: 46, 49].
* **Concepto:** Es el proceso de asignar un valor numérico finito a la intensidad luminosa de cada píxel.
* **Efecto Observado:** Al reducir los niveles de gris de 256 (8 bits) a solo 4 (2 bits), la imagen pierde gradientes suaves.
* [cite_start]**Impacto:** Produce **falsos contornos**, donde las transiciones de luz se ven como bandas sólidas, afectando la interpretación visual del artefacto cultural[cite: 15].

## 3. Conclusión del Laboratorio
[cite_start]La calidad de la imagen digital no es absoluta; depende de la relación entre el **hardware de captura** y el **software de procesamiento**[cite: 12, 93]. [cite_start]Dominar estos conceptos es el primer paso para proponer soluciones innovadoras en técnicas de visión contemporáneas[cite: 13].

---
[cite_start]**Desarrollado con:** Python 3.12, OpenCV y scikit-image[cite: 27].