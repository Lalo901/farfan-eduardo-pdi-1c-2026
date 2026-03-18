# Lab Manifest: Técnicas de Procesamiento Digital de Imágenes 2026

Este manifiesto automatiza la configuración completa del entorno, la estructura de carpetas de la cátedra y la sincronización inicial con GitHub.

## 1. Identidad y Conexión Remota
# Configurar credenciales de Git
git config --global user.name "Lalo901"
git config --global user.email "farfaneduar@gmail.com"

# Inicializar y conectar al repositorio de la cátedra
git init
git remote add origin https://github.com/Lalo901/TecnicaProcesamientoImg.git
git branch -M main

## 2. Entorno Virtual con uv (Python 3.12)
# Inicializar proyecto con la versión estable para 2026
uv init . --python 3.12
uv venv

## [cite_start]3. Instalación de Dependencias [cite: 27, 111-115]
# Herramientas de desarrollo y Notebooks
uv add jupyterlab ipykernel ipywidgets

# Procesamiento de imágenes e IA (Core de la materia)
uv add opencv-python scikit-image py5 matplotlib numpy
uv add tensorflow keras torch torchvision ultralytics diffusers transformers pillow

## [cite_start]4. Estructura de Carpetas del Programa 
# Crear las 18 unidades de la cursada
mkdir -p clases/unidad_{01..18}

# [cite_start]Instancias de Evaluación Obligatorias [cite: 136, 154]
mkdir -p entregas/evaluacion_01_fundamentos    # 29/04
mkdir -p entregas/evaluacion_02_proyecto_final # 30/06

# Repositorios de datos y modelos (Ignorados por Git)
mkdir -p recursos/datasets recursos/pretrained_models

## 5. Configuración de Seguridad (.gitignore)
cat <<EOF > .gitignore
.venv/
__pycache__/
.ipynb_checkpoints/
*.py[cod]
.vscode/
.env

# Bloquear archivos pesados de datasets y modelos
recursos/datasets/
recursos/pretrained_models/
*.h5
*.pt
*.onnx
*.weights
*.yolov8
EOF

## 6. Generación del README.md Profesional
cat <<'EOF' > README.md
# Técnicas de Procesamiento Digital de Imágenes 2026 👁️

Laboratorio de investigación y producción de la carrera de **Ciencia de Datos e Inteligencia Artificial**. [cite: 4]

**Profesor:** Matias Barreto [cite: 4]
**Entorno:** Fedora Linux + uv + Google Colab [cite: 111]

## 🎯 Objetivos
* [cite_start]Comprender la imagen como un artefacto sociotécnico complejo. [cite: 11]
* [cite_start]Implementar soluciones de visión por computadora (CV) contemporáneas. [cite: 13]
* [cite_start]Dominar técnicas desde el procesamiento elemental hasta Modelos Generativos. [cite: 36]

## 📚 Estructura del curso
1. [cite_start]**Unidades 1-6:** Fundamentos, Muestreo, Realce y Métricas. [cite: 45-58]
2. [cite_start]**Unidades 7-11:** Visión Tradicional y Segmentación. [cite: 59-69]
3. [cite_start]**Unidades 12-18:** Deep Learning, CNNs, Transformers, VAEs y Stable Diffusion. [cite: 72-85]

## 🗓️ Fechas de Entrega
* [cite_start]**29/04:** Instancia 1 - Fundamentos. [cite: 136]
* [cite_start]**30/06:** Instancia 2 - Proyecto Integrador Final. [cite: 154]
EOF

## 7. Primer Commit y Despliegue de Estructura
# Crear .gitkeep en carpetas vacías para forzar su subida a GitHub
find clases/ entregas/ recursos/ -type d -exec touch {}/.gitkeep \;

# Sincronizar con el repositorio
git add .
git commit -m "Initial commit: Estructura completa de la cátedra 2026 con README y .gitkeeps"
# El siguiente comando pedirá tu Key/Token en la terminal:
# git push -u origin main
