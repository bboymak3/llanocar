#!/usr/bin/env python3
"""
Script masivo para agregar enlaces internos a todas las páginas landing de LLANOCAR.
- Agrega al menos 1 enlace interno por párrafo en SEO section
- Convierte service cards en links clickeables
- Llena sección "Related Vehicles" vacía
- Agrega botones internos en secciones de servicios/fotos
"""

import re
import os
import glob
import random
from pathlib import Path

BASE_DIR = "/home/z/my-project"

# Mapeo de servicios base (nombre de display -> archivo html)
SERVICE_PAGES = {
    "Mecánico a Domicilio": "mecanico-a-domicilio.html",
    "Scanner Automotriz": "scanner-automotriz.html",
    "Cambio de Frenos": "cambio-de-frenos.html",
    "Cambio de Pastillas de Freno": "cambio-de-pastillas.html",
    "Cambio de Aceite": "cambio-de-aceite.html",
    "Alineación y Balanceo": "alineacion-y-balanceo.html",
    "Reparación de Motor": "reparacion-de-motor.html",
    "Compresión de Motor": "compresion-de-motor.html",
    "Revisión por Kilometraje": "revision-por-kilometraje.html",
    "Reparación de Embrague": "reparacion-de-embrague.html",
    "Correa de Distribución": "correa-de-distribucion.html",
    "Servicio de Batería": "servicio-de-bateria.html",
    "Suspensión y Dirección": "suspension-y-direccion.html",
    "Electricidad Automotriz": "electricidad-automotriz.html",
    "Cambio de Bujías": "cambio-de-bujias.html",
    "Cambio de Filtros": "cambio-de-filtros.html",
    "Mantención Automotriz": "mantencion-automotriz.html",
    "Mantención a Domicilio": "mantencion-a-domicilio.html",
    "Emergencias Mecánicas": "emergencias-mecanicas.html",
    "Taller Mecánico Cerca": "taller-mecanico-cerca.html",
    "Embragues y Distribución": "embragues-y-distribucion.html",
    "Tren Delantero": "tren-delantero.html",
    "Diagnóstico Automotriz": "diagnostico-automotriz.html",
    "Inspección Mecánica": "inspeccion-mecanica.html",
    "Mecánico de Emergencia": "mecanico-de-emergencia.html",
    "Mecánico para Mujeres": "mecanico-para-mujeres.html",
    "Transmisión Automática": "transmision-automatica.html",
    "Sistema de Enfriamiento": "sistema-de-enfriamiento.html",
    "Reparación de Frenos ABS": "reparacion-de-frenos-abs.html",
    "Revisión Técnica Preventiva": "revision-tecnica-preventiva.html",
    "Taller Mecánico a Domicilio": "taller-mecanico-a-domicilio.html",
    "Servicios a Domicilio": "servicios-domicilio.html",
}

# Mapeo de vehículos
VEHICLE_PAGES = {
    "Nissan Kicks": "vehiculos/nissan-kicks.html",
    "Toyota Corolla": "vehiculos/toyota-corolla.html",
    "Honda Civic": "vehiculos/honda-civic.html",
    "Hyundai Tucson": "vehiculos/hyundai-tucson.html",
    "Chevrolet Sail": "vehiculos/chevrolet-sail.html",
    "Kia Rio": "vehiculos/kia-rio.html",
    "Renault Duster": "vehiculos/renault-duster.html",
    "Ford EcoSport": "vehiculos/ford-ecosport.html",
    "Mazda 3": "vehiculos/mazda-3.html",
    "Toyota Yaris": "vehiculos/toyota-yaris.html",
    "Chevrolet Spark": "vehiculos/chevrolet-spark.html",
    "Suzuki Swift": "vehiculos/suzuki-swift.html",
    "Nissan Versa": "vehiculos/nissan-versa.html",
    "Hyundai Accent": "vehiculos/hyundai-accent.html",
    "Kia Morning": "vehiculos/kia-morning.html",
    "Peugeot 208": "vehiculos/peugeot-208.html",
    "Ford Fiesta": "vehiculos/ford-fiesta.html",
    "Chevrolet Sonic": "vehiculos/chevrolet-sonic.html",
    "Renault Logan": "vehiculos/renault-logan.html",
    "Suzuki Celerio": "vehiculos/suzuki-celerio.html",
    "Honda City": "vehiculos/honda-city.html",
    "Suzuki Baleno": "vehiculos/suzuki-baleno.html",
    "MG 3": "vehiculos/mg-3.html",
    "MG ZS": "vehiculos/mg-zs.html",
    "Mazda CX-5": "vehiculos/mazda-cx-5.html",
    "Honda CR-V": "vehiculos/honda-cr-v.html",
    "Subaru Forester": "vehiculos/subaru-forester.html",
    "Subaru XV": "vehiculos/subaru-xv.html",
    "Peugeot 3008": "vehiculos/peugeot-3008.html",
    "Hyundai Grand i10": "vehiculos/hyundai-grand-i10.html",
    "Fiat Bravo T-Jet": "vehiculos/fiat-bravo-tjet.html",
    "Volkswagen Gol": "vehiculos/volkswagen-gol.html",
}

