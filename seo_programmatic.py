#!/usr/bin/env python3
"""
SEO Programático para LlanoCar (repo bboymak3/llanocar en commit 95f7184).
Actualiza Meta Titles, Meta Descriptions y Schema JSON-LD en 358 HTML.

REGLAS:
- SIN nombre de marca ("LlanoCar", "LLANOCAR") en titles ni descriptions
- Fórmulas exactas:
  * Comunas: "Mecánico a domicilio en [Comuna] | 24/7"
  * Servicios: "[Servicio] a domicilio en Santiago | En sitio"
  * Vehículos: "Mecánico a domicilio para [Marca Modelo] | Santiago"
  * Combinaciones: "[Servicio] para [Marca Modelo] en [Comuna]"
- Title máx 60 chars
- Description 120-155 chars con emojis y CTA teléfono
- Schema JSON-LD @type AutoRepair con todas las props
"""
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent

# Catálogos
COMUNAS = {
    "alhue": "Alhué", "buin": "Buin", "calera-de-tango": "Calera de Tango",
    "cerrillos": "Cerrillos", "cerro-navia": "Cerro Navia", "colina": "Colina",
    "conchali": "Conchalí", "curacavi": "Curacaví", "el-bosque": "El Bosque",
    "el-monte": "El Monte", "estacion-central": "Estación Central",
    "huechuraba": "Huechuraba", "independencia": "Independencia",
    "isla-de-maipo": "Isla de Maipo", "la-cisterna": "La Cisterna",
    "la-florida": "La Florida", "la-granja": "La Granja",
    "la-pintana": "La Pintana", "la-reina": "La Reina", "lampa": "Lampa",
    "las-condes": "Las Condes", "lo-barnechea": "Lo Barnechea",
    "lo-espejo": "Lo Espejo", "lo-prado": "Lo Prado", "macul": "Macul",
    "maipu": "Maipú", "maria-pinto": "María Pinto", "melipilla": "Melipilla",
    "nunoa": "Ñuñoa", "padre-hurtado": "Padre Hurtado", "paine": "Paine",
    "pedro-aguirre-cerda": "Pedro Aguirre Cerda", "penaflor": "Peñaflor",
    "penalolen": "Peñalolén", "pirque": "Pirque", "providencia": "Providencia",
    "pudahuel": "Pudahuel", "puente-alto": "Puente Alto", "quilicura": "Quilicura",
    "quinta-normal": "Quinta Normal", "recoleta": "Recoleta", "renca": "Renca",
    "san-bernardo": "San Bernardo", "san-joaquin": "San Joaquín",
    "san-jose-de-maipo": "San José de Maipo", "san-miguel": "San Miguel",
    "san-pedro": "San Pedro", "san-ramon": "San Ramón", "santiago": "Santiago",
    "talagante": "Talagante", "tiltil": "Til Til", "vitacura": "Vitacura",
}

