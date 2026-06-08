#!/usr/bin/env python3
"""
SEO Round 2 for LLANOCAR (llanocar.pages.dev)
- Adds H2 sections with UNIQUE content (different wording from other repositories)
- H2 in Spanish, then same H2 in English in italics/parentheses below
- No separate English pages; bilingual in one page
- Comunas: 47 pages
- Vehiculos: 32 pages (excluding index.html)
"""

import os, re, glob

BASE = "/home/z/my-project/llanocar"
COMUNAS_DIR = os.path.join(BASE, "comunas")
VEHICULOS_DIR = os.path.join(BASE, "vehiculos")

# WhatsApp number for LLANOCAR
WHATSAPP = "56933261085"
BRAND = "LLANOCAR"

# ─── Comuna name mapping (slug → display name) ───
COMUNA_NAMES = {
    "alhue": "Alhué",
    "buin": "Buín",
    "calera-de-tango": "Calera de Tango",
    "cerrillos": "Cerrillos",
    "cerro-navia": "Cerro Navia",
    "colina": "Colina",
    "conchali": "Conchalí",
    "curacavi": "Curacaví",
    "el-bosque": "El Bosque",
    "el-monte": "El Monte",
    "estacion-central": "Estación Central",
    "independencia": "Independencia",
    "isla-de-maipo": "Isla de Maipo",
    "la-cisterna": "La Cisterna",
    "la-florida": "La Florida",
    "la-granja": "La Granja",
    "la-pintana": "La Pintana",
    "lampa": "Lampa",
    "lo-espejo": "Lo Espejo",
    "lo-prado": "Lo Prado",
    "macul": "Macul",
    "maipu": "Maipú",
    "maria-pinto": "María Pinto",
    "melipilla": "Melipilla",
    "nunoa": "Ñuñoa",
    "padre-hurtado": "Padre Hurtado",
    "paine": "Paine",
    "pedro-aguirre-cerda": "Pedro Aguirre Cerda",
    "penaflor": "Peñaflor",
    "penalolen": "Peñalolén",
    "pirque": "Pirque",
    "providencia": "Providencia",
    "pudahuel": "Pudahuel",
    "puente-alto": "Puente Alto",
    "quilicura": "Quilicura",
    "quinta-normal": "Quinta Normal",
    "recoleta": "Recoleta",
    "renca": "Renca",
    "san-bernardo": "San Bernardo",
    "san-joaquin": "San Joaquín",
    "san-jose-de-maipo": "San José de Maipo",
    "san-miguel": "San Miguel",
    "san-pedro": "San Pedro",
    "san-ramon": "San Ramón",
    "santiago": "Santiago",
    "talagante": "Talagante",
    "tiltil": "Tiltil",
}

# ─── Vehicle name mapping (slug → display name) ───
VEHICLE_NAMES = {
    "chevrolet-sail": "Chevrolet Sail",
    "chevrolet-sonic": "Chevrolet Sonic",
    "chevrolet-spark": "Chevrolet Spark",
    "fiat-bravo-tjet": "Fiat Bravo T-Jet",
    "ford-ecosport": "Ford EcoSport",
    "ford-fiesta": "Ford Fiesta",
    "honda-city": "Honda City",
    "honda-civic": "Honda Civic",
    "honda-cr-v": "Honda CR-V",
    "hyundai-accent": "Hyundai Accent",
    "hyundai-grand-i10": "Hyundai Grand i10",
    "hyundai-tucson": "Hyundai Tucson",
    "kia-morning": "Kia Morning",
    "kia-rio": "Kia Rio",
    "mazda-3": "Mazda 3",
    "mazda-cx-5": "Mazda CX-5",
    "mg-3": "MG 3",
    "mg-zs": "MG ZS",
    "nissan-kicks": "Nissan Kicks",
    "nissan-versa": "Nissan Versa",
    "peugeot-208": "Peugeot 208",
    "peugeot-3008": "Peugeot 3008",
    "renault-duster": "Renault Duster",
    "renault-logan": "Renault Logan",
    "subaru-forester": "Subaru Forester",
    "subaru-xv": "Subaru XV",
    "suzuki-baleno": "Suzuki Baleno",
    "suzuki-celerio": "Suzuki Celerio",
    "suzuki-swift": "Suzuki Swift",
    "toyota-corolla": "Toyota Corolla",
    "toyota-yaris": "Toyota Yaris",
    "volkswagen-gol": "Volkswagen Gol",
}


