#!/usr/bin/env python3
"""
Reemplaza nombres de imágenes de servicio con nombres SEO optimizados.
NO toca: logos de marcas (SVG), fotos de vehículos, favicon, imágenes especiales.
Solo reemplaza las imágenes de servicio en images/ (hero backgrounds, OG, favicon de servicio).
"""

import re
import glob
import os
import random

# ============ CONFIGURACIÓN ============

# Nuevos nombres SEO proporcionados por el usuario (200)
NUEVOS_NOMBRES_SEO = """
mecanico-a-domicilio-chevrolet-santiago-taller-mecanico-cerca-de-mi.jpg
scanner-automotriz-ford-puente-alto-profesional-diagnostico-avanzado.jpg
frenos-y-pastillas-honda-maipu-taller-mecanico-cerca-de-mi-urgente.jpg
cambio-de-aceite-hyundai-la-florida-express-mantenimiento-garantizado.jpg
afinamiento-motor-kia-san-bernardo-taller-mecanico-cerca-de-mi-experto.jpg
inspeccion-pre-compra-mazda-las-condes-revision-tecnica-completa.jpg
diagnostico-electrico-mitsubishi-penalolen-taller-mecanico-cerca-de-mi.jpg
mantenimiento-kilometraje-nissan-pudahuel-servicio-oficial-llanocar.jpg
reparacion-de-embrague-peugeot-quilicura-taller-mecanico-cerca-de-mi-diesel.jpg
cambio-correa-distribucion-renault-nunoa-repuestos-originales-garantizados.jpg
servicio-de-baterias-subaru-la-cisterna-taller-mecanico-cerca-de-mi-24hrs.jpg
ajuste-de-suspension-suzuki-estacion-central-amortiguadores-y-direccion.jpg
mecanico-urgencia-toyota-recoleta-taller-mecanico-cerca-de-mi-panne.jpg
scanner-multimarca-volkswagen-providencia-deteccion-de-fallas-electronicas.jpg
auxilio-mecanico-audi-vitacura-taller-mecanico-cerca-de-mi-alta-gama.jpg
revision-tecnica-bmw-lo-barnechea-preparacion-profesional-expertos.jpg
mecanico-24-horas-citroen-macul-taller-mecanico-cerca-de-mi-emergencia.jpg
reparacion-transmision-fiat-quinta-normal-caja-de-cambios-especialista.jpg
mantencion-preventiva-jeep-independencia-taller-mecanico-cerca-de-mi-4x4.jpg
electricidad-automotriz-mercedes-benz-san-miguel-sistema-electrico-integral.jpg
mecanico-domicilio-mg-huechuraba-taller-mecanico-cerca-de-mi-economico.jpg
scanner-motor-opel-conchali-lectura-de-codigos-check-engine.jpg
frenos-pastillas-ssangyong-lo-prado-taller-mecanico-cerca-de-mi-seguridad.jpg
cambio-aceite-volvo-cerrillos-filtro-de-aire-y-lubricante-sintetico.jpg
afinamiento-motor-byd-renca-taller-mecanico-cerca-de-mi-hibridos.jpg
inspeccion-compra-chery-cerro-navia-peritaje-automotriz-profesional.jpg
diagnostico-scanner-changan-lo-espejo-taller-mecanico-cerca-de-mi-rapido.jpg
embrague-y-frenos-dfsk-san-joaquin-kit-nuevo-instalacion-express.jpg
correa-distribucion-great-wall-san-ramon-taller-mecanico-cerca-de-mi-motor.jpg
bateria-automotriz-haval-la-granja-reemplazo-a-domicilio-instante.jpg
suspension-y-direccion-jac-la-pintana-taller-mecanico-cerca-de-mi-tren-delantero.jpg
mecanico-express-jmc-pedro-aguirre-cerda-taller-movil-multimarca.jpg
servicio-integral-mahindra-san-jose-de-maipo-taller-mecanico-cerca-de-mi-montana.jpg
mantenimiento-ram-pirque-camionetas-petroleras-servicio-profesional.jpg
mecanico-a-domicilio-chevrolet-buin-taller-mecanico-cerca-de-mi-confianza.jpg
scanner-automotriz-toyota-paine-limpieza-inyectores-y-bujias.jpg
frenos-y-pastillas-nissan-talagante-taller-mecanico-cerca-de-mi-rectificado.jpg
cambio-de-aceite-hyundai-el-monte-sintetico-multigrado-alto-kilometraje.jpg
afinamiento-motor-kia-isla-de-maipo-taller-mecanico-cerca-de-mi-bujias.jpg
inspeccion-pre-compra-ford-melipilla-scanner-total-y-fugas-aceite.jpg
diagnostico-electrico-mazda-curacavi-taller-mecanico-cerca-de-mi-partida.jpg
mantenimiento-kilometraje-suzuki-maria-pinto-pauta-fabricante-oficial.jpg
reparacion-de-embrague-peugeot-colina-taller-mecanico-cerca-de-mi-pedal.jpg
cambio-correa-distribucion-renault-lampa-kit-distribucion-completo.jpg
servicio-de-bateria-subaru-tiltil-taller-mecanico-cerca-de-mi-voltaje.jpg
ajuste-de-suspension-volkswagen-alhue-amortiguadores-y-cazoletas.jpg
mecanico-urgencia-fiat-calera-de-tango-taller-mecanico-cerca-de-mi-panne.jpg
scanner-automotriz-chery-padre-hurtado-luz-check-engine-borrado.jpg
frenos-y-pastillas-mg-penaflor-taller-mecanico-cerca-de-mi-expertos.jpg
cambio-de-aceite-changan-santiago-centro-rapido-barato-calidad.jpg
afinamiento-motor-haval-vitacura-taller-mecanico-cerca-de-mi-premium.jpg
inspeccion-pre-compra-mitsubishi-las-condes-mecanica-general-scanner.jpg
diagnostico-electrico-nissan-maipu-taller-mecanico-cerca-de-mi-bobinas.jpg
mantenimiento-kilometraje-toyota-la-florida-garantia-llanocar-total.jpg
reparacion-de-embrague-hyundai-puente-alto-taller-mecanico-cerca-de-mi-bimasa.jpg
cambio-correa-distribucion-kia-san-bernardo-bomba-de-agua-expertos.jpg
servicio-de-bateria-chevrolet-la-cisterna-taller-mecanico-cerca-de-mi-carga.jpg
ajuste-de-suspension-mazda-nunoa-alineacion-y-balanceo-ruedas.jpg
mecanico-domicilio-ford-providencia-taller-mecanico-cerca-de-mi-camionetas.jpg
scanner-automotriz-volkswagen-las-condes-diagnosis-computarizada-vcds.jpg
frenos-pastillas-toyota-la-reina-taller-mecanico-cerca-de-mi-discos.jpg
cambio-aceite-nissan-macul-filtro-aire-y-filtro-polen.jpg
afinamiento-motor-chevrolet-penalolen-taller-mecanico-cerca-de-mi-limpieza.jpg
inspeccion-compra-hyundai-la-pintana-informe-tecnico-scanner-fugas.jpg
diagnostico-electrico-kia-pudahuel-taller-mecanico-cerca-de-mi-tablero.jpg
mantenimiento-kilometraje-ford-quilicura-aceite-motorcraft-original.jpg
reparacion-embrague-suzuki-san-miguel-taller-mecanico-cerca-de-mi-prensa.jpg
correa-distribucion-peugeot-estacion-central-motor-hdi-especialistas.jpg
bateria-domicilio-mazda-huechuraba-taller-mecanico-cerca-de-mi-bosch.jpg
suspension-mitsubishi-independencia-buje-bandeja-y-terminal-direccion.jpg
mecanico-urgencia-renault-recoleta-taller-mecanico-cerca-de-mi-electrico.jpg
scanner-changan-quinta-normal-borrado-fallas-computador-auto.jpg
frenos-pastillas-great-wall-san-joaquin-taller-mecanico-cerca-de-mi-ceramica.jpg
cambio-aceite-haval-san-ramon-castrol-mobil-ultra-proteccion.jpg
afinamiento-chery-lo-prado-taller-mecanico-cerca-de-mi-inyectores.jpg
inspeccion-jac-lo-espejo-recorrido-de-prueba-y-compresion.jpg
diagnostico-dfsk-cerro-navia-taller-mecanico-cerca-de-mi-furgones.jpg
mantenimiento-mg-cerrillos-pauta-garantia-llanocar-multimarca.jpg
embrague-ssangyong-renca-taller-mecanico-cerca-de-mi-especialista.jpg
correa-distribucion-volvo-vitacura-mantenimiento-mayor-kilometraje.jpg
mecanico-domicilio-kia-lo-barnechea-taller-mecanico-cerca-de-mi-suv.jpg
scanner-toyota-buin-corolla-yaris-limpieza-mariposa-admision.jpg
frenos-nissan-paine-taller-mecanico-cerca-de-mi-qashqai-xtrail.jpg
cambio-aceite-ford-talagante-ecosport-ranger-express-garantizado.jpg
afinamiento-mazda-el-monte-taller-mecanico-cerca-de-mi-skyactiv.jpg
inspeccion-hyundai-isla-de-maipo-tucson-santafe-revision-precompra.jpg
diagnostico-chevrolet-melipilla-taller-mecanico-cerca-de-mi-sail-spark.jpg
mantenimiento-suzuki-curacavi-swift-baleno-mantenimiento-preventivo.jpg
embrague-peugeot-maria-pinto-taller-mecanico-cerca-de-mi-partner.jpg
correa-distribucion-renault-colina-clio-symbol-cambio-urgente.jpg
bateria-subaru-lampa-taller-mecanico-cerca-de-mi-awd-sistema.jpg
suspension-volkswagen-tiltil-gol-vento-amortiguadores-nuevos.jpg
mecanico-urgencia-fiat-alhue-taller-mecanico-cerca-de-mi-comerciales.jpg
scanner-chery-calera-de-tango-tiggo-pro-diagnostico-computador.jpg
frenos-mg-padre-hurtado-taller-mecanico-cerca-de-mi-zs-extender.jpg
cambio-aceite-changan-penaflor-cx70-alsvin-filtro-aceite-original.jpg
afinamiento-haval-pirque-taller-mecanico-cerca-de-mi-h6-jolion.jpg
inspeccion-mitsubishi-san-jose-de-maipo-l200-montero-scanner-4x4.jpg
diagnostico-nissan-san-pedro-taller-mecanico-cerca-de-mi-sentra-versa.jpg
mantenimiento-toyota-alhue-hilux-rav4-expertos-japoneses-llanocar.jpg
mecanico-domicilio-chevrolet-la-reina-taller-mecanico-cerca-de-mi-onix.jpg
scanner-automotriz-ford-lo-barnechea-territory-explorer-diagnosis.jpg
frenos-pastillas-honda-vitacura-taller-mecanico-cerca-de-mi-civic.jpg
cambio-aceite-hyundai-providencia-accent-elantra-mecanico-express.jpg
afinamiento-motor-kia-las-condes-taller-mecanico-cerca-de-mi-rio.jpg
inspeccion-pre-compra-mazda-nunoa-cx5-mazda3-peritaje-tecnico.jpg
diagnostico-electrico-mitsubishi-la-florida-taller-mecanico-cerca-de-mi-asx.jpg
mantenimiento-kilometraje-nissan-maipu-kicks-navara-pauta-llanocar.jpg
reparacion-embrague-peugeot-puente-alto-taller-mecanico-cerca-de-mi-3008.jpg
correa-distribucion-renault-san-bernardo-duster-oroch-mantenimiento.jpg
servicio-bateria-subaru-la-cisterna-taller-mecanico-cerca-de-mi-forester.jpg
ajuste-suspension-suzuki-estacion-central-vitara-jimny-expertos.jpg
mecanico-urgencia-toyota-macul-taller-mecanico-cerca-de-mi-hibrido.jpg
scanner-multimarca-volkswagen-quilicura-amarok-tiguan-diagnosis-vcds.jpg
auxilio-mecanico-audi-san-miguel-taller-mecanico-cerca-de-mi-premium.jpg
revision-tecnica-bmw-huechuraba-serie3-x5-pre-revision-profesional.jpg
mecanico-24-horas-citroen-recoleta-taller-mecanico-cerca-de-mi-berlingo.jpg
reparacion-transmision-fiat-quinta-normal-palio-uno-caja-cambios.jpg
mantencion-preventiva-jeep-independencia-taller-mecanico-cerca-de-mi-wrangler.jpg
electricidad-automotriz-mercedes-san-joaquin-sprinter-clasea-electronica.jpg
mecanico-domicilio-mg-san-ramon-taller-mecanico-cerca-de-mi-mg3.jpg
scanner-motor-opel-la-granja-corsa-mokka-lectura-fallas.jpg
frenos-pastillas-ssangyong-la-pintana-taller-mecanico-cerca-de-mi-actyon.jpg
cambio-aceite-volvo-pedro-aguirre-cerda-xc60-v40-sintetico.jpg
afinamiento-motor-byd-san-pedro-taller-mecanico-cerca-de-mi-yuan.jpg
inspeccion-compra-chery-alhue-arrizo-iq-revision-total.jpg
diagnostico-scanner-changan-pirque-taller-mecanico-cerca-de-mi-cs35.jpg
embrague-y-frenos-dfsk-san-jose-de-maipo-glory-truck-urgente.jpg
correa-distribucion-great-wall-penaflor-taller-mecanico-cerca-de-mi-poer.jpg
bateria-automotriz-haval-padre-hurtado-start-stop-reemplazo.jpg
suspension-y-direccion-jac-melipilla-taller-mecanico-cerca-de-mi-js2.jpg
mecanico-express-jmc-curacavi-vigus-conway-taller-movil.jpg
servicio-integral-mahindra-colina-taller-mecanico-cerca-de-mi-pikup.jpg
mantenimiento-ram-lampa-700-1500-expertos-camionetas.jpg
mecanico-domicilio-nissan-tiltil-taller-mecanico-cerca-de-mi-24hrs.jpg
scanner-toyota-calera-de-tango-hibridos-expertos-diagnosis.jpg
frenos-ford-maria-pinto-taller-mecanico-cerca-de-mi-abs.jpg
cambio-aceite-kia-isla-de-maipo-filtro-original-llanocar.jpg
afinamiento-hyundai-el-monte-taller-mecanico-cerca-de-mi-mariposa.jpg
inspeccion-chevrolet-talagante-scanner-fugas-compresion.jpg
diagnostico-mazda-paine-taller-mecanico-cerca-de-mi-sensores.jpg
mantenimiento-suzuki-buin-garantizado-llanocar-profesional.jpg
reparacion-peugeot-san-pedro-taller-mecanico-cerca-de-mi-diesel.jpg
correa-distribucion-renault-alhue-clio-kangoo-cambio-kit.jpg
bateria-subaru-san-jose-de-maipo-taller-mecanico-cerca-de-mi-gel.jpg
suspension-volkswagen-pirque-gol-saveiro-amortiguacion.jpg
mecanico-urgencia-fiat-penaflor-taller-mecanico-cerca-de-mi-panne.jpg
scanner-chery-padre-hurtado-borrar-testigo-check-engine.jpg
frenos-mg-calera-de-tango-taller-mecanico-cerca-de-mi-pastillas.jpg
cambio-aceite-changan-tiltil-lubricante-sintetico-express.jpg
afinamiento-haval-lampa-taller-mecanico-cerca-de-mi-motor.jpg
inspeccion-mitsubishi-colina-compra-segura-peritaje.jpg
diagnostico-nissan-curacavi-taller-mecanico-cerca-de-mi-profesional.jpg
mantenimiento-toyota-melipilla-kilometraje-pauta-oficial.jpg
mecanico-domicilio-chevrolet-cerro-navia-taller-mecanico-cerca-de-mi.jpg
scanner-ford-renca-fallas-transmision-diagnosis-motor.jpg
frenos-honda-cerrillos-taller-mecanico-cerca-de-mi-liquido.jpg
cambio-aceite-hyundai-lo-espejo-filtro-petroleo-diesel.jpg
afinamiento-kia-lo-prado-taller-mecanico-cerca-de-mi-inyector.jpg
inspeccion-mazda-san-joaquin-estado-motor-y-chasis.jpg
diagnostico-mitsubishi-quinta-normal-taller-mecanico-cerca-de-mi-4x4.jpg
mantenimiento-nissan-recoleta-aceite-transmision-automatica.jpg
reparacion-peugeot-independencia-taller-mecanico-cerca-de-mi-tren.jpg
correa-distribucion-renault-huechuraba-cambio-urgente-kit.jpg
bateria-subaru-estacion-central-taller-mecanico-cerca-de-mi-bornes.jpg
suspension-suzuki-la-cisterna-amortiguadores-traseros-nuevos.jpg
mecanico-urgencia-toyota-san-bernardo-taller-mecanico-cerca-de-mi.jpg
scanner-volkswagen-puente-alto-airbag-abs-diagnosis.jpg
frenos-audi-la-florida-taller-mecanico-cerca-de-mi-brembo.jpg
cambio-aceite-bmw-maipu-aceite-longlife-filtro-original.jpg
afinamiento-citroen-pudahuel-taller-mecanico-cerca-de-mi-polen.jpg
inspeccion-fiat-quilicura-mecanico-de-confianza-llanocar.jpg
diagnostico-jeep-nunoa-taller-mecanico-cerca-de-mi-computador.jpg
mantenimiento-mercedes-las-condes-service-a-b-expertos.jpg
reparacion-mg-vitacura-taller-mecanico-cerca-de-mi-postventa.jpg
correa-distribucion-opel-lo-barnechea-reemplazo-kit-original.jpg
bateria-ssangyong-la-reina-taller-mecanico-cerca-de-mi-amperaje.jpg
suspension-volvo-providencia-bieletas-rotulas-bandejas.jpg
mecanico-domicilio-byd-macul-taller-mecanico-cerca-de-mi-electrico.jpg
scanner-chery-penalolen-reinicio-mantenimiento-testigos.jpg
frenos-changan-san-miguel-taller-mecanico-cerca-de-mi-balatas.jpg
cambio-aceite-dfsk-lo-prado-filtro-habitaculo-express.jpg
afinamiento-great-wall-cerrillos-taller-mecanico-cerca-de-mi-admision.jpg
inspeccion-haval-lo-espejo-revision-suspension-motor.jpg
diagnostico-jac-san-joaquin-taller-mecanico-cerca-de-mi-diesel.jpg
mantenimiento-jmc-quinta-normal-camioneta-vigus-expertos.jpg
reparacion-mahindra-recoleta-taller-mecanico-cerca-de-mi-bimasa.jpg
correa-distribucion-ram-independencia-ajuste-tiempo-motor.jpg
bateria-chevrolet-huechuraba-taller-mecanico-cerca-de-mi-prueba.jpg
suspension-ford-estacion-central-alineacion-ruedas-expertos.jpg
mecanico-urgencia-honda-la-cisterna-taller-mecanico-cerca-de-mi.jpg
scanner-hyundai-san-bernardo-computador-abordo-diagnosis.jpg
frenos-kia-maipu-taller-mecanico-cerca-de-mi-emergencia.jpg
cambio-aceite-mazda-la-florida-filtro-skyactiv-original.jpg
afinamiento-nissan-puente-alto-taller-mecanico-cerca-de-mi-bujia.jpg
inspeccion-peugeot-las-condes-fugas-refrigerante-expertos.jpg
diagnostico-suzuki-nunoa-taller-mecanico-cerca-de-mi-sensores.jpg
mantenimiento-toyota-vitacura-expertos-japoneses-original.jpg
reparacion-volkswagen-providencia-taller-mecanico-cerca-de-mi-dsg.jpg
mecanico-domicilio-chevrolet-maipu-urgente-llanocar-taller.jpg
""".strip().split('\n')