# Palabras clave en párrafos que se pueden convertir en enlaces
KEYWORD_LINKS = [
    # (patrón regex, archivo html, texto del enlace)
    (r'(?i)\bcambio de aceite\b', 'cambio-de-aceite.html', 'cambio de aceite'),
    (r'(?i)\bcambio de frenos\b', 'cambio-de-frenos.html', 'cambio de frenos'),
    (r'(?i)\bcambio de pastillas\b', 'cambio-de-pastillas.html', 'cambio de pastillas de freno'),
    (r'(?i)\bcambio de buj[ií]as\b', 'cambio-de-bujias.html', 'cambio de bujías'),
    (r'(?i)\bcambio de filtros\b', 'cambio-de-filtros.html', 'cambio de filtros'),
    (r'(?i)\breparaci[oó]n de motor\b', 'reparacion-de-motor.html', 'reparación de motor'),
    (r'(?i)\breparaci[oó]n de embrague\b', 'reparacion-de-embrague.html', 'reparación de embrague'),
    (r'(?i)\bcompresi[oó]n de motor\b', 'compresion-de-motor.html', 'compresión de motor'),
    (r'(?i)\bscanner automotriz\b', 'scanner-automotriz.html', 'scanner automotriz'),
    (r'(?i)\bdiagn[oó]stico automotriz\b', 'diagnostico-automotriz.html', 'diagnóstico automotriz'),
    (r'(?i)\balineaci[oó]n y balanceo\b', 'alineacion-y-balanceo.html', 'alineación y balanceo'),
    (r'(?i)\bcorrea de distribuci[oó]n\b', 'correa-de-distribucion.html', 'correa de distribución'),
    (r'(?i)\bservicio de bater[ií]a\b', 'servicio-de-bateria.html', 'servicio de batería'),
    (r'(?i)\bsuspensi[oó]n y direcci[oó]n\b', 'suspension-y-direccion.html', 'suspensión y dirección'),
    (r'(?i)\belectricidad automotriz\b', 'electricidad-automotriz.html', 'electricidad automotriz'),
    (r'(?i)\bmantenci[oó]n automotriz\b', 'mantencion-automotriz.html', 'mantención automotriz'),
    (r'(?i)\bmantenci[oó]n a domicilio\b', 'mantencion-a-domicilio.html', 'mantención a domicilio'),
    (r'(?i)\bemergencias mec[aá]nicas\b', 'emergencias-mecanicas.html', 'emergencias mecánicas'),
    (r'(?i)\bmec[aá]nico a domicilio\b', 'mecanico-a-domicilio.html', 'mecánico a domicilio'),
    (r'(?i)\btaller mec[aá]nico cerca\b', 'taller-mecanico-cerca.html', 'taller mecánico cerca'),
    (r'(?i)\brevision por kilometraje\b', 'revision-por-kilometraje.html', 'revisión por kilometraje'),
    (r'(?i)\brevision t[eé]cnica\b', 'revision-tecnica-preventiva.html', 'revisión técnica preventiva'),
    (r'(?i)\binspecci[oó]n mec[aá]nica\b', 'inspeccion-mecanica.html', 'inspección mecánica'),
    (r'(?i)\btren delantero\b', 'tren-delantero.html', 'tren delantero'),
    (r'(?i)\btransmisi[oó]n autom[aá]tica\b', 'transmision-automatica.html', 'transmisión automática'),
    (r'(?i)\bsistema de enfriamiento\b', 'sistema-de-enfriamiento.html', 'sistema de enfriamiento'),
    (r'(?i)\bfrenos abs\b', 'reparacion-de-frenos-abs.html', 'frenos ABS'),
    (r'(?i)\bembragues y distribuci[oó]n\b', 'embragues-y-distribucion.html', 'embragues y distribución'),
]