VEHICULOS = {
    "chevrolet-sail": {"marca": "Chevrolet", "modelo": "Sail", "nombre": "Chevrolet Sail"},
    "chevrolet-sonic": {"marca": "Chevrolet", "modelo": "Sonic", "nombre": "Chevrolet Sonic"},
    "chevrolet-spark": {"marca": "Chevrolet", "modelo": "Spark", "nombre": "Chevrolet Spark"},
    "fiat-bravo-tjet": {"marca": "Fiat", "modelo": "Bravo T-Jet", "nombre": "Fiat Bravo T-Jet"},
    "ford-ecosport": {"marca": "Ford", "modelo": "EcoSport", "nombre": "Ford EcoSport"},
    "ford-fiesta": {"marca": "Ford", "modelo": "Fiesta", "nombre": "Ford Fiesta"},
    "honda-city": {"marca": "Honda", "modelo": "City", "nombre": "Honda City"},
    "honda-civic": {"marca": "Honda", "modelo": "Civic", "nombre": "Honda Civic"},
    "honda-cr-v": {"marca": "Honda", "modelo": "CR-V", "nombre": "Honda CR-V"},
    "hyundai-accent": {"marca": "Hyundai", "modelo": "Accent", "nombre": "Hyundai Accent"},
    "hyundai-grand-i10": {"marca": "Hyundai", "modelo": "Grand i10", "nombre": "Hyundai Grand i10"},
    "hyundai-tucson": {"marca": "Hyundai", "modelo": "Tucson", "nombre": "Hyundai Tucson"},
    "kia-morning": {"marca": "Kia", "modelo": "Morning", "nombre": "Kia Morning"},
    "kia-rio": {"marca": "Kia", "modelo": "Rio", "nombre": "Kia Rio"},
    "mazda-3": {"marca": "Mazda", "modelo": "3", "nombre": "Mazda 3"},
    "mazda-cx-5": {"marca": "Mazda", "modelo": "CX-5", "nombre": "Mazda CX-5"},
    "mg-3": {"marca": "MG", "modelo": "3", "nombre": "MG 3"},
    "mg-zs": {"marca": "MG", "modelo": "ZS", "nombre": "MG ZS"},
    "nissan-kicks": {"marca": "Nissan", "modelo": "Kicks", "nombre": "Nissan Kicks"},
    "nissan-versa": {"marca": "Nissan", "modelo": "Versa", "nombre": "Nissan Versa"},
    "peugeot-208": {"marca": "Peugeot", "modelo": "208", "nombre": "Peugeot 208"},
    "peugeot-3008": {"marca": "Peugeot", "modelo": "3008", "nombre": "Peugeot 3008"},
    "renault-duster": {"marca": "Renault", "modelo": "Duster", "nombre": "Renault Duster"},
    "renault-logan": {"marca": "Renault", "modelo": "Logan", "nombre": "Renault Logan"},
    "subaru-forester": {"marca": "Subaru", "modelo": "Forester", "nombre": "Subaru Forester"},
    "subaru-xv": {"marca": "Subaru", "modelo": "XV", "nombre": "Subaru XV"},
    "suzuki-baleno": {"marca": "Suzuki", "modelo": "Baleno", "nombre": "Suzuki Baleno"},
    "suzuki-celerio": {"marca": "Suzuki", "modelo": "Celerio", "nombre": "Suzuki Celerio"},
    "suzuki-swift": {"marca": "Suzuki", "modelo": "Swift", "nombre": "Suzuki Swift"},
    "toyota-corolla": {"marca": "Toyota", "modelo": "Corolla", "nombre": "Toyota Corolla"},
    "toyota-yaris": {"marca": "Toyota", "modelo": "Yaris", "nombre": "Toyota Yaris"},
    "volkswagen-gol": {"marca": "Volkswagen", "modelo": "Gol", "nombre": "Volkswagen Gol"},
}