# Imágenes que NUNCA se deben tocar (logos, vehículos, favicon, especiales)
IMAGENES_PROTEGIDAS = {
    # Favicon compartido
    'mecanico-a-domicilio-en-santiago.png',
    # Imágenes genéricas / especiales
    'image1.jpg', 'image2.png', 'og-image.jpg',
    'mantenimiento-vehicular-general.jpeg',
    'mecanico-a-domicilio-santiago-247-global-pro-automotriz-reparacion-emergencia-en-ruta.jpg',
    'mecanico-a-domicilio-providencia.jpg',
    'forrar-un-volante-con-cuero-forrar-volante-coche-en-santiago-monocromatico.jpg',
    'accidentado-en-la-via-barado-el-carro-no-prende-mecanico-en-la-via-a-domicilio-en-santiago.png',
    'WhatsApp Image 2026-03-05 at 6.09.22 PM.jpeg',
}

# Rutas protegidas (subdirectorios de vehículos y logos)
PROTECTED_PATHS = ['wp-content/', 'imagen/', 'galeria/']

# ============ FUNCIONES ============

def get_service_images_from_html():
    """Obtiene todas las imágenes de servicio referenciadas en archivos HTML."""
    service_images = {}  # filename -> set of html files
    
    # Buscar en todos los HTML del root
    html_files = glob.glob('*.html') + glob.glob('comunas/*.html', recursive=True)
    
    for f in html_files:
        basename = os.path.basename(f)
        # Saltar páginas no-servicio
        skip = ['sitemap.xml', 'google7a5c4682e9b25d4f.html', 'robots.txt']
        if basename in skip:
            continue
            
        try:
            with open(f, 'r', encoding='utf-8') as fh:
                content = fh.read()
        except:
            continue
            
        # Buscar imágenes de servicio en images/ directamente (no subdirectorios)
        matches = re.findall(r'images/([a-zA-Z0-9_\-]+\.(?:jpg|jpeg|png))', content)
        for m in matches:
            if m in IMAGENES_PROTEGIDAS:
                continue
            if m not in service_images:
                service_images[m] = []
            service_images[m].append(f)
    
    return service_images


