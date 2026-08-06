#!/usr/bin/env python3
"""
Inyecta un modal con mapa interactivo de la Región Metropolitana
en la sección zonas-section del index.html.

Funcionalidades:
- Botón "Ver mapa interactivo" en la sección de comunas
- Modal fullscreen con:
  - Mapa Leaflet (tema dark) con todas las comunas como marcadores
  - Lista lateral con todas las comunas (responsive)
- Clic en comuna de la lista → resalta marcador en el mapa + popup
- Clic en marcador → muestra popup con "Ver página"
- Clic en "Ver página" del popup → va a /comunas/[slug].html
- Botón cerrar (X) + click fuera + tecla ESC
"""
import re
from pathlib import Path

INDEX = Path(__file__).resolve().parent / "index.html"

# Coordenadas de las comunas de la RM (centro aproximado de cada una)
COMUNAS = {
    "alhue": {"nombre": "Alhué", "lat": -33.8750, "lng": -71.0833},
    "buin": {"nombre": "Buin", "lat": -33.7324, "lng": -70.7445},
    "calera-de-tango": {"nombre": "Calera de Tango", "lat": -33.8828, "lng": -70.7920},
    "cerrillos": {"nombre": "Cerrillos", "lat": -33.5020, "lng": -70.7250},
    "cerro-navia": {"nombre": "Cerro Navia", "lat": -33.5100, "lng": -70.7100},
    "colina": {"nombre": "Colina", "lat": -33.3500, "lng": -70.7167},
    "conchali": {"nombre": "Conchalí", "lat": -33.4670, "lng": -70.6830},
    "curacavi": {"nombre": "Curacaví", "lat": -33.4400, "lng": -71.1333},
    "el-bosque": {"nombre": "El Bosque", "lat": -33.5700, "lng": -70.7000},
    "el-monte": {"nombre": "El Monte", "lat": -33.6800, "lng": -70.9500},
    "estacion-central": {"nombre": "Estación Central", "lat": -33.4630, "lng": -70.7030},
    "huechuraba": {"nombre": "Huechuraba", "lat": -33.4100, "lng": -70.6800},
    "independencia": {"nombre": "Independencia", "lat": -33.4700, "lng": -70.6830},
    "isla-de-maipo": {"nombre": "Isla de Maipo", "lat": -33.7500, "lng": -70.9000},
    "la-cisterna": {"nombre": "La Cisterna", "lat": -33.5300, "lng": -70.7000},
    "la-florida": {"nombre": "La Florida", "lat": -33.5500, "lng": -70.5800},
    "la-granja": {"nombre": "La Granja", "lat": -33.5400, "lng": -70.6300},
    "la-pintana": {"nombre": "La Pintana", "lat": -33.5800, "lng": -70.5700},
    "la-reina": {"nombre": "La Reina", "lat": -33.4500, "lng": -70.5500},
    "lampa": {"nombre": "Lampa", "lat": -33.2800, "lng": -70.8667},
    "las-condes": {"nombre": "Las Condes", "lat": -33.4100, "lng": -70.5500},
    "lo-barnechea": {"nombre": "Lo Barnechea", "lat": -33.3600, "lng": -70.5200},
    "lo-espejo": {"nombre": "Lo Espejo", "lat": -33.5200, "lng": -70.7300},
    "lo-prado": {"nombre": "Lo Prado", "lat": -33.4900, "lng": -70.7200},
    "macul": {"nombre": "Macul", "lat": -33.5000, "lng": -70.6000},
    "maipu": {"nombre": "Maipú", "lat": -33.5100, "lng": -70.7600},
    "maria-pinto": {"nombre": "María Pinto", "lat": -33.6500, "lng": -71.0500},
    "melipilla": {"nombre": "Melipilla", "lat": -33.6833, "lng": -71.2167},
    "nunoa": {"nombre": "Ñuñoa", "lat": -33.4600, "lng": -70.6000},
    "padre-hurtado": {"nombre": "Padre Hurtado", "lat": -33.5800, "lng": -70.8500},
    "paine": {"nombre": "Paine", "lat": -33.8000, "lng": -70.7333},
    "pedro-aguirre-cerda": {"nombre": "Pedro Aguirre Cerda", "lat": -33.5000, "lng": -70.6700},
    "penaflor": {"nombre": "Peñaflor", "lat": -33.6167, "lng": -70.8833},
    "penalolen": {"nombre": "Peñalolén", "lat": -33.4900, "lng": -70.5700},
    "pirque": {"nombre": "Pirque", "lat": -33.6333, "lng": -70.5833},
    "providencia": {"nombre": "Providencia", "lat": -33.4400, "lng": -70.6100},
    "pudahuel": {"nombre": "Pudahuel", "lat": -33.4300, "lng": -70.7800},
    "puente-alto": {"nombre": "Puente Alto", "lat": -33.6200, "lng": -70.5800},
    "quilicura": {"nombre": "Quilicura", "lat": -33.3600, "lng": -70.7300},
    "quinta-normal": {"nombre": "Quinta Normal", "lat": -33.4500, "lng": -70.7000},
    "recoleta": {"nombre": "Recoleta", "lat": -33.4300, "lng": -70.6400},
    "renca": {"nombre": "Renca", "lat": -33.4100, "lng": -70.7300},
    "san-bernardo": {"nombre": "San Bernardo", "lat": -33.5900, "lng": -70.7000},
    "san-joaquin": {"nombre": "San Joaquín", "lat": -33.5000, "lng": -70.6300},
    "san-jose-de-maipo": {"nombre": "San José de Maipo", "lat": -33.6333, "lng": -70.3667},
    "san-miguel": {"nombre": "San Miguel", "lat": -33.4900, "lng": -70.6600},
    "san-pedro": {"nombre": "San Pedro", "lat": -33.9167, "lng": -71.0000},
    "san-ramon": {"nombre": "San Ramón", "lat": -33.5400, "lng": -70.5800},
    "santiago": {"nombre": "Santiago", "lat": -33.4500, "lng": -70.6667},
    "talagante": {"nombre": "Talagante", "lat": -33.6667, "lng": -70.9333},
    "tiltil": {"nombre": "Til Til", "lat": -33.0833, "lng": -70.9167},
    "vitacura": {"nombre": "Vitacura", "lat": -33.4000, "lng": -70.6000},
}