def build_comuna_h2_blocks(comuna):
    """
    Build 8 H2 blocks for a comuna page.
    Content is UNIQUE - uses synonyms and different phrasing from other repositories.
    Format: H2 in Spanish, then same H2 in English in italics/parentheses below.
    """

    blocks = []

    # ──────────────────────────────────────────────────────────────
    # H2-1: Taller Mecánico Cerca de Mí en [Comuna] (improved)
    # ──────────────────────────────────────────────────────────────
    h2_es = f"Taller Mecánico Cerca de Mí en {comuna}"
    h2_en = f"Mechanic Shop Near Me in {comuna}"
    content = f"""<section class="seo-section" style="background-color:#fff; padding:50px 0;">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2 class="seo-h2" style="color:#E87722; font-size:1.7rem; font-weight:700; margin-bottom:8px;">{h2_es}</h2>
        <p style="font-style:italic; color:#888; font-size:1rem; margin-bottom:20px;">({h2_en})</p>
        <div class="seo-text">
          <p>Si estás buscando un <strong>taller mecánico cerca de mí en {comuna}</strong>, {BRAND} es tu alternativa de confianza. Nuestros operarios calificados concurren hasta tu domicilio o lugar de trabajo en <strong>{comuna}</strong> con instrumental técnico de vanguardia para solucionar cualquier inconveniente mecánico sin que debas acudir a un establecimiento físico. Somos especialistas en reparaciones de motor, sistema de frenado, inyección electrónica y diagnóstico computarizado, atendiendo todas las marcas y modelos que circulan por <strong>{comuna}</strong> y la Región Metropolitana.</p>
          <p>Contamos con más de 15 años de trayectoria y miles de vehículos atendidos, lo que nos convierte en una opción sólida cuando necesitas un <strong>taller mecánico en {comuna}</strong> que responda de manera expedita. Nuestro compromiso es brindarte un servicio honesto, con presupuestos sin sorpresas y garantía en cada intervención. Puedes agendar tu cita por WhatsApp y en menos de 24 horas un profesional estará en la puerta de tu hogar en <strong>{comuna}</strong>.</p>
          <p>Ya se trate de una mantención programada o de una urgencia inesperada, nuestro equipo está equipado para resolver in situ. Evita los tiempos de espera y el traslado de tu automóvil: contrata el servicio de <strong>taller mecánico cerca de mí en {comuna}</strong> que te ofrece {BRAND} y recupera la tranquilidad al volante.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    blocks.append(content)

    # ──────────────────────────────────────────────────────────────
    # H2-2: Mecánico Cerca de Mí en [Comuna] — Asistencia a Domicilio
    # ──────────────────────────────────────────────────────────────
    h2_es = f"Mecánico Cerca de Mí en {comuna} — Asistencia a Domicilio"
    h2_en = f"Mechanic Near Me in {comuna} — Mobile Mechanic Service"
    content = f"""<section class="seo-section" style="background-color:#f8f9fa; padding:50px 0; border-top:3px solid #E87722;">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2 class="seo-h2" style="color:#E87722; font-size:1.7rem; font-weight:700; margin-bottom:8px;">{h2_es}</h2>
        <p style="font-style:italic; color:#888; font-size:1rem; margin-bottom:20px;">({h2_en})</p>
        <div class="seo-text">
          <p>Encontrar un <strong>mecánico cerca de mí en {comuna}</strong> ya no es un problema. En {BRAND} disponemos de técnicos que se desplazan a cualquier punto de <strong>{comuna}</strong> en horario diurno y nocturno, incluyendo fines de semana y festivos. Nuestra cobertura abarca desde la zona céntrica hasta los barrios periféricos de la comuna, garantizando una llegada rápida y eficiente para cualquier tipo de avería o mantención.</p>
          <p>La ventaja de contar con un <strong>mecánico a domicilio en {comuna}</strong> es que no necesitas llevar tu automóvil a un taller convencional. Nuestros profesionales portan escáner de diagnóstico, herramientas neumáticas, gato hidráulico y repuestos de uso frecuente, lo que permite resolver la mayoría de las fallas en el mismo instante de la visita. Si el caso requiere una reparación mayor, coordinamos el traslado sin costo adicional.</p>
          <p>No dejes que una falla mecánica arruine tu día. Comunícate por WhatsApp con {BRAND}, el <strong>mecánico cerca de mí en {comuna}</strong> que responde cuando más lo necesitas, con transparencia en los precios y la calidad que tus vecinos ya recomiendan.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    blocks.append(content)

    # ──────────────────────────────────────────────────────────────
    # H2-3: Electricidad Automotriz a Domicilio en [Comuna]
    # ──────────────────────────────────────────────────────────────
    h2_es = f"Electricidad Automotriz a Domicilio en {comuna}"
    h2_en = f"Auto Electrical Service at Home in {comuna}"
    content = f"""<section class="seo-section" style="background-color:#fff; padding:50px 0;">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2 class="seo-h2" style="color:#E87722; font-size:1.7rem; font-weight:700; margin-bottom:8px;">{h2_es}</h2>
        <p style="font-style:italic; color:#888; font-size:1rem; margin-bottom:20px;">({h2_en})</p>
        <div class="seo-text">
          <p>Las fallas eléctricas son una de las causas más frecuentes de averías en los vehículos modernos, y en {BRAND} contamos con técnicos especializados en <strong>electricidad automotriz a domicilio en {comuna}</strong>. Desde problemas en la batería y el alternador hasta fallas en la unidad de control del motor (ECU), sensores de oxígeno, sistema de encendido y cableado, nuestro personal diagnostica y repara en el lugar sin que tengas que mover tu vehículo.</p>
          <p>Los automóviles de última generación incorporan múltiples módulos electrónicos que requieren equipos de escaneo avanzados. En {BRAND} utilizamos escáner profesional de última generación que lee y borra códigos de falla en tiempo real, permitiéndote conocer exactamente qué ocurre con tu carro antes de autorizar cualquier intervención. Este servicio de <strong>electricidad automotriz en {comuna}</strong> es ideal para vehículos que presentan luces testigo encendidas, arranque intermitente o consumos anómalos de energía.</p>
          <p>Si resides en <strong>{comuna}</strong> y tu auto presenta síntomas eléctricos, no lo postergues: una falla menor puede derivar en un daño mayor. Contáctanos por WhatsApp y un electricista automotriz con experiencia llegará hasta tu puerta con la solución.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    blocks.append(content)

    # ──────────────────────────────────────────────────────────────
    # H2-4: Mantención Preventiva a Domicilio en [Comuna]
    # ──────────────────────────────────────────────────────────────
    h2_es = f"Mantención Preventiva a Domicilio en {comuna}"
    h2_en = f"Preventive Maintenance at Home in {comuna}"
    content = f"""<section class="seo-section" style="background-color:#f8f9fa; padding:50px 0; border-top:3px solid #E87722;">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2 class="seo-h2" style="color:#E87722; font-size:1.7rem; font-weight:700; margin-bottom:8px;">{h2_es}</h2>
        <p style="font-style:italic; color:#888; font-size:1rem; margin-bottom:20px;">({h2_en})</p>
        <div class="seo-text">
          <p>La <strong>mantención preventiva a domicilio en {comuna}</strong> es la forma más inteligente de cuidar tu vehículo y evitar reparaciones costosas. En {BRAND} diseñamos planes de mantenimiento adaptados al kilometraje, modelo y año de tu automóvil, cubriendo cambio de aceite y filtros, revisión de líquidos (refrigerante, frenos, dirección), inspección de correas, revisión del estado de pastillas y discos, y control de neumáticos.</p>
          <p>Realizar la <strong>mantención a domicilio en {comuna}</strong> con regularidad extiende la vida útil de tu motor, mejora el rendimiento de combustible y te da la seguridad de circular con un vehículo en condiciones óptimas. Nuestros técnicos se presentan con todo lo necesario: aceites sintéticos y semi-sintéticos de marcas líderes, filtros originales y compatibles, y herramientas de precisión para cada tarea.</p>
          <p>Agendar tu mantención es muy sencillo: envía un mensaje por WhatsApp indicando tu modelo y kilometraje, y te confirmamos un horario que se ajuste a tu rutina en <strong>{comuna}</strong>. La prevención siempre es más económica que la corrección.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    blocks.append(content)

    # ──────────────────────────────────────────────────────────────
    # H2-5: Diagnóstico Automotriz con Scanner en [Comuna]
    # ──────────────────────────────────────────────────────────────
    h2_es = f"Diagnóstico Automotriz con Scanner en {comuna}"
    h2_en = f"Car Diagnostic Scan Service in {comuna}"
    content = f"""<section class="seo-section" style="background-color:#fff; padding:50px 0;">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2 class="seo-h2" style="color:#E87722; font-size:1.7rem; font-weight:700; margin-bottom:8px;">{h2_es}</h2>
        <p style="font-style:italic; color:#888; font-size:1rem; margin-bottom:20px;">({h2_en})</p>
        <div class="seo-text">
          <p>El <strong>diagnóstico automotriz con scanner en {comuna}</strong> es el primer paso para resolver cualquier falla electrónica o mecánica de tu vehículo. En {BRAND} empleamos equipos de escaneo de alta resolución que acceden a todos los módulos del automóvil: motor, transmisión, ABS, airbag, inmovilizador y sistemas de confort. Esto permite identificar con exactitud la causa raíz del problema, evitando reemplazos innecesarios y ahorros significativos para tu bolsillo.</p>
          <p>Si la luz de check engine se encendió en tu tablero, o si percibes fallos en el rendimiento, consumos elevados o ruidos atípicos, nuestro servicio de <strong>scanner automotriz en {comuna}</strong> te proporciona un informe completo con los códigos de falla, su significado y el presupuesto de reparación. Todo esto sin que muevas tu vehículo del lugar donde se encuentre.</p>
          <p>En {BRAND} creemos que la transparencia es fundamental. Por eso, antes de cualquier reparación te mostramos los resultados del escaneo y te explicamos cada detalle. Agenda tu <strong>diagnóstico con scanner en {comuna}</strong> por WhatsApp y recibe atención profesional en menos de 24 horas.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    blocks.append(content)

    # ──────────────────────────────────────────────────────────────
    # H2-6: Taller de Frenos Cerca de Mí en [Comuna]
    # ──────────────────────────────────────────────────────────────
    h2_es = f"Taller de Frenos Cerca de Mí en {comuna}"
    h2_en = f"Brake Repair Shop Near Me in {comuna}"
    content = f"""<section class="seo-section" style="background-color:#f8f9fa; padding:50px 0; border-top:3px solid #E87722;">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2 class="seo-h2" style="color:#E87722; font-size:1.7rem; font-weight:700; margin-bottom:8px;">{h2_es}</h2>
        <p style="font-style:italic; color:#888; font-size:1rem; margin-bottom:20px;">({h2_en})</p>
        <div class="seo-text">
          <p>El sistema de frenado es el componente de seguridad más crítico de tu vehículo, y en {BRAND} ofrecemos un servicio integral de <strong>taller de frenos cerca de mí en {comuna}</strong>. Nuestros mecánicos revisan y reemplazan pastillas, discos, tambores, líquido hidráulico, latiguillos y bombines, utilizando repuestos de primera calidad que cumplen con las normas de fabricación original.</p>
          <p>Sabemos que la conducción urbana en <strong>{comuna}</strong> exige frenadas constantes que aceleran el desgaste de pastillas y discos. Por eso recomendamos una inspección cada 10.000 km y el cambio de pastillas cuando el espesor residual alcanza los 3 mm. Nuestro servicio de <strong>frenos a domicilio en {comuna}</strong> incluye medición con calibrador digital, rectificación de discos cuando es viable, y purga del circuito hidráulico con fluido DOT 4 de alta especificación.</p>
          <p>No arriesgues tu seguridad ni la de tu familia. Si notas chirridos, vibraciones al frenar o el pedal se siente esponjoso, contáctanos de inmediato. {BRAND} es tu <strong>taller de frenos en {comuna}</strong> con atención a domicilio y garantía en cada intervención.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    blocks.append(content)

    # ──────────────────────────────────────────────────────────────
    # H2-7: Vulcanización a Domicilio en [Comuna]
    # ──────────────────────────────────────────────────────────────
    h2_es = f"Vulcanización a Domicilio en {comuna}"
    h2_en = f"Mobile Tire Repair Service in {comuna}"
    content = f"""<section class="seo-section" style="background-color:#fff; padding:50px 0;">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2 class="seo-h2" style="color:#E87722; font-size:1.7rem; font-weight:700; margin-bottom:8px;">{h2_es}</h2>
        <p style="font-style:italic; color:#888; font-size:1rem; margin-bottom:20px;">({h2_en})</p>
        <div class="seo-text">
          <p>Un pinchazo siempre llega en el momento más inoportuno, pero con el servicio de <strong>vulcanización a domicilio en {comuna}</strong> de {BRAND}, puedes solucionar el inconveniente sin moverte. Nuestro equipo de vulcanización se traslada hasta tu ubicación en <strong>{comuna}</strong> con todo el equipamiento necesario: compresor portátil, parches en caliente y en frío, balanza de balanceo y herramientas para desmontaje y montaje de neumáticos.</p>
          <p>Además de la reparación de pinchaduras, nuestro servicio de <strong>vulcanización en {comuna}</strong> incluye rotación de neumáticos, revisión de presión y desgaste, alineación de dirección cuando se requiere y asesoría para el reemplazo de cubiertas cuando la vida útil ha llegado a su fin. Trabajamos con todas las medidas y tipos: radiales, de alto rendimiento, todo terreno y run-flat.</p>
          <p>Si necesitas <strong>vulcanización a domicilio en {comuna}</strong>, envíanos un mensaje por WhatsApp con tu ubicación y el tipo de avería. En el menor tiempo posible, un técnico estará contigo para que puedas volver a circular con seguridad.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    blocks.append(content)

    # ──────────────────────────────────────────────────────────────
    # H2-8: Servicios Especializados: Turbos, Bujías, Suspensión, Amortiguadores y Alternadores
    # ──────────────────────────────────────────────────────────────
    h2_es = f"Servicios Especializados en {comuna}: Turbos, Bujías, Suspensión y Alternadores"
    h2_en = f"Specialized Auto Services in {comuna}: Turbos, Spark Plugs, Suspension & Alternators"
    content = f"""<section class="seo-section" style="background-color:#f8f9fa; padding:50px 0; border-top:3px solid #E87722; border-bottom:5px solid #E87722;">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2 class="seo-h2" style="color:#E87722; font-size:1.7rem; font-weight:700; margin-bottom:8px;">{h2_es}</h2>
        <p style="font-style:italic; color:#888; font-size:1rem; margin-bottom:20px;">({h2_en})</p>
        <div class="seo-text">
          <p>En {BRAND} no solo atendemos mecánica general; también contamos con <strong>servicios especializados en {comuna}</strong> para intervenir componentes que requieren conocimientos avanzados. La <strong>reparación de turbocompresores</strong> es uno de ellos: diagnosticamos pérdida de presión, fugas de aceite en el turbo y ruidos anómalos, realizando la reconstrucción o reemplazo con garantía de funcionamiento. Igualmente, el <strong>cambio de bujías</strong> es clave para el rendimiento del motor: unas bujías en mal estado generan fallas de encendido, mayor consumo y emisiones contaminantes.</p>
          <p>La <strong>suspensión y los amortiguadores</strong> son otra de nuestras especialidades. Una suspensión desgastada compromete la estabilidad, alarga las distancias de frenado y acelera el deterioro de neumáticos. Nuestros técnicos reemplazan amortiguadores, rótulas, brazos de suspensión, bujes y terminales de dirección, devolviendo a tu vehículo el confort y la seguridad original. Además, reparamos y cambiamos <strong>alternadores</strong> defectuosos que impiden la correcta carga de la batería, evitando que tu auto se quede sin energía en plena vía.</p>
          <p>Somos un <strong>taller multimarca en {comuna}</strong> que atiende Toyota, Hyundai, Kia, Chevrolet, Nissan, Renault, Peugeot, Ford, Volkswagen, Honda, Mazda, Suzuki, Subaru, Fiat, MG y muchas más. Solicita tu presupuesto por WhatsApp y recibe atención especializada a domicilio.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    blocks.append(content)

    return "\n\n".join(blocks)