def build_mapping(old_images, new_names):
    """
    Construye mapeo inteligente entre imágenes viejas y nuevas.
    Intenta emparejar por servicio y ubicación cuando es posible.
    """
    # Definir categorías de servicio para matching
    service_categories = {
        'aceite': ['cambio-de-aceite', 'cambio-aceite', 'cambio-de-aceite'],
        'frenos': ['cambio-de-frenos', 'cambio-frenos', 'frenos', 'frenos-y-pastillas', 'frenos-pastillas'],
        'pastillas': ['cambio-de-pastillas'],
        'bujias': ['cambio-de-bujias'],
        'amortiguadores': ['cambio-de-amortiguadores'],
        'correa': ['cambio-de-correa-de-distribucion', 'correa-distribucion'],
        'discos': ['cambio-de-discos-de-freno'],
        'filtros': ['cambio-de-filtros'],
        'bateria': ['cambio-de-bateria', 'bateria', 'servicio-de-bateria'],
        'alineacion': ['alineacion-y-balanceo', 'ajuste-de-suspension', 'suspension'],
        'scanner': ['scanner-automotriz', 'scanner', 'scanner-multimarca', 'scanner-motor', 'diagnostico-scanner'],
        'emergencia': ['auxilio-mecanico', 'emergencias-mecanicas', 'mecanico-urgencia', 'mecanico-24-horas'],
        'aire': ['aire-acondicionado'],
        'diagnostico': ['diagnostico-automotriz', 'diagnostico-electrico', 'electricidad-automotriz'],
        'embrague': ['reparacion-de-embrague', 'embrague'],
        'motor': ['reparacion-de-motor', 'compresion-de-motor', 'afinamiento-motor', 'afinamiento'],
        'inspeccion': ['inspeccion-mecanica', 'inspeccion-pre-compra', 'inspeccion-compra', 'inspeccion', 'revision-tecnica'],
        'mantencion': ['mantencion-automotriz', 'mantencion-a-domicilio', 'mantencion-preventiva', 'mantenimiento'],
        'mecanico': ['mecanico-a-domicilio', 'taller-mecanico', 'mecanico-domicilio', 'mecanico-express', 'mecanico'],
        'suspension': ['suspension-y-direccion', 'tren-delantero'],
        'transmision': ['transmision-automatica'],
        'reparacion': ['reparacion-transmision', 'reparacion'],
    }
    
    # Intentar matching semántico
    mapping = {}
    used_new = set()
    unmatched_old = list(old_images.keys())
    
    # Primera pasada: matching por ubicación exacta
    for old_name in list(unmatched_old):
        old_lower = old_name.lower()
        # Extraer ubicación del nombre viejo
        location = None
        for loc in ['puente-alto', 'san-bernardo', 'la-florida', 'maipu', 'las-condes', 
                     'providencia', 'nunoa', 'quilicura', 'penalolen', 'pudahuel', 'recoleta',
                     'san-miguel', 'estacion-central', 'la-cisterna', 'san-ramon', 'cerrillos',
                     'renca', 'conchali', 'el-bosque', 'la-granja', 'lo-espejo', 'lo-prado',
                     'san-joaquin', 'la-pintana', 'pedro-aguirre-cerda', 'independencia',
                     'cerro-navia', 'huechuraba', 'macul', 'vitacura', 'quinta-normal',
                     'santiago-centro', 'buin', 'paine', 'talagante', 'el-monte', 
                     'isla-de-maipo', 'melipilla', 'curacavi', 'maria-pinto', 'colina',
                     'lampa', 'pirque', 'calera-de-tango', 'padre-hurtado', 'penaflor',
                     'tiltil', 'alhue', 'san-pedro', 'san-jose-de-maipo', 'la-reina']:
            if loc in old_lower:
                location = loc
                break
        
        # También buscar marca
        brand = None
        for br in ['chevrolet', 'ford', 'honda', 'hyundai', 'kia', 'mazda', 'mitsubishi', 
                    'nissan', 'peugeot', 'renault', 'subaru', 'suzuki', 'toyota', 'volkswagen',
                    'chevrolet-sail', 'chevrolet-sonic', 'chevrolet-spark', 'ford-ecosport', 
                    'ford-fiesta', 'honda-city', 'honda-civic', 'honda-cr-v', 'hyundai-accent',
                    'hyundai-grand-i10', 'hyundai-tucson', 'kia-morning', 'kia-rio', 'mazda-3',
                    'mazda-cx-5', 'mg-3', 'mg-zs', 'nissan-kicks', 'nissan-versa', 'peugeot-208',
                    'peugeot-3008', 'renault-duster', 'renault-logan', 'subaru-forester', 
                    'subaru-xv', 'suzuki-baleno', 'suzuki-celerio', 'suzuki-swift',
                    'toyota-corolla', 'toyota-yaris', 'volkswagen-gol', 'fiat-bravo-tjet']:
            if br in old_lower:
                brand = br
                break
        
        # Buscar mejor match en nuevos nombres
        best_match = None
        best_score = 0
        
        for i, new_name in enumerate(new_names):
            if i in used_new:
                continue
            new_lower = new_name.lower()
            score = 0
            
            if location and location in new_lower:
                score += 10
            if brand and brand in new_lower:
                score += 15
            
            # Matching por tipo de servicio
            for cat_key, cat_aliases in service_categories.items():
                for alias in cat_aliases:
                    if alias in old_lower and alias in new_lower:
                        score += 8
                    elif alias in old_lower and any(a in new_lower for a in cat_aliases):
                        score += 5
            
            if score > best_score:
                best_score = score
                best_match = i
        
        if best_match is not None and best_score >= 5:
            mapping[old_name] = new_names[best_match]
            used_new.add(best_match)
            unmatched_old.remove(old_name)
    
    # Segunda pasada: asignar los restantes en orden
    remaining_new = [(i, name) for i, name in enumerate(new_names) if i not in used_new]
    for old_name in unmatched_old:
        if remaining_new:
            idx, new_name = remaining_new.pop(0)
            mapping[old_name] = new_name
        else:
            print(f"WARNING: No hay suficientes nombres nuevos para {old_name}")
    
    return mapping