SERVICIOS = {
    "alineacion-y-balanceo": {"nombre": "Alineación y balanceo", "desc": "Alineación y balanceo de dirección y llantas"},
    "cambio-de-aceite": {"nombre": "Cambio de aceite", "desc": "Cambio de aceite y filtros"},
    "cambio-de-bujias": {"nombre": "Cambio de bujías", "desc": "Cambio de bujías y calibración"},
    "cambio-de-filtros": {"nombre": "Cambio de filtros", "desc": "Cambio de filtros de aire, polen y combustible"},
    "cambio-de-frenos": {"nombre": "Cambio de frenos", "desc": "Pastillas, discos y líquido de frenos"},
    "cambio-de-pastillas": {"nombre": "Cambio de pastillas", "desc": "Cambio de pastillas de freno"},
    "compresion-de-motor": {"nombre": "Compresión de motor", "desc": "Test de compresión de motor"},
    "correa-de-distribucion": {"nombre": "Correa de distribución", "desc": "Cambio de correa de distribución"},
    "embragues-y-distribucion": {"nombre": "Embragues y distribución", "desc": "Embragues y sistema de distribución"},
    "emergencias-mecanicas": {"nombre": "Emergencias mecánicas", "desc": "Atención de emergencias mecánicas 24/7"},
    "reparacion-de-embrague": {"nombre": "Reparación de embrague", "desc": "Reparación y cambio de embrague"},
    "reparacion-de-frenos-abs": {"nombre": "Reparación de frenos ABS", "desc": "Sistema antibloqueo de frenos"},
    "reparacion-de-motor": {"nombre": "Reparación de motor", "desc": "Reparación mayor de motor"},
    "revision-por-kilometraje": {"nombre": "Revisión por kilometraje", "desc": "Mantención según kilometraje"},
    "revision-tecnica-preventiva": {"nombre": "Revisión técnica preventiva", "desc": "Preparación para revisión técnica"},
    "scanner-automotriz": {"nombre": "Scanner automotriz", "desc": "Diagnóstico computarizado"},
    "servicio-de-bateria": {"nombre": "Servicio de batería", "desc": "Cambio y carga de baterías"},
    "suspension-y-direccion": {"nombre": "Suspensión y dirección", "desc": "Reparación de suspensión y dirección"},
    "tren-delantero": {"nombre": "Tren delantero", "desc": "Reparación de tren delantero"},
    "transmision-automatica": {"nombre": "Transmisión automática", "desc": "Reparación de transmisión automática"},
    "inspeccion-mecanica": {"nombre": "Inspección mecánica", "desc": "Inspección mecánica pre-compra"},
    "mantencion-a-domicilio": {"nombre": "Mantención a domicilio", "desc": "Mantención preventiva a domicilio"},
    "mantencion-automotriz": {"nombre": "Mantención automotriz", "desc": "Mantención preventiva del vehículo"},
    "mecanico-a-domicilio": {"nombre": "Mecánico a domicilio", "desc": "Servicio mecánico en tu domicilio"},
    "mecanico-de-emergencia": {"nombre": "Mecánico de emergencia", "desc": "Auxilio mecánico inmediato"},
    "taller-mecanico-a-domicilio": {"nombre": "Taller mecánico a domicilio", "desc": "Taller móvil completo"},
    "taller-mecanico-cerca": {"nombre": "Taller mecánico cerca", "desc": "Taller mecánico cerca de ti"},
    "mecanico-para-mujeres": {"nombre": "Mecánico para mujeres", "desc": "Servicio mecánico con trato cercano"},
    "servicios-domicilio": {"nombre": "Servicios a domicilio", "desc": "Todos los servicios a domicilio"},
    "diagnostico-automotriz": {"nombre": "Diagnóstico automotriz", "desc": "Diagnóstico completo del vehículo"},
    "sistema-de-enfriamiento": {"nombre": "Sistema de enfriamiento", "desc": "Refrigeración y sistema de enfriamiento"},
}

PHONE = "+56 9 3326 1085"
DOMAIN = "https://llanocar.pages.dev"


def truncate_title(text, max_len=60):
    if len(text) <= max_len:
        return text
    truncated = text[:max_len]
    last_space = truncated.rfind(' ')
    if last_space > 30:
        return truncated[:last_space]
    return truncated


def truncate_desc(text, min_len=120, max_len=155):
    if min_len <= len(text) <= max_len:
        return text
    if len(text) > max_len:
        truncated = text[:max_len]
        last_space = truncated.rfind(' ')
        if last_space > min_len:
            return truncated[:last_space]
        return truncated
    return text