def build_vehicle_h2_blocks(vehicle):
    """
    Build 3 H2 blocks for a vehicle page.
    Content is UNIQUE - uses synonyms and different phrasing from other repositories.
    Format: H2 in Spanish, then same H2 in English in italics/parentheses below.
    """

    blocks = []

    # ──────────────────────────────────────────────────────────────
    # H2-1: Mecánico Cerca de Mí para [Vehículo] en Santiago
    # ──────────────────────────────────────────────────────────────
    h2_es = f"Mecánico Cerca de Mí para {vehicle} en Santiago"
    h2_en = f"Mechanic Near Me for {vehicle} in Santiago"
    content = f"""<section class="seo-section" style="background-color:#fff; padding:50px 0;">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2 class="seo-h2" style="color:#E87722; font-size:1.7rem; font-weight:700; margin-bottom:8px;">{h2_es}</h2>
        <p style="font-style:italic; color:#888; font-size:1rem; margin-bottom:20px;">({h2_en})</p>
        <div class="seo-text">
          <p>Si buscas un <strong>mecánico cerca de mí para {vehicle} en Santiago</strong>, {BRAND} es la opción que necesitas. Nuestro equipo de técnicos certificados se traslada a tu domicilio, oficina o cualquier punto de la Región Metropolitana para atender tu <strong>{vehicle}</strong> con herramientas de diagnóstico profesional y repuestos de calidad. No importa si se trata de una revisión rutinaria o de una avería imprevista: estamos disponibles de lunes a domingo, incluyendo festivos, para brindarte la asistencia que mereces.</p>
          <p>El modelo <strong>{vehicle}</strong> tiene particularidades mecánicas que exigen conocimiento específico. En {BRAND} conocemos las fallas más frecuentes de este vehículo y contamos con la experiencia necesaria para resolverlas en el menor tiempo posible. Nuestro servicio de <strong>mecánico a domicilio para {vehicle}</strong> incluye diagnóstico con escáner, cambio de aceite y filtros, revisión de frenos, ajuste de suspensión y reparación de sistemas eléctricos, todo sin que traslades tu automóvil a un taller convencional.</p>
          <p>Agendar tu atención es muy simple: envíame un WhatsApp con tu modelo, año y el síntoma que presenta tu <strong>{vehicle}</strong>. En minutos recibirás un presupuesto transparente y una ventana horaria para que un profesional acuda a tu ubicación en Santiago.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    blocks.append(content)

    # ──────────────────────────────────────────────────────────────
    # H2-2: Electricidad Automotriz y Diagnóstico con Scanner para [Vehículo]
    # ──────────────────────────────────────────────────────────────
    h2_es = f"Electricidad Automotriz y Diagnóstico con Scanner para {vehicle}"
    h2_en = f"Auto Electrical & Diagnostic Scan for {vehicle}"
    content = f"""<section class="seo-section" style="background-color:#f8f9fa; padding:50px 0; border-top:3px solid #E87722;">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2 class="seo-h2" style="color:#E87722; font-size:1.7rem; font-weight:700; margin-bottom:8px;">{h2_es}</h2>
        <p style="font-style:italic; color:#888; font-size:1rem; margin-bottom:20px;">({h2_en})</p>
        <div class="seo-text">
          <p>Los vehículos modernos como el <strong>{vehicle}</strong> dependen en gran medida de sistemas electrónicos complejos. Desde la unidad de control del motor hasta los sensores de estacionamiento, cualquier componente eléctrico puede fallar y generar síntomas difíciles de identificar sin el equipamiento adecuado. En {BRAND} ofrecemos <strong>electricidad automotriz y diagnóstico con scanner para {vehicle}</strong>, utilizando tecnología de escaneo de última generación que accede a todos los módulos del automóvil en segundos.</p>
          <p>Nuestro servicio cubre desde la detección de códigos de falla hasta la reparación de cableado, reemplazo de sensores, recuperación de módulos y programación de llaves. Si tu <strong>{vehicle}</strong> presenta luces testigo encendidas en el tablero, arranque intermitente, pérdida de potencia o consumos anormales de combustible, un escaneo profesional es la herramienta indicada para determinar la causa real del problema y evitar gastos innecesarios en repuestos.</p>
          <p>Con {BRAND}, el <strong>diagnóstico con scanner para {vehicle}</strong> se realiza en tu propia puerta en Santiago. Te entregamos un reporte claro con los códigos detectados, su significado y el costo de reparación antes de iniciar cualquier trabajo. Transparencia y profesionalismo son nuestra carta de presentación.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    blocks.append(content)

    # ──────────────────────────────────────────────────────────────
    # H2-3: Taller de Frenos y Suspensión para [Vehículo]
    # ──────────────────────────────────────────────────────────────
    h2_es = f"Taller de Frenos y Suspensión para {vehicle}"
    h2_en = f"Brake & Suspension Shop for {vehicle}"
    content = f"""<section class="seo-section" style="background-color:#fff; padding:50px 0; border-bottom:5px solid #E87722;">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2 class="seo-h2" style="color:#E87722; font-size:1.7rem; font-weight:700; margin-bottom:8px;">{h2_es}</h2>
        <p style="font-style:italic; color:#888; font-size:1rem; margin-bottom:20px;">({h2_en})</p>
        <div class="seo-text">
          <p>La seguridad vial de tu <strong>{vehicle}</strong> depende directamente del buen estado de su sistema de frenado y de su suspensión. En {BRAND} somos un <strong>taller de frenos y suspensión para {vehicle}</strong> que opera a domicilio en toda la Región Metropolitana. Revisamos y reemplazamos pastillas, discos, tambores, líquido hidráulico, amortiguadores, rótulas, brazos de control, bujes y terminales de dirección, utilizando repuestos que cumplen con las especificaciones del fabricante.</p>
          <p>Un sistema de frenos en condiciones deficientes alarga las distancias de detención y puede provocar accidentes. Del mismo modo, una <strong>suspensión desgastada en tu {vehicle}</strong> genera vibraciones, desgaste irregular de neumáticos y pérdida de adherencia en curvas. Nuestros técnicos realizan una inspección visual y funcional completa, midiendo el espesor de pastillas con calibrador digital, verificando la planitud de los discos y evaluando el estado de los amortiguadores con la prueba de rebote.</p>
          <p>No esperes a que una falla se agrave. Si percibes chirridos al frenar, el vehículo se desvía hacia un lado, o sientes golpeteos al pasar por baches, contáctanos por WhatsApp. {BRAND} es tu <strong>taller de frenos y suspensión para {vehicle}</strong> con servicio a domicilio, precios justos y garantía en cada trabajo.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    blocks.append(content)

    return "\n\n".join(blocks)


def process_comunas():
    """Process all comuna HTML files."""
    files = sorted(glob.glob(os.path.join(COMUNAS_DIR, "*.html")))
    total_lines = 0
    modified = 0

    for fpath in files:
        slug = os.path.splitext(os.path.basename(fpath))[0]
        if slug not in COMUNA_NAMES:
            print(f"  [SKIP] Unknown comuna slug: {slug}")
            continue

        comuna = COMUNA_NAMES[slug]

        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()

        # Check if already has the SEO Round 2 content
        if "Mecánico Cerca de Mí en " + comuna in html and "Asistencia a Domicilio" in html:
            print(f"  [SKIP] {comuna} - already has Round 2 content")
            continue

        # Find insertion point: before the FAQ section
        # Try the standard marker first
        faq_marker = '<section class="py-5 bg-light" id="faq">'
        if faq_marker not in html:
            # Try alternative markers
            alt_markers = [
                'id="faq"',
                '<!-- PREGUNTAS FRECUENTES',
                '<!-- FAQ',
            ]
            found = False
            for alt in alt_markers:
                if alt in html:
                    faq_marker = alt
                    found = True
                    break
            if not found:
                print(f"  [WARN] No FAQ marker found in {comuna}, skipping")
                continue

        # Build H2 blocks
        h2_content = build_comuna_h2_blocks(comuna)
        lines_added = h2_content.count("\n") + 1

        # Insert before FAQ marker
        idx = html.find(faq_marker)
        # Also insert the separator comment
        insert_text = f"""