# Palabras clave de vehículos para enlaces en párrafos
VEHICLE_KEYWORDS = [
    (r'(?i)\bNissan Kicks\b', 'vehiculos/nissan-kicks.html', 'Nissan Kicks'),
    (r'(?i)\bToyota Corolla\b', 'vehiculos/toyota-corolla.html', 'Toyota Corolla'),
    (r'(?i)\bHonda Civic\b', 'vehiculos/honda-civic.html', 'Honda Civic'),
    (r'(?i)\bHyundai Tucson\b', 'vehiculos/hyundai-tucson.html', 'Hyundai Tucson'),
    (r'(?i)\bChevrolet Sail\b', 'vehiculos/chevrolet-sail.html', 'Chevrolet Sail'),
    (r'(?i)\bKia Rio\b', 'vehiculos/kia-rio.html', 'Kia Rio'),
    (r'(?i)\bRenault Duster\b', 'vehiculos/renault-duster.html', 'Renault Duster'),
    (r'(?i)\bFord EcoSport\b', 'vehiculos/ford-ecosport.html', 'Ford EcoSport'),
    (r'(?i)\bMazda 3\b', 'vehiculos/mazda-3.html', 'Mazda 3'),
    (r'(?i)\bToyota Yaris\b', 'vehiculos/toyota-yaris.html', 'Toyota Yaris'),
    (r'(?i)\bChevrolet Spark\b', 'vehiculos/chevrolet-spark.html', 'Chevrolet Spark'),
    (r'(?i)\bSuzuki Swift\b', 'vehiculos/suzuki-swift.html', 'Suzuki Swift'),
    (r'(?i)\bNissan Versa\b', 'vehiculos/nissan-versa.html', 'Nissan Versa'),
    (r'(?i)\bHyundai Accent\b', 'vehiculos/hyundai-accent.html', 'Hyundai Accent'),
    (r'(?i)\bKia Morning\b', 'vehiculos/kia-morning.html', 'Kia Morning'),
    (r'(?i)\bPeugeot 208\b', 'vehiculos/peugeot-208.html', 'Peugeot 208'),
    (r'(?i)\bFord Fiesta\b', 'vehiculos/ford-fiesta.html', 'Ford Fiesta'),
    (r'(?i)\bChevrolet Sonic\b', 'vehiculos/chevrolet-sonic.html', 'Chevrolet Sonic'),
    (r'(?i)\bRenault Logan\b', 'vehiculos/renault-logan.html', 'Renault Logan'),
    (r'(?i)\bSuzuki Celerio\b', 'vehiculos/suzuki-celerio.html', 'Suzuki Celerio'),
    (r'(?i)\bHonda City\b', 'vehiculos/honda-city.html', 'Honda City'),
    (r'(?i)\bSuzuki Baleno\b', 'vehiculos/suzuki-baleno.html', 'Suzuki Baleno'),
    (r'(?i)\bMG ZS\b', 'vehiculos/mg-zs.html', 'MG ZS'),
    (r'(?i)\bMazda CX-5\b', 'vehiculos/mazda-cx-5.html', 'Mazda CX-5'),
    (r'(?i)\bHonda CR-V\b', 'vehiculos/honda-cr-v.html', 'Honda CR-V'),
    (r'(?i)\bSubaru Forester\b', 'vehiculos/subaru-forester.html', 'Subaru Forester'),
    (r'(?i)\bSubaru XV\b', 'vehiculos/subaru-xv.html', 'Subaru XV'),
    (r'(?i)\bPeugeot 3008\b', 'vehiculos/peugeot-3008.html', 'Peugeot 3008'),
    (r'(?i)\bHyundai Grand i10\b', 'vehiculos/hyundai-grand-i10.html', 'Hyundai Grand i10'),
    (r'(?i)\bFiat Bravo\b', 'vehiculos/fiat-bravo-tjet.html', 'Fiat Bravo T-Jet'),
    (r'(?i)\bVolkswagen Gol\b', 'vehiculos/volkswagen-gol.html', 'Volkswagen Gol'),
    (r'(?i)\bMG 3\b', 'vehiculos/mg-3.html', 'MG 3'),
]