def make_schema(name, description, url, area_served="Santiago, Región Metropolitana, Chile", knows_about=None):
    if knows_about is None:
        knows_about = ["Mecánico a domicilio", "Reparación automotriz", "Santiago"]
    return {
        "@context": "https://schema.org",
        "@type": "AutoRepair",
        "name": name,
        "description": description,
        "url": url,
        "telephone": PHONE,
        "areaServed": area_served,
        "knowsAbout": knows_about,
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
            "opens": "00:00",
            "closes": "23:59"
        }],
        "priceRange": "$$"
    }


def classify_filename(filename: str) -> dict:
    """Clasifica un filename en tipo, servicio, comuna, marca."""
    name = filename.replace(".html", "")
    
    servicio_slug = None
    for svc in SERVICIOS:
        if name == svc or name.startswith(svc + "-"):
            servicio_slug = svc
            rest = name[len(svc)+1:]
            break
    else:
        rest = name
    
    if not servicio_slug:
        return {"tipo": "desconocido", "servicio": None, "comuna": None, "marca": None}
    
    comuna_slug = None
    marca_slug = None
    
    # Buscar "en-[comuna]" al final
    en_match = re.search(r'(?:^|-)en-([a-z-]+)$', rest)
    if en_match:
        possible_comuna = en_match.group(1)
        if possible_comuna in COMUNAS:
            comuna_slug = possible_comuna
            rest = rest[:en_match.start()].rstrip("-")
    
    # Si queda algo, es la marca/vehículo
    if rest:
        if rest in VEHICULOS:
            marca_slug = rest
        else:
            for veh_slug in VEHICULOS:
                if rest == veh_slug or rest.startswith(veh_slug + "-"):
                    possible_comuna = rest[len(veh_slug)+1:]
                    if possible_comuna in COMUNAS:
                        marca_slug = veh_slug
                        comuna_slug = possible_comuna
                    break
    
    if comuna_slug and marca_slug:
        tipo = "servicio-marca-comuna"
    elif comuna_slug:
        tipo = "servicio-comuna"
    elif marca_slug:
        tipo = "servicio-marca"
    else:
        tipo = "servicio"
    
    return {"tipo": tipo, "servicio": servicio_slug, "comuna": comuna_slug, "marca": marca_slug}