<!-- ======================================================================= -->
<!-- SEO ROUND 2 - H2 KEYWORD CONTENT (LLANOCAR) -->
<!-- ======================================================================= -->
{h2_content}

"""
        new_html = html[:idx] + insert_text + html[idx:]

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_html)

        total_lines += lines_added
        modified += 1
        print(f"  [OK] {comuna} - {lines_added} lines added")

    return modified, total_lines


def process_vehiculos():
    """Process all vehicle HTML files."""
    files = sorted(glob.glob(os.path.join(VEHICULOS_DIR, "*.html")))
    total_lines = 0
    modified = 0

    for fpath in files:
        slug = os.path.splitext(os.path.basename(fpath))[0]
        if slug == "index":
            continue
        if slug not in VEHICLE_NAMES:
            print(f"  [SKIP] Unknown vehicle slug: {slug}")
            continue

        vehicle = VEHICLE_NAMES[slug]

        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()

        # Check if already has the SEO Round 2 content
        if f"Mecánico Cerca de Mí para {vehicle}" in html and "Santiago" in html:
            print(f"  [SKIP] {vehicle} - already has Round 2 content")
            continue

        # Find insertion point: before "Otros Vehiculos" section
        insert_marker = "Otros Vehiculos"
        if insert_marker not in html:
            # Try alternative markers
            alt_markers = [
                "Otros Veh",
                "Otros veh",
            ]
            found = False
            for alt in alt_markers:
                if alt in html:
                    insert_marker = alt
                    found = True
                    break
            if not found:
                print(f"  [WARN] No insertion marker found in {vehicle}, skipping")
                continue

        # Build H2 blocks
        h2_content = build_vehicle_h2_blocks(vehicle)
        lines_added = h2_content.count("\n") + 1

        # Find the section start that contains "Otros Vehiculos"
        idx = html.find(insert_marker)
        # Go back to find the <section> tag
        section_start = html.rfind("<section", 0, idx)
        if section_start == -1:
            print(f"  [WARN] No section tag before marker in {vehicle}, using direct position")
            section_start = idx
        else:
            # Go back a bit more to include the newline before the section
            newline_before = html.rfind("\n", 0, section_start)
            if newline_before != -1 and section_start - newline_before < 5:
                section_start = newline_before

        # Insert the H2 content before the "Otros Vehiculos" section
        insert_text = f"""