def get_service_name_from_file(filename):
    """Extrae el nombre del servicio del nombre de archivo"""
    name = filename.replace('.html', '').replace('-', ' ').title()
    return name

def get_related_services(current_file):
    """Obtiene servicios relacionados excluyendo el actual"""
    current_service = Path(current_file).stem
    related = {}
    for name, href in SERVICE_PAGES.items():
        target = Path(href).stem
        if target != current_service and target != 'index':
            related[name] = href
    return related

def get_related_vehicles(current_file):
    """Obtiene vehículos relacionados al servicio actual"""
    with open(current_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    found = {}
    for pattern, href, name in VEHICLE_KEYWORDS:
        if re.search(pattern, content):
            found[name] = href
    
    # Si no encontramos vehículos en el contenido, devolver algunos aleatorios
    if len(found) < 3:
        all_vehicles = list(VEHICLE_PAGES.items())
        random.shuffle(all_vehicles)
        for name, href in all_vehicles:
            if name not in found:
                found[name] = href
            if len(found) >= 6:
                break
    
    return dict(list(found.items())[:8])

def add_links_to_paragraphs(content, current_file):
    """Agrega al menos 1 enlace interno por párrafo en la sección SEO"""
    current_service = Path(current_file).stem
    
    # Encontrar la sección SEO main (entre <!-- SEO MAIN SECTION --> y <!-- SERVICES LIST -->)
    seo_match = re.search(r'(<!-- SEO MAIN SECTION -->.*?)(<!-- SERVICES LIST -->)', content, re.DOTALL)
    if not seo_match:
        return content, 0
    
    seo_section = seo_match.group(1)
    links_added = 0
    
    # Procesar cada párrafo
    paragraphs = re.finditer(r'(<p>)(.*?)(</p>)', seo_section, re.DOTALL)
    
    for p_match in paragraphs:
        p_open = p_match.group(1)
        p_content = p_match.group(2)
        p_close = p_match.group(3)
        
        # Verificar si ya tiene un enlace interno
        if re.search(r'<a\s+href=["\'][^"\']*\.html["\']', p_content):
            continue
        
        # Intentar agregar un enlace de servicio
        new_p_content = p_content
        linked = False
        
        for pattern, href, link_text in KEYWORD_LINKS:
            if re.search(pattern, p_content):
                # No enlazar a la misma página
                target_stem = Path(href).stem
                if target_stem == current_service:
                    continue
                # No enlazar si ya hay un <a> que contenga esta palabra
                if re.search(r'<a[^>]*>' + re.escape(link_text), p_content, re.IGNORECASE):
                    continue
                
                new_p_content = re.sub(
                    pattern,
                    f'<a href="{href}" style="color:var(--primary);text-decoration:underline;font-weight:600;">{link_text}</a>',
                    new_p_content,
                    count=1,
                    flags=re.IGNORECASE
                )
                links_added += 1
                linked = True
                break
        
        # Si no se encontró keyword de servicio, intentar vehículo
        if not linked:
            for pattern, href, link_text in VEHICLE_KEYWORDS:
                if re.search(pattern, p_content):
                    if re.search(r'<a[^>]*>' + re.escape(link_text), p_content, re.IGNORECASE):
                        continue
                    new_p_content = re.sub(
                        pattern,
                        f'<a href="{href}" style="color:var(--primary);text-decoration:underline;font-weight:600;">{link_text}</a>',
                        new_p_content,
                        count=1,
                        flags=re.IGNORECASE
                    )
                    links_added += 1
                    linked = True
                    break
        
        # Si aún no se encontró nada, agregar enlace a mecanico-a-domicilio o index
        if not linked and current_service != 'mecanico-a-domicilio':
            # Buscar "LLANOCAR Servicios Automotrices" o "LLANOCAR Automotriz" y agregar enlace a index
            if 'LLANOCAR' in p_content and 'href=' not in new_p_content:
                new_p_content = new_p_content.replace(
                    'LLANOCAR Servicios Automotrices',
                    '<a href="index.html" style="color:var(--primary);font-weight:600;">LLANOCAR Servicios Automotrices</a>',
                    1
                )
                if new_p_content == p_content:
                    new_p_content = new_p_content.replace(
                        'LLANOCAR Automotriz',
                        '<a href="index.html" style="color:var(--primary);font-weight:600;">LLANOCAR Automotriz</a>',
                        1
                    )
                links_added += 1
        
        if new_p_content != p_content:
            seo_section = seo_section.replace(
                p_open + p_content + p_close,
                p_open + new_p_content + p_close,
                1
            )
    
    # Reemplazar en el contenido original
    new_content = content.replace(
        seo_match.group(1),
        seo_section,
        1
    )
    
    return new_content, links_added

def make_service_cards_clickable(content, current_file):
    """Convierte los service cards en links clickeables"""
    current_service = Path(current_file).stem
    
    # Buscar los service cards: h3 dentro de divs con border-left/right
    # Patrón: <h3 class="fw-bold mb-0"...>Nombre del Servicio</h3>
    def replace_service_card(match):
        h3_tag = match.group(0)
        service_name = match.group(1)
        
        # Buscar el archivo correspondiente
        for display_name, href in SERVICE_PAGES.items():
            if display_name.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ñ', 'n') == service_name.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ñ', 'n'):
                target_stem = Path(href).stem
                if target_stem != current_service:
                    return f'<h3 class="fw-bold mb-0" style="color:#333;font-size:1.1rem;"><a href="{href}" style="color:inherit;text-decoration:none;">{service_name}</a></h3>'
                break
        
        return h3_tag
    
    # Buscar h3 dentro de service cards
    new_content = re.sub(
        r'<h3 class="fw-bold mb-0" style="color:#333;font-size:1\.1rem;">(.*?)</h3>',
        replace_service_card,
        content
    )
    
    cards_changed = 0
    if new_content != content:
        cards_changed = content.count('<h3 class="fw-bold mb-0"') - new_content.count('<h3 class="fw-bold mb-0"')
    
    return new_content, cards_changed