def gen_metadata(rel_path: str) -> dict:
    parts = rel_path.split("/")
    
    # Páginas en subcarpetas
    if len(parts) == 2:
        section = parts[0]
        slug = parts[1].replace(".html", "")
        
        if section == "comunas" and slug in COMUNAS:
            comuna = COMUNAS[slug]
            url = f"{DOMAIN}/comunas/{slug}.html"
            title = truncate_title(f"Mecánico a domicilio en {comuna} | 24/7")
            desc = truncate_desc(f"🚗 ¿Necesitas mecánico a domicilio en {comuna}? Atendemos 24/7 frenos, aceite, scanner y más. 🔧 ¡Cotiza ahora! 📞 {PHONE}")
            schema = make_schema(
                f"Mecánico a Domicilio en {comuna}",
                f"Servicio de mecánico a domicilio en {comuna}, Región Metropolitana. Reparación de frenos, cambio de aceite, diagnóstico scanner, electricidad y emergencias 24 horas.",
                url,
                f"{comuna}, Región Metropolitana, Chile",
                ["Mecánico a domicilio", "Reparación de frenos", "Cambio de aceite", "Diagnóstico scanner", "Electricidad automotriz", comuna]
            )
            return {"title": title, "description": desc, "schema": schema, "url": url}
        
        elif section == "vehiculos" and slug in VEHICULOS:
            veh = VEHICULOS[slug]
            nombre = veh["nombre"]
            marca = veh["marca"]
            url = f"{DOMAIN}/vehiculos/{slug}.html"
            title = truncate_title(f"Mecánico a domicilio para {nombre} | Santiago")
            desc = truncate_desc(f"🚗 ¿Mecánico a domicilio para {nombre} en Santiago? Aceite, frenos, scanner, electricidad. ⚡ 24/7. 📞 {PHONE}")
            schema = make_schema(
                f"Mecánico a Domicilio para {nombre} en Santiago",
                f"Servicio de mecánico a domicilio para {nombre} en Santiago, Región Metropolitana. Cambio de aceite, frenos, diagnóstico scanner, electricidad y emergencias 24 horas.",
                url,
                "Santiago, Región Metropolitana, Chile",
                ["Mecánico a domicilio", marca, veh["modelo"], nombre, "Reparación automotriz"]
            )
            return {"title": title, "description": desc, "schema": schema, "url": url}
        
        elif section == "marcas_automotrices":
            if slug in VEHICULOS:
                veh = VEHICULOS[slug]
                marca = veh["marca"]
                nombre = veh["nombre"]
            else:
                marca = slug.replace("-", " ").title()
                nombre = marca
            url = f"{DOMAIN}/marcas_automotrices/{slug}.html"
            title = truncate_title(f"Mecánico a domicilio para {marca} | Santiago")
            desc = truncate_desc(f"🔧 ¿Mecánico a domicilio para {marca} en Santiago? Especialistas 24/7. Frenos, aceite, scanner. 📞 {PHONE}")
            schema = make_schema(
                f"Mecánico a Domicilio para {marca} en Santiago",
                f"Servicio de mecánico a domicilio especializado para vehículos {marca} en Santiago, Región Metropolitana. Reparación de frenos, cambio de aceite, diagnóstico scanner y emergencias 24 horas.",
                url,
                "Santiago, Región Metropolitana, Chile",
                ["Mecánico a domicilio", marca, "Reparación automotriz"]
            )
            return {"title": title, "description": desc, "schema": schema, "url": url}
        
        elif section == "blog":
            url = f"{DOMAIN}/blog/{slug}.html"
            title = truncate_title(f"Mecánico a domicilio en Santiago | Blog")
            desc = truncate_desc(f"🔧 Blog de mecánica automotriz. Tips, mantención y reparación de autos en Santiago, Chile. 📞 {PHONE}")
            schema = make_schema(
                "Mecánico a Domicilio en Santiago - Blog",
                "Blog de mecánica automotriz con tips de mantención, reparación y diagnóstico para vehículos en Santiago, Chile.",
                url,
                "Santiago, Región Metropolitana, Chile",
                ["Mecánico a domicilio", "Blog automotriz", "Tips de mecánica"]
            )
            return {"title": title, "description": desc, "schema": schema, "url": url}
    
    # Páginas en raíz
    if len(parts) == 1:
        filename = parts[0]
        
        # Páginas especiales raíz
        root_pages = {
            "index.html": {
                "title": "Mecánico a domicilio en Santiago | 24/7",
                "desc": f"🚗 ¿Mecánico a domicilio en Santiago? Atención 24/7. Frenos, aceite, scanner, electricidad. +5.000 clientes. 🔧 ¡Cotiza! 📞 {PHONE}",
            },
            "contacto.html": {
                "title": "Contacto mecánico a domicilio Santiago | 24/7",
                "desc": f"📞 Contacta mecánico a domicilio en Santiago. Atención 24/7. Cotiza por WhatsApp {PHONE}. 🚗 ¡Llama ahora!",
            },
            "quienes-somos.html": {
                "title": "Mecánico a domicilio Santiago | Quiénes somos",
                "desc": f"🔧 Equipo de mecánicos a domicilio en Santiago. +5.000 clientes atendidos. Experiencia y confianza. 📞 {PHONE}",
            },
        }
        
        if filename in root_pages:
            page = root_pages[filename]
            url = DOMAIN if filename == "index.html" else f"{DOMAIN}/{filename.replace('.html', '')}.html"
            title = truncate_title(page["title"])
            desc = truncate_desc(page["desc"])
            schema = make_schema(
                "Mecánico a Domicilio en Santiago",
                desc.replace("🚗 ", "").replace("🔧 ", "").replace("📞 ", ""),
                url,
                "Santiago, Región Metropolitana, Chile",
                ["Mecánico a domicilio", "Reparación automotriz", "Santiago"]
            )
            return {"title": title, "description": desc, "schema": schema, "url": url}
        
        # Clasificar por patrón
        info = classify_filename(filename)
        tipo = info["tipo"]
        svc = info["servicio"]
        comuna_slug = info["comuna"]
        marca_slug = info["marca"]
        
        url = f"{DOMAIN}/{filename.replace('.html', '')}.html"
        
        if tipo == "servicio" and svc:
            svc_data = SERVICIOS[svc]
            nombre = svc_data["nombre"]
            desc_corta = svc_data["desc"]
            title = truncate_title(f"{nombre} a domicilio en Santiago | En sitio")
            desc = truncate_desc(f"🔧 {nombre} a domicilio en Santiago. {desc_corta}. Vamos a tu casa o trabajo 24/7. ⚡ ¡Cotiza! 📞 {PHONE}")
            schema = make_schema(
                f"{nombre} a Domicilio en Santiago",
                f"Servicio de {nombre.lower()} a domicilio en Santiago, Región Metropolitana. {desc_corta}. Atención en sitio 24/7.",
                url,
                "Santiago, Región Metropolitana, Chile",
                ["Mecánico a domicilio", nombre]
            )
            return {"title": title, "description": desc, "schema": schema, "url": url}
        
        elif tipo == "servicio-comuna" and svc and comuna_slug:
            svc_data = SERVICIOS[svc]
            comuna = COMUNAS[comuna_slug]
            nombre = svc_data["nombre"]
            desc_corta = svc_data["desc"]
            title = truncate_title(f"{nombre} a domicilio en {comuna} | 24/7")
            desc = truncate_desc(f"🔧 {nombre} a domicilio en {comuna}. {desc_corta}. Vamos a tu casa 24/7. ⚡ ¡Cotiza! 📞 {PHONE}")
            schema = make_schema(
                f"{nombre} a Domicilio en {comuna}",
                f"Servicio de {nombre.lower()} a domicilio en {comuna}, Región Metropolitana. {desc_corta}. Atención 24/7.",
                url,
                f"{comuna}, Región Metropolitana, Chile",
                ["Mecánico a domicilio", nombre, comuna]
            )
            return {"title": title, "description": desc, "schema": schema, "url": url}
        
        elif tipo == "servicio-marca" and svc and marca_slug:
            svc_data = SERVICIOS[svc]
            veh = VEHICULOS[marca_slug]
            nombre_svc = svc_data["nombre"]
            nombre_veh = veh["nombre"]
            marca = veh["marca"]
            title = truncate_title(f"{nombre_svc} para {nombre_veh} | Santiago")
            desc = truncate_desc(f"🚗 {nombre_svc} para {nombre_veh} en Santiago. Vamos a tu casa 24/7. ⚡ ¡Cotiza! 📞 {PHONE}")
            schema = make_schema(
                f"{nombre_svc} para {nombre_veh} en Santiago",
                f"Servicio de {nombre_svc.lower()} para {nombre_veh} en Santiago, Región Metropolitana. Atención a domicilio 24/7.",
                url,
                "Santiago, Región Metropolitana, Chile",
                ["Mecánico a domicilio", nombre_svc, marca, veh["modelo"], nombre_veh]
            )
            return {"title": title, "description": desc, "schema": schema, "url": url}
        
        elif tipo == "servicio-marca-comuna" and svc and marca_slug and comuna_slug:
            svc_data = SERVICIOS[svc]
            veh = VEHICULOS[marca_slug]
            comuna = COMUNAS[comuna_slug]
            nombre_svc = svc_data["nombre"]
            nombre_veh = veh["nombre"]
            marca = veh["marca"]
            title = truncate_title(f"{nombre_svc} para {nombre_veh} en {comuna}")
            desc = truncate_desc(f"🚗 {nombre_svc} para {nombre_veh} en {comuna}. Vamos a tu casa 24/7. ⚡ ¡Cotiza! 📞 {PHONE}")
            schema = make_schema(
                f"{nombre_svc} para {nombre_veh} en {comuna}",
                f"Servicio de {nombre_svc.lower()} para {nombre_veh} en {comuna}, Región Metropolitana. Atención a domicilio 24/7.",
                url,
                f"{comuna}, Región Metropolitana, Chile",
                ["Mecánico a domicilio", nombre_svc, marca, veh["modelo"], nombre_veh, comuna]
            )
            return {"title": title, "description": desc, "schema": schema, "url": url}
    
    # Fallback genérico
    url = f"{DOMAIN}/{rel_path.replace('.html', '')}.html"
    title = truncate_title("Mecánico a domicilio en Santiago | 24/7")
    desc = truncate_desc(f"🚗 ¿Mecánico a domicilio en Santiago? Atención 24/7. Frenos, aceite, scanner, electricidad. 📞 {PHONE}")
    schema = make_schema(
        "Mecánico a Domicilio en Santiago",
        "Servicio de mecánico a domicilio en Santiago, Región Metropolitana. Reparación de frenos, cambio de aceite, diagnóstico scanner y emergencias 24 horas.",
        url,
        "Santiago, Región Metropolitana, Chile"
    )
    return {"title": title, "description": desc, "schema": schema, "url": url}