<!-- ======================================================================= -->
<!-- SEO ROUND 2 - H2 KEYWORD CONTENT (LLANOCAR) -->
<!-- ======================================================================= -->
{h2_content}

"""
        new_html = html[:section_start] + insert_text + html[section_start:]

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_html)

        total_lines += lines_added
        modified += 1
        print(f"  [OK] {vehicle} - {lines_added} lines added")

    return modified, total_lines


def validate_html():
    """Basic validation: check that section tags are balanced in each file."""
    errors = 0
    for fpath in glob.glob(os.path.join(COMUNAS_DIR, "*.html")) + glob.glob(os.path.join(VEHICULOS_DIR, "*.html")):
        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()
        opens = len(re.findall(r"<section", html))
        closes = len(re.findall(r"</section>", html))
        if opens != closes:
            print(f"  [ERROR] {os.path.basename(fpath)}: {opens} <section> vs {closes} </section>")
            errors += 1
    return errors


if __name__ == "__main__":
    print("=" * 60)
    print("LLANOCAR SEO Round 2 - Adding H2 keyword content")
    print("=" * 60)

    print("\n--- Processing COMUNAS (47 pages) ---")
    c_mod, c_lines = process_comunas()
    print(f"  Result: {c_mod} comunas modified, ~{c_lines} lines added")

    print("\n--- Processing VEHICULOS (32 pages) ---")
    v_mod, v_lines = process_vehiculos()
    print(f"  Result: {v_mod} vehicles modified, ~{v_lines} lines added")

    print("\n--- Validating HTML integrity ---")
    errors = validate_html()
    if errors == 0:
        print("  All files pass validation!")
    else:
        print(f"  {errors} files have issues - review needed")

    total = c_mod + v_mod
    total_lines = c_lines + v_lines
    print(f"\n{'=' * 60}")
    print(f"TOTAL: {total} files modified, ~{total_lines} lines added")
    print(f"{'=' * 60}")