def fill_vehicles_section(content, current_file):
    """Llena la sección vacía 'Related Vehicles' con enlaces"""
    related_vehicles = get_related_vehicles(current_file)
    
    if not related_vehicles:
        return content, 0
    
    # Buscar la sección vacía de Related Vehicles
    pattern = r'(<!-- CROSS-LINKS: Related Vehicles -->)\s*\n'
    match = re.search(pattern, content)
    
    if not match:
        return content, 0
    
    # Verificar si ya tiene contenido
    after_marker = content[match.end():]
    if re.match(r'\s*<section', after_marker):
        return content, 0  # Ya tiene sección con contenido
    
    # Generar los badges de vehículos
    vehicle_badges = []
    vehicle_icons = {
        'Nissan': 'fa-car', 'Toyota': 'fa-car', 'Honda': 'fa-car',
        'Hyundai': 'fa-car', 'Chevrolet': 'fa-car', 'Kia': 'fa-car',
        'Renault': 'fa-car', 'Ford': 'fa-car', 'Mazda': 'fa-car',
        'Suzuki': 'fa-car', 'Peugeot': 'fa-car', 'MG': 'fa-car',
        'Subaru': 'fa-car', 'Fiat': 'fa-car', 'Volkswagen': 'fa-car',
    }
    
    for name, href in related_vehicles.items():
        brand = name.split()[0]
        icon = vehicle_icons.get(brand, 'fa-car')
        vehicle_badges.append(f'<a href="{href}" class="badge bg-secondary text-decoration-none m-1 p-2"><i class="fas {icon} me-1"></i>{name}</a>')
    
    vehicles_section = f'''<section class="section-dark">
<div class="container">
  <h2><i class="fas fa-car me-2"></i>Vehículos que Atendemos</h2>
  <p class="subtitle" style="color:#999;">Conoce los vehículos para los que ofrecemos este servicio</p>
  <div class="text-center">{''.join(vehicle_badges)}
</div>
</div>
</section>
'''
    
    new_content = content[:match.end()] + '\n' + vehicles_section + content[match.end():]
    
    return new_content, len(related_vehicles)