def apply_metadata_to_html(html: str, metadata: dict) -> str:
    # 1. Title
    title_pattern = re.compile(r'<title>[^<]*</title>', re.IGNORECASE)
    new_title = f'<title>{metadata["title"]}</title>'
    if title_pattern.search(html):
        html = title_pattern.sub(new_title, html, count=1)
    else:
        html = re.sub(r'(<head[^>]*>)', r'\1\n  ' + new_title, html, count=1)
    
    # 2. Meta description
    desc_pattern = re.compile(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\']\s*/?>', re.IGNORECASE)
    new_desc_tag = f'<meta name="description" content="{metadata["description"]}"/>'
    if desc_pattern.search(html):
        html = desc_pattern.sub(new_desc_tag, html, count=1)
    else:
        html = re.sub(r'(</title>)', r'\1\n  ' + new_desc_tag, html, count=1)
    
    # 3. OG tags
    og_title_pattern = re.compile(r'<meta\s+property=["\']og:title["\']\s+content=["\']([^"\']*)["\']\s*/?>', re.IGNORECASE)
    if og_title_pattern.search(html):
        html = og_title_pattern.sub(f'<meta property="og:title" content="{metadata["title"]}"/>', html, count=1)
    
    og_desc_pattern = re.compile(r'<meta\s+property=["\']og:description["\']\s+content=["\']([^"\']*)["\']\s*/?>', re.IGNORECASE)
    if og_desc_pattern.search(html):
        html = og_desc_pattern.sub(f'<meta property="og:description" content="{metadata["description"]}"/>', html, count=1)
    
    # 4. Twitter tags
    tw_title_pattern = re.compile(r'<meta\s+name=["\']twitter:title["\']\s+content=["\']([^"\']*)["\']\s*/?>', re.IGNORECASE)
    if tw_title_pattern.search(html):
        html = tw_title_pattern.sub(f'<meta name="twitter:title" content="{metadata["title"]}"/>', html, count=1)
    
    tw_desc_pattern = re.compile(r'<meta\s+name=["\']twitter:description["\']\s+content=["\']([^"\']*)["\']\s*/?>', re.IGNORECASE)
    if tw_desc_pattern.search(html):
        html = tw_desc_pattern.sub(f'<meta name="twitter:description" content="{metadata["description"]}"/>', html, count=1)
    
    # 5. JSON-LD: reemplazar el primer bloque existente
    jsonld_pattern = re.compile(
        r'<script\s+type=["\']application/ld\+json["\']\s*>(.*?)</script>',
        re.DOTALL | re.IGNORECASE
    )
    
    schema_json = json.dumps(metadata["schema"], ensure_ascii=False, indent=2)
    new_jsonld_block = f'<script type="application/ld+json">\n{schema_json}\n  </script>'
    
    if jsonld_pattern.search(html):
        html = jsonld_pattern.sub(new_jsonld_block, html, count=1)
    else:
        html = re.sub(r'(</head>)', '  ' + new_jsonld_block + r'\n\1', html, count=1)
    
    return html


