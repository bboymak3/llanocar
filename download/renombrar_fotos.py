"""
RENOMBRAR Y CONVERTIR FOTOS A JPG
===================================
Ejecutar en CMD:
  cd E:\Documents\fogo
  python renombrar_fotos.py

Requisito: pip install Pillow
"""
import os
import sys
from PIL import Image

# === CONFIGURACION ===
carpeta_origen  = r'E:\Documents\fogo\foto1'
carpeta_destino = r'E:\Documents\fogo\foto2'
archivo_nombres = r'E:\Documents\fogo\fogo.txt'
# ====================

os.makedirs(carpeta_destino, exist_ok=True)

# Leer nombres del txt
with open(archivo_nombres, 'r', encoding='utf-8') as f:
    nombres = [linea.strip() for linea in f if linea.strip()]

print(f'Nombres cargados: {len(nombres)}')

# Listar imagenes en foto1
ext_validas = ('.jpg', '.jpeg', '.png', '.webp', '.bmp', '.gif', '.tiff', '.jfif')
archivos = sorted([
    a for a in os.listdir(carpeta_origen)
    if os.path.isfile(os.path.join(carpeta_origen, a))
    and a.lower().endswith(ext_validas)
])

print(f'Fotos encontradas: {len(archivos)}')
print('-' * 55)

procesadas = 0
errores = 0
for i, archivo in enumerate(archivos):
    if i >= len(nombres):
        print(f'\nADVERTENCIA: Faltan {len(archivos) - len(nombres)} nombres en fogo.txt')
        break

    nuevo_nombre = nombres[i]
    if not nuevo_nombre.lower().endswith('.jpg'):
        nuevo_nombre = nuevo_nombre.rsplit('.', 1)[0] + '.jpg'

    ruta_origen = os.path.join(carpeta_origen, archivo)
    ruta_destino = os.path.join(carpeta_destino, nuevo_nombre)

    try:
        img = Image.open(ruta_origen)
        if img.mode in ('RGBA', 'LA', 'P'):
            img = img.convert('RGB')
        img.save(ruta_destino, 'JPEG', quality=95, optimize=True)
        img.close()

        kb = os.path.getsize(ruta_destino) / 1024
        print(f'[{i+1:3d}/{min(len(archivos), len(nombres))}] {archivo[:25]:>25} -> {nuevo_nombre[:45]}  ({kb:.0f}KB)')
        procesadas += 1
    except Exception as e:
        print(f'ERROR {archivo}: {e}')
        errores += 1

print('-' * 55)
print(f'HECHO: {procesadas} OK, {errores} errores')
print(f'Destino: {carpeta_destino}')
input('\nPresiona Enter para salir...')
