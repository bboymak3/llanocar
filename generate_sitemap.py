#!/usr/bin/env python3
"""Generar sitemap.xml completo para LLANOCAR"""
import os
import glob
from datetime import datetime

BASE_URL = "https://llanocar.pages.dev"
BASE_DIR = "/home/z/my-project/llanocar"
TODAY = datetime.now().strftime("%Y-%m-%d")

urls = []

# 1. Root HTML files (including 200 new landing pages)
for f in sorted(glob.glob(os.path.join(BASE_DIR, "*.html"))):
    fname = os.path.basename(f)
    if fname.startswith("google") or fname == "google7a5c4682e9b25d4f.html":
        continue
    urls.append(f"{BASE_URL}/{fname}")

# 2. Comunas
for f in sorted(glob.glob(os.path.join(BASE_DIR, "comunas", "*.html"))):
    fname = os.path.basename(f)
    urls.append(f"{BASE_URL}/comunas/{fname}")

# 3. Vehículos
for f in sorted(glob.glob(os.path.join(BASE_DIR, "vehiculos", "*.html"))):
    fname = os.path.basename(f)
    urls.append(f"{BASE_URL}/vehiculos/{fname}")

# 4. Marcas automotrices
for f in sorted(glob.glob(os.path.join(BASE_DIR, "marcas_automotrices", "*.html"))):
    fname = os.path.basename(f)
    urls.append(f"{BASE_URL}/marcas_automotrices/{fname}")

# 5. Blog
for f in sorted(glob.glob(os.path.join(BASE_DIR, "blog", "*.html"))):
    fname = os.path.basename(f)
    urls.append(f"{BASE_URL}/blog/{fname}")

# Write sitemap
sitemap_path = os.path.join(BASE_DIR, "sitemap.xml")
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for url in urls:
        f.write(f'  <url>\n')
        f.write(f'    <loc>{url}</loc>\n')
        f.write(f'    <lastmod>{TODAY}</lastmod>\n')
        f.write(f'    <changefreq>monthly</changefreq>\n')
        f.write(f'    <priority>0.8</priority>\n')
        f.write(f'  </url>\n')
    f.write('</urlset>\n')

print(f"Sitemap generado: {sitemap_path}")
print(f"Total URLs: {len(urls)}")
print(f"  Root: {len(glob.glob(os.path.join(BASE_DIR, '*.html')))}")
print(f"  Comunas: {len(glob.glob(os.path.join(BASE_DIR, 'comunas', '*.html')))}")
print(f"  Vehículos: {len(glob.glob(os.path.join(BASE_DIR, 'vehiculos', '*.html')))}")
print(f"  Marcas: {len(glob.glob(os.path.join(BASE_DIR, 'marcas_automotrices', '*.html')))}")
print(f"  Blog: {len(glob.glob(os.path.join(BASE_DIR, 'blog', '*.html')))}")