INJECTION = '''
<!-- ============================================================ -->
<!-- MODAL MAPA INTERACTIVO DE COMUNAS -->
<!-- ============================================================ -->
<style>
/* Modal overlay */
.modal-comunas-overlay {
  display: none;
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  z-index: 99999;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.modal-comunas-overlay.active {
  display: flex !important;
  align-items: center;
  justify-content: center;
  opacity: 1;
}

/* Modal container */
.modal-comunas {
  background: #0F0F0F;
  border: 1px solid #2A2A2A;
  border-radius: 16px;
  width: 95vw;
  max-width: 1200px;
  height: 90vh;
  max-height: 800px;
  box-shadow: 0 25px 80px rgba(0, 0, 0, 0.7), 0 0 0 1px rgba(232, 119, 34, 0.2);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  transform: scale(0.9);
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.modal-comunas-overlay.active .modal-comunas {
  transform: scale(1);
}

/* Modal header */
.modal-comunas-header {
  background: linear-gradient(135deg, #1A1A1A 0%, #0F0F0F 100%);
  border-bottom: 1px solid #2A2A2A;
  padding: 18px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-shrink: 0;
}

.modal-comunas-title {
  color: #FFFFFF;
  font-size: 1.3rem;
  font-weight: 700;
  margin: 0;
  display: flex;
  align-items: center;
  gap: 10px;
}

.modal-comunas-title::before {
  content: '🗺️';
  font-size: 1.5rem;
}

.modal-comunas-close {
  background: transparent;
  border: 1px solid #3A3A3A;
  color: #FFFFFF;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  font-size: 1.2rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.modal-comunas-close:hover {
  background: #E87722;
  border-color: #E87722;
  transform: rotate(90deg);
}

/* Modal body: layout split */
.modal-comunas-body {
  display: flex;
  flex: 1;
  overflow: hidden;
}

/* Sidebar con lista de comunas */
.modal-comunas-sidebar {
  width: 320px;
  background: #141414;
  border-right: 1px solid #2A2A2A;
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
}

.modal-comunas-search {
  padding: 14px 16px;
  border-bottom: 1px solid #2A2A2A;
  position: relative;
}

.modal-comunas-search input {
  width: 100%;
  background: #1A1A1A;
  border: 1px solid #2A2A2A;
  border-radius: 8px;
  padding: 10px 14px 10px 38px;
  color: #FFFFFF;
  font-size: 0.9rem;
  font-family: inherit;
  outline: none;
  transition: all 0.2s ease;
}

.modal-comunas-search input:focus {
  border-color: #E87722;
  background: #1F1F1F;
}

.modal-comunas-search input::placeholder {
  color: #666;
}

.modal-comunas-search::before {
  content: '🔍';
  position: absolute;
  left: 28px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 0.85rem;
  opacity: 0.6;
}

.modal-comunas-list {
  flex: 1;
  overflow-y: auto;
  padding: 8px;
}

.modal-comunas-list::-webkit-scrollbar {
  width: 6px;
}

.modal-comunas-list::-webkit-scrollbar-track {
  background: #0F0F0F;
}

.modal-comunas-list::-webkit-scrollbar-thumb {
  background: #2A2A2A;
  border-radius: 3px;
}

.modal-comunas-list::-webkit-scrollbar-thumb:hover {
  background: #E87722;
}

/* Item de comuna en la lista */
.modal-comuna-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 14px;
  margin-bottom: 4px;
  background: #1A1A1A;
  border: 1px solid transparent;
  border-radius: 6px;
  color: #E0E0E0;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 500;
  transition: all 0.2s ease;
}

.modal-comuna-item:hover {
  background: #1F1F1F;
  border-color: #E87722;
  color: #FFFFFF;
  transform: translateX(4px);
}

.modal-comuna-item.active {
  background: #E87722;
  border-color: #E87722;
  color: #FFFFFF;
  font-weight: 700;
  box-shadow: 0 4px 12px rgba(232, 119, 34, 0.4);
}

.modal-comuna-item::before {
  content: '📍';
  font-size: 0.85rem;
  opacity: 0.8;
}

.modal-comuna-item.active::before {
  opacity: 1;
}

/* Contenedor del mapa */
.modal-comunas-map-container {
  flex: 1;
  position: relative;
  background: #0A0A0A;
}

#modal-map-llanocar {
  width: 100%;
  height: 100%;
  background: #0A0A0A;
}

/* Leaflet custom dark theme */
.leaflet-container {
  background: #0A0A0A !important;
  font-family: 'Space Grotesk', -apple-system, sans-serif !important;
}

.leaflet-tile {
  filter: invert(1) hue-rotate(180deg) brightness(0.85) contrast(0.95) !important;
}

.leaflet-control-zoom a {
  background: #1A1A1A !important;
  color: #FFFFFF !important;
  border: 1px solid #2A2A2A !important;
  border-radius: 4px !important;
}

.leaflet-control-zoom a:hover {
  background: #E87722 !important;
  color: #FFFFFF !important;
  border-color: #E87722 !important;
}

.leaflet-popup-content-wrapper {
  background: #1A1A1A !important;
  color: #FFFFFF !important;
  border: 1px solid #E87722 !important;
  border-radius: 10px !important;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6) !important;
}

.leaflet-popup-tip {
  background: #1A1A1A !important;
  border: 1px solid #E87722 !important;
}

.leaflet-popup-content {
  margin: 14px 18px !important;
  font-family: 'Space Grotesk', sans-serif !important;
  text-align: center;
}

.leaflet-popup-content strong {
  color: #E87722 !important;
  font-size: 1.1rem !important;
  display: block !important;
  margin-bottom: 6px !important;
  font-weight: 700 !important;
}

.leaflet-popup-content .popup-desc {
  color: #B0B0B0 !important;
  font-size: 0.85rem !important;
  margin-bottom: 10px !important;
  display: block !important;
}

.leaflet-popup-content a.popup-link {
  display: inline-block !important;
  background: #E87722 !important;
  color: #FFFFFF !important;
  padding: 8px 16px !important;
  border-radius: 6px !important;
  text-decoration: none !important;
  font-weight: 700 !important;
  font-size: 0.85rem !important;
  text-transform: uppercase !important;
  letter-spacing: 0.05em !important;
  transition: all 0.2s ease !important;
}

.leaflet-popup-content a.popup-link:hover {
  background: #FF8C42 !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 6px 16px rgba(232, 119, 34, 0.5) !important;
}

/* Marcador custom */
.modal-comuna-marker {
  background: transparent !important;
  border: none !important;
}

.modal-comuna-marker-inner {
  width: 20px;
  height: 20px;
  background: #E87722;
  border: 3px solid #FFFFFF;
  border-radius: 50%;
  box-shadow: 0 0 12px rgba(232, 119, 34, 0.6), 0 2px 6px rgba(0, 0, 0, 0.4);
  transition: all 0.3s ease;
  cursor: pointer;
}

.modal-comuna-marker-inner.active {
  background: #FF8C42;
  transform: scale(1.5);
  box-shadow: 0 0 25px rgba(232, 119, 34, 1), 0 4px 12px rgba(0, 0, 0, 0.5);
}

.modal-comuna-marker-inner.active::after {
  content: '';
  position: absolute;
  top: -10px; left: -10px;
  right: -10px; bottom: -10px;
  border: 2px solid #E87722;
  border-radius: 50%;
  animation: modal-pulse 1.5s infinite;
}

@keyframes modal-pulse {
  0% { transform: scale(1); opacity: 1; }
  100% { transform: scale(1.8); opacity: 0; }
}

/* Botón "Ver mapa interactivo" en zonas-section */
.btn-mapa-interactivo {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: linear-gradient(135deg, #E87722 0%, #FF8C42 100%);
  color: #FFFFFF !important;
  border: none;
  padding: 14px 32px;
  border-radius: 10px;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  text-decoration: none;
  text-transform: uppercase;
  letter-spacing: 0.03em;
  box-shadow: 0 6px 20px rgba(232, 119, 34, 0.4);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  margin-top: 24px;
}

.btn-mapa-interactivo:hover {
  transform: translateY(-3px) scale(1.03);
  box-shadow: 0 10px 30px rgba(232, 119, 34, 0.6);
  background: linear-gradient(135deg, #FF8C42 0%, #FFA563 100%);
  color: #FFFFFF !important;
}

.btn-mapa-interactivo::before {
  content: '🗺️';
  font-size: 1.2rem;
}

/* Responsive */
@media (max-width: 768px) {
  .modal-comunas {
    width: 100vw;
    height: 100vh;
    max-width: 100vw;
    max-height: 100vh;
    border-radius: 0;
  }
  
  .modal-comunas-body {
    flex-direction: column;
  }
  
  .modal-comunas-sidebar {
    width: 100%;
    height: 40%;
    border-right: none;
    border-bottom: 1px solid #2A2A2A;
  }
  
  .modal-comunas-map-container {
    height: 60%;
  }
  
  .modal-comunas-title {
    font-size: 1.1rem;
  }
  
  .btn-mapa-interactivo {
    padding: 12px 24px;
    font-size: 0.9rem;
  }
}
</style>

<!-- Botón que abre el modal -->
<div class="text-center" style="margin-top: 20px;">
  <button id="btn-abrir-mapa-comunas" class="btn-mapa-interactivo">
    Ver mapa interactivo de comunas
  </button>
</div>

<!-- Modal -->
<div class="modal-comunas-overlay" id="modal-comunas-overlay">
  <div class="modal-comunas">
    <div class="modal-comunas-header">
      <h3 class="modal-comunas-title">Comunas — Región Metropolitana</h3>
      <button class="modal-comunas-close" id="modal-comunas-close" aria-label="Cerrar">✕</button>
    </div>
    <div class="modal-comunas-body">
      <div class="modal-comunas-sidebar">
        <div class="modal-comunas-search">
          <input type="text" id="modal-comunas-search-input" placeholder="Buscar comuna..." />
        </div>
        <div class="modal-comunas-list" id="modal-comunas-list">
          <!-- Se llena con JS -->
        </div>
      </div>
      <div class="modal-comunas-map-container">
        <div id="modal-map-llanocar"></div>
      </div>
    </div>
  </div>
</div>

<!-- Leaflet JS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.4/dist/leaflet.js"></script>

<script>
(function() {
  const COMUNAS = __COMUNAS_JSON__;
  const DOMAIN = window.location.origin;
  
  let map = null;
  let markers = {};
  let activeSlug = null;
  let modalInitialized = false;
  
  // ========== INICIALIZAR MODAL ==========
  function initModal() {
    if (modalInitialized) return;
    modalInitialized = true;
    
    // Crear mapa
    map = L.map('modal-map-llanocar', {
      center: [-33.45, -70.65],
      zoom: 10,
      zoomControl: true,
      scrollWheelZoom: true
    });
    
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; OpenStreetMap',
      maxZoom: 18
    }).addTo(map);
    
    // Custom icon
    const customIcon = L.divIcon({
      className: 'modal-comuna-marker',
      html: '<div class="modal-comuna-marker-inner"></div>',
      iconSize: [20, 20],
      iconAnchor: [10, 10]
    });
    
    // Crear markers
    Object.entries(COMUNAS).forEach(([slug, data]) => {
      const marker = L.marker([data.lat, data.lng], { icon: customIcon })
        .addTo(map)
        .bindPopup(`
          <strong>${data.nombre}</strong>
          <span class="popup-desc">Mecánico a domicilio 24/7</span>
          <a href="${DOMAIN}/comunas/${slug}.html" class="popup-link">Ver página →</a>
        `);
      
      marker.on('click', function() {
        setActiveComuna(slug);
      });
      
      markers[slug] = marker;
    });
    
    // Llenar lista
    const listContainer = document.getElementById('modal-comunas-list');
    Object.entries(COMUNAS).forEach(([slug, data]) => {
      const item = document.createElement('div');
      item.className = 'modal-comuna-item';
      item.dataset.slug = slug;
      item.dataset.nombre = data.nombre.toLowerCase();
      item.textContent = data.nombre;
      
      item.addEventListener('click', function() {
        if (activeSlug === slug) {
          // Segundo clic → ir a la página
          window.location.href = `${DOMAIN}/comunas/${slug}.html`;
        } else {
          // Primer clic → resaltar en mapa
          setActiveComuna(slug);
          // Hacer zoom al marcador
          map.flyTo([data.lat, data.lng], 13, { duration: 1.0 });
          setTimeout(() => {
            markers[slug].openPopup();
          }, 600);
        }
      });
      
      listContainer.appendChild(item);
    });
    
    // Búsqueda
    const searchInput = document.getElementById('modal-comunas-search-input');
    searchInput.addEventListener('input', function() {
      const query = this.value.toLowerCase();
      document.querySelectorAll('.modal-comuna-item').forEach(item => {
        const nombre = item.dataset.nombre;
        item.style.display = nombre.includes(query) ? 'flex' : 'none';
      });
    });
  }
  
  function setActiveComuna(slug) {
    // Remover active de todos
    Object.values(markers).forEach(m => {
      const el = m.getElement();
      if (el) {
        const inner = el.querySelector('.modal-comuna-marker-inner');
        if (inner) inner.classList.remove('active');
      }
    });
    document.querySelectorAll('.modal-comuna-item').forEach(i => i.classList.remove('active'));
    
    // Activar este
    const marker = markers[slug];
    if (marker) {
      const el = marker.getElement();
      if (el) {
        const inner = el.querySelector('.modal-comuna-marker-inner');
        if (inner) inner.classList.add('active');
      }
    }
    const item = document.querySelector(`.modal-comuna-item[data-slug="${slug}"]`);
    if (item) {
      item.classList.add('active');
      item.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
    activeSlug = slug;
  }
  
  // ========== ABRIR/CERRAR MODAL ==========
  const overlay = document.getElementById('modal-comunas-overlay');
  const btnAbrir = document.getElementById('btn-abrir-mapa-comunas');
  const btnCerrar = document.getElementById('modal-comunas-close');
  
  function abrirModal() {
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
    
    // Inicializar el mapa solo cuando se abre (evita problemas de render)
    setTimeout(() => {
      initModal();
      map.invalidateSize();
    }, 100);
  }
  
  function cerrarModal() {
    overlay.classList.remove('active');
    document.body.style.overflow = '';
  }
  
  btnAbrir.addEventListener('click', abrirModal);
  btnCerrar.addEventListener('click', cerrarModal);
  
  // Click fuera del modal → cerrar
  overlay.addEventListener('click', function(e) {
    if (e.target === overlay) cerrarModal();
  });
  
  // ESC → cerrar
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && overlay.classList.contains('active')) {
      cerrarModal();
    }
  });
})();
</script>
'''