def replace_in_files(mapping):
    """Reemplaza nombres de imágenes en todos los archivos HTML."""
    stats = {'files_modified': 0, 'replacements': 0}
    
    # Obtener todos los HTML a procesar
    html_dirs = ['', 'comunas']
    all_html = []
    for d in html_dirs:
        pattern = os.path.join(d, '*.html') if d else '*.html'
        all_html.extend(glob.glob(pattern))
    
    for filepath in all_html:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            continue
        
        original = content
        for old_name, new_name in mapping.items():
            # Reemplazar en todas las formas: images/old.jpg -> images/new.jpg
            content = content.replace(f'images/{old_name}', f'images/{new_name}')
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            stats['files_modified'] += 1
            # Contar reemplazos
            for old_name in mapping:
                count = original.count(f'images/{old_name}')
                if count > 0:
                    stats['replacements'] += count
                    print(f"  {filepath}: images/{old_name} -> images/{mapping[old_name]} ({count}x)")
    
    return stats


def update_nombres_file(new_names):
    """Actualiza el archivo nombres-imagenes-seo.txt con los nuevos nombres."""
    with open('nombres-imagenes-seo.txt', 'w', encoding='utf-8') as f:
        for name in new_names:
            f.write(name + '\n')
    print(f"\nArchivo nombres-imagenes-seo.txt actualizado con {len(new_names)} nombres.")