def main():
    files = sorted(REPO_ROOT.rglob("*.html"))
    # Excluir .git, node_modules, etc.
    files = [f for f in files if ".git" not in f.parts and "node_modules" not in f.parts]
    
    print(f"Procesando {len(files)} archivos HTML...")
    print(f"Directorio: {REPO_ROOT}")
    print("=" * 60)
    
    stats = {}
    total_processed = 0
    
    for i, f in enumerate(files, 1):
        rel = f.relative_to(REPO_ROOT).as_posix()
        
        if "google7a5c4682" in rel:
            continue
        
        try:
            metadata = gen_metadata(rel)
            
            parts = rel.split("/")
            if len(parts) == 2:
                section = parts[0]
            elif len(parts) == 1:
                info = classify_filename(parts[0])
                section = info["tipo"]
            else:
                section = "other"
            
            stats[section] = stats.get(section, 0) + 1
            
            html = f.read_text(encoding="utf-8", errors="replace")
            modified = apply_metadata_to_html(html, metadata)
            
            if modified != html:
                f.write_text(modified, encoding="utf-8")
                total_processed += 1
            
            if i % 50 == 0 or i == len(files):
                print(f"  [{i}/{len(files)}] procesados")
        except Exception as e:
            print(f"  ✗ ERROR en {rel}: {e}")
    
    print()
    print("=" * 60)
    print(f"✓ Total archivos modificados: {total_processed}")
    print(f"  Por tipo:")
    for tipo, count in sorted(stats.items(), key=lambda x: -x[1]):
        print(f"    - {tipo}: {count}")
    
    # Muestras
    print()
    print("=" * 60)
    print("MUESTRAS DE EJEMPLO:")
    
    samples = [
        ("index.html", "Index"),
        ("comunas/la-florida.html", "Comuna"),
        ("vehiculos/toyota-corolla.html", "Vehículo"),
        ("marcas_automotrices/renault-duster.html", "Marca"),
        ("cambio-de-aceite.html", "Servicio simple"),
        ("cambio-de-aceite-en-pudahuel.html", "Servicio + comuna"),
        ("alineacion-y-balanceo-chevrolet-sail.html", "Servicio + marca"),
        ("cambio-de-aceite-toyota-corolla-en-la-granja.html", "Servicio + marca + comuna"),
        ("correa-de-distribucion.html", "Servicio simple 2"),
        ("emergencias-mecanicas-en-conchali.html", "Emergencias + comuna"),
    ]
    
    for path, label in samples:
        full_path = REPO_ROOT / path
        if not full_path.exists():
            print(f"\n--- {label} ({path}) ---")
            print(f"  (archivo no encontrado)")
            continue
        try:
            metadata = gen_metadata(path)
            print(f"\n--- {label} ({path}) ---")
            print(f"  Title: {metadata['title']} ({len(metadata['title'])} chars)")
            print(f"  Desc:  {metadata['description']} ({len(metadata['description'])} chars)")
            print(f"  URL:   {metadata['url']}")
            print(f"  Schema name: {metadata['schema'].get('name')}")
        except Exception as e:
            print(f"\n--- {label} ({path}) ---")
            print(f"  ERROR: {e}")


if __name__ == "__main__":
    main()