def main():
    print("Inyectando modal de mapa interactivo en index.html...")
    print("=" * 60)
    
    if not INDEX.exists():
        print(f"✗ No encontrado: {INDEX}")
        return
    
    content = INDEX.read_text(encoding="utf-8", errors="replace")
    
    # Verificar si ya tiene el modal
    if 'id="modal-comunas-overlay"' in content:
        print("  ⚠ El modal ya está inyectado, saltando")
        return
    
    # Generar JSON de comunas
    import json
    comunas_json = json.dumps(COMUNAS, ensure_ascii=False, indent=2)
    injection_html = INJECTION.replace("__COMUNAS_JSON__", comunas_json)
    
    # Insertar antes del cierre de la sección zonas-section
    # Buscar </section> después de la sección zonas-section
    zonas_match = re.search(r'<section class="zonas-section">.*?</section>', content, re.DOTALL | re.IGNORECASE)
    if zonas_match:
        # Insertar el modal justo antes del </section> de zonas-section
        insert_pos = zonas_match.end() - len('</section>')
        modified = content[:insert_pos] + injection_html + '\n' + content[insert_pos:]
        INDEX.write_text(modified, encoding="utf-8")
        print(f"  ✓ Modal inyectado en zonas-section (posición {insert_pos})")
    else:
        # Si no encuentra la sección, insertar antes de </body>
        modified = re.sub(r'(</body>)', injection_html + r'\n\1', content, count=1)
        INDEX.write_text(modified, encoding="utf-8")
        print(f"  ⚠ No se encontró zonas-section, inyectado antes de </body>")
    
    print()
    print("✓ Modal de mapa interactivo inyectado correctamente")
    print("  Funcionalidades:")
    print("    - Botón 'Ver mapa interactivo de comunas' en sección zonas")
    print("    - Modal con mapa Leaflet (tema dark) + lista lateral")
    print("    - 52 marcadores de comunas con popups")
    print("    - Buscador de comunas en la lista")
    print("    - Clic en comuna de lista → resalta en mapa + flyTo + popup")
    print("    - Segundo clic en comuna → va a la página de la comuna")
    print("    - Clic en marcador → muestra popup con 'Ver página →'")
    print("    - Cerrar con X, click fuera, o tecla ESC")


if __name__ == "__main__":
    main()