# ============ MAIN ============

if __name__ == '__main__':
    print("=" * 70)
    print("REEMPLAZO DE IMÁGENES SEO - LLANOCAR")
    print("=" * 70)
    
    # 1. Obtener imágenes actuales de servicio
    print("\n[1/4] Escaneando imágenes de servicio en HTML files...")
    service_images = get_service_images_from_html()
    old_names = sorted(service_images.keys())
    print(f"  Encontradas {len(old_names)} imágenes de servicio únicas")
    
    # 2. Construir mapeo
    print(f"\n[2/4] Construyendo mapeo ({len(old_names)} viejas -> {len(NUEVOS_NOMBRES_SEO)} nuevas)...")
    mapping = build_mapping(service_images, NUEVOS_NOMBRES_SEO)
    print(f"  Mapeo creado: {len(mapping)} imágenes")
    
    # Mostrar algunos ejemplos del mapeo
    print("\n  Ejemplos del mapeo:")
    for i, (old, new) in enumerate(list(mapping.items())[:10]):
        print(f"    {old} -> {new}")
    if len(mapping) > 10:
        print(f"    ... y {len(mapping) - 10} más")
    
    # 3. Ejecutar reemplazo
    print(f"\n[3/4] Reemplazando en archivos HTML...")
    stats = replace_in_files(mapping)
    print(f"  Archivos modificados: {stats['files_modified']}")
    print(f"  Reemplazos totales: {stats['replacements']}")
    
    # 4. Actualizar archivo de nombres
    print(f"\n[4/4] Actualizando nombres-imagenes-seo.txt...")
    update_nombres_file(NUEVOS_NOMBRES_SEO)
    
    print("\n" + "=" * 70)
    print("COMPLETADO")
    print("=" * 70)