def add_internal_buttons_to_sections(content, current_file):
    """Agrega botones con enlaces internos en la sección de servicios listados"""
    current_service = Path(current_file).stem
    
    # Buscar la sección "Servicios Relacionados" y agregar botones
    services_section = re.search(
        r'(<!-- SERVICES LIST -->.*?<h2><i class="fas fa-tools me-2"></i>Servicios Relacionados</h2>\s*<p class="subtitle">.*?</p>)',
        content, re.DOTALL
    )
    
    if not services_section:
        return content, 0
    
    # Verificar si ya tiene botones internos después del subtítulo
    after_subtitle = content[services_section.end():]
    if re.search(r'btn-call.*href=["\'][^"\']*\.html', after_subtitle[:500]):
        return content, 0  # Ya tiene botones internos
    
    # Agregar una fila de botones internos después del subtítulo
    related = get_related_services(current_file)
    selected = list(related.items())[:4]
    
    if not selected:
        return content, 0
    
    buttons_html = '\n  <div class="d-flex flex-wrap justify-content-center gap-2 mb-4">\n'
    for name, href in selected:
        buttons_html += f'    <a href="{href}" class="btn btn-sm btn-outline-dark" style="border-radius:50px;font-size:.85rem;padding:6px 16px;"><i class="fas fa-wrench me-1"></i>{name}</a>\n'
    buttons_html += '  </div>'
    
    insert_pos = services_section.end()
    new_content = content[:insert_pos] + buttons_html + content[insert_pos:]
    
    return new_content, len(selected)

def add_see_more_service_button(content, current_file):
    """Agrega un botón 'Ver más servicios' al final de la sección de servicios"""
    current_service = Path(current_file).stem
    
    # Buscar el cierre de la sección "Services List"
    services_end = re.search(
        r'(</div>\s*</div>\s*</section>\s*)(<!-- WHY CHOOSE US -->)',
        content, re.DOTALL
    )
    
    if not services_end:
        return content
    
    # Buscar si ya tiene un enlace a más servicios
    section_content = content[:services_end.start()]
    if 'Ver Todos los Servicios' in section_content:
        return content
    
    button_html = '''  <div class="text-center mt-4">
    <a href="index.html#servicios" class="btn-call" style="font-size:.95rem;padding:10px 24px;"><i class="fas fa-th-list me-2"></i>Ver Todos los Servicios</a>
  </div>
'''
    
    new_content = content[:services_end.start()] + button_html + content[services_end.start():]
    return new_content

def process_landing_page(filepath):
    """Procesa una página landing individual"""
    print(f"  Procesando: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    total_links = 0
    
    # 1. Agregar enlaces a párrafos SEO
    content, n = add_links_to_paragraphs(content, filepath)
    total_links += n
    if n > 0:
        print(f"    ✓ {n} enlaces en párrafos SEO")
    
    # 2. Hacer service cards clickeables
    content, n = make_service_cards_clickable(content, filepath)
    total_links += n
    if n > 0:
        print(f"    ✓ {n} service cards clickeables")
    
    # 3. Llenar sección Related Vehicles
    content, n = fill_vehicles_section(content, filepath)
    total_links += n
    if n > 0:
        print(f"    ✓ {n} vehículos relacionados agregados")
    
    # 4. Agregar botones internos a sección de servicios
    content, n = add_internal_buttons_to_sections(content, filepath)
    total_links += n
    if n > 0:
        print(f"    ✓ {n} botones internos en servicios")
    
    # 5. Agregar botón "Ver más servicios"
    content = add_see_more_service_button(content, filepath)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"    Total: {total_links} enlaces agregados")
    else:
        print(f"    (sin cambios necesarios)")
    
    return content != original

def main():
    # Excluir estos archivos
    exclude = {'index.html', 'contacto.html', 'faq.html', 'quienes-somos.html',
               'politica-privacidad.html', 'google7a5c4682e9b25d4f.html'}
    
    # Obtener todas las páginas landing
    html_files = sorted(glob.glob(os.path.join(BASE_DIR, '*.html')))
    landing_pages = [f for f in html_files if Path(f).name not in exclude]
    
    print(f"Total de páginas landing a procesar: {len(landing_pages)}")
    print("=" * 60)
    
    changed = 0
    for filepath in landing_pages:
        if process_landing_page(filepath):
            changed += 1
    
    print("=" * 60)
    print(f"Páginas modificadas: {changed}/{len(landing_pages)}")

if __name__ == '__main__':
    main()
