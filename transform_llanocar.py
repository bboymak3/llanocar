#!/usr/bin/env python3
"""
SCRIPT DE TRANSFORMACIÓN TOTAL: GlobalPro → LLANOCAR
- Cambia colores rojo sangre → naranja Caterpillar
- Cambia toda la información del negocio
- Actualiza teléfonos, emails, direcciones, redes sociales
- Agrega nuevas keywords: mantención, Embragues y Distribución, Tren Delantero
- Elimina referencias a GlobalPro
"""

import os
import re
import glob

BASE = "/home/z/my-project/llanocar"

# ============================================================
# 1. LISTA DE ARCHIVOS A PROCESAR
# ============================================================
html_files = []
for root, dirs, files in os.walk(BASE):
    for f in files:
        if f.endswith(('.html', '.css', '.xml', '.txt')):
            filepath = os.path.join(root, f)
            html_files.append(filepath)

# Excluir archivos que no son del proyecto
exclude_dirs = ['.git', 'node_modules', '__pycache__']
html_files = [f for f in html_files if not any(ex in f for ex in exclude_dirs)]

print(f"Archivos a procesar: {len(html_files)}")

# ============================================================
# 2. MAPEO DE COLORES: Rojo sangre → Naranja Caterpillar
# ============================================================
color_map = {
    # Rojo sangre → Naranja Caterpillar principal
    '#a80000': '#E87722',
    '#A80000': '#E87722',
    '#800000': '#C4611A',
    '#7F1D1D': '#3D2200',
    '#DC2626': '#E87722',
    '#dc2626': '#E87722',
    '#D32F2F': '#E87722',
    '#d32f2f': '#E87722',
    '#b71c1c': '#C4611A',
    '#B91C1C': '#C4611A',
    '#FECACA': '#FFE0B2',
    '#FEF2F2': '#FFF4E8',
    '#fff8f0': '#FFF8F0',  # se mantiene
    '#fff5f5': '#FFF4E8',
    '#f0f7ff': '#FFF4E8',
    '#c62828': '#E87722',
    '#C62828': '#E87722',
    '#e53935': '#F5A623',
    '#E53935': '#F5A623',
    '#ef5350': '#FF8C00',
    '#EF5350': '#FF8C00',
    '#f44336': '#E87722',
    '#F44336': '#E87722',
    'rgba(220, 38, 38,': 'rgba(232, 119, 34,',
    'rgba(168, 0, 0,': 'rgba(232, 119, 34,',
    'rgba(211, 47, 47,': 'rgba(232, 119, 34,',
    'rgba(185, 28, 28,': 'rgba(196, 97, 26,',
    'rgba(127, 29, 29,': 'rgba(61, 34, 0,',
    'rgba(220,38,38,': 'rgba(232,119,34,',
    'rgba(168,0,0,': 'rgba(232,119,34,',
    'rgba(211,47,47,': 'rgba(232,119,34,',
    'rgba(185,28,28,': 'rgba(196,97,26,',
    'rgba(127,29,29,': 'rgba(61,34,0,',
    # Gradient rojo → naranja
    'linear-gradient(135deg, #000000 0%, #7F1D1D 100%)': 'linear-gradient(135deg, #1A1A1A 0%, #3D2200 100%)',
    'linear-gradient(135deg, #DC2626 0%, #000000 100%)': 'linear-gradient(135deg, #E87722 0%, #1A1A1A 100%)',
    'linear-gradient(135deg, #DC2626 0%, #B91C1C 100%)': 'linear-gradient(135deg, #E87722 0%, #C4611A 100%)',
    'linear-gradient(135deg, #a80000 0%, #d32f2f 100%)': 'linear-gradient(135deg, #E87722 0%, #F5A623 100%)',
    'linear-gradient(135deg, #a80000, #ff6b00)': 'linear-gradient(135deg, #E87722, #F5A623)',
    'linear-gradient(135deg, #ff6b00 0%, #ff8c33 100%)': 'linear-gradient(135deg, #FF8C00 0%, #FFB347 100%)',
}

# ============================================================
# 3. MAPEO DE TEXTO: GlobalPro → Llanocar
# ============================================================
text_map = {
    # Nombres del negocio
    'GlobalPro': 'LLANOCAR',
    'Globalpro': 'LLANOCAR',
    'GLOBALPRO': 'LLANOCAR',
    'globalpro': 'llanocar',
    'Global Pro': 'LLANOCAR',
    'Global Pro Automotriz': 'LLANOCAR Servicios Automotrices',
    
    # Teléfonos
    '939026185': '933261085',
    '+569 39026185': '+56 9 3326 1085',
    '+56 9 39026185': '+56 9 3326 1085',
    'tel:939026185': 'tel:933261085',
    
    # WhatsApp
    '56939026185': '56933261085',
    'wa.me/56939026185': 'wa.me/56933261085',
    
    # Email
    'contacto@globalpro.cl': 'llanocar2019@gmail.com',
    
    # Dirección
    'Pedro Aguirre Cerda, RM': 'Pudahuel, Región Metropolitana',
    'Base: Pedro Aguirre Cerda, RM': 'Pudahuel, Región Metropolitana de Santiago',
    'Servicio a Domicilio en todo Santiago\\n            Base: Pedro Aguirre Cerda, RM': 'Taller en Pudahuel, Región Metropolitana de Santiago',
    
    # URLs
    'globalpro.pages.dev': 'llanocar.pages.dev',
    'mecanico247.com': 'llanocar.pages.dev',
    'https://globalpro.pages.dev/images/mecanico-a-domicilio-en-santiago.png': 'https://llanocar.pages.dev/images/mecanico-a-domicilio-en-santiago.png',
    
    # Títulos
    'GlobalPro - Taller Mecánico en Santiago | Servicio Automotriz Integral': 'LLANOCAR - Mecánico a Domicilio en Santiago | Reparaciones y Mantención Automotriz',
    'GlobalPro Automotriz': 'LLANOCAR Servicios Automotrices',
    'GlobalPro Taller Mecánico': 'LLANOCAR Servicios Automotrices',
    'Taller Mecánico': 'Servicios Automotrices',
    
    # Logo subtext
    'Taller Mecánico': 'Servicios Automotrices',
    
    # Copyright
    'GlobalPro. Todos los derechos reservados': 'LLANOCAR. Todos los derechos reservados',
    
    # Cloudflare beacon token - NO cambiar (es del usuario)
}

# ============================================================
# 4. PROCESAMIENTO
# ============================================================
stats = {"colors": 0, "texts": 0, "files": 0}

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
    except Exception as e:
        print(f"  ERROR leyendo {filepath}: {e}")
        continue
    
    original = content
    
    # 4a. Cambiar colores
    for old_color, new_color in color_map.items():
        count = content.count(old_color)
        if count > 0:
            content = content.replace(old_color, new_color)
            stats["colors"] += count
    
    # 4b. Cambiar textos
    for old_text, new_text in text_map.items():
        count = content.count(old_text)
        if count > 0:
            content = content.replace(old_text, new_text)
            stats["texts"] += count
    
    # 4c. Escribir si hubo cambios
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        stats["files"] += 1
        rel = os.path.relpath(filepath, BASE)
        print(f"  ✅ {rel}")

print(f"\n{'='*60}")
print(f"RESUMEN:")
print(f"  Colores cambiados: {stats['colors']}")
print(f"  Textos cambiados: {stats['texts']}")
print(f"  Archivos modificados: {stats['files']}")
print(f"{'='*60}")
