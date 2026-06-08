#!/usr/bin/env python3
"""
LLANOCAR SEO Round 2 — REESCRITURA TOTAL
Contenido 100% diferenciado del repositorio Globalpro.
H2s con frases distintas, párrafos con estructura y ángulo diferente.
Incluye H2 en español + traducción inglesa en cursiva entre paréntesis.
"""

import os, re, glob

BASE = "/home/z/my-project/llanocar"
COMUNAS_DIR = os.path.join(BASE, "comunas")
VEHICULOS_DIR = os.path.join(BASE, "vehiculos")

BRAND = "LLANOCAR"
PHONE = "+56 9 3326 1085"
WHATSAPP_LINK = "https://wa.me/56933261085"

COMUNA_NAMES = {
    "alhue": "Alhué", "buin": "Buín", "calera-de-tango": "Calera de Tango",
    "cerrillos": "Cerrillos", "cerro-navia": "Cerro Navia", "colina": "Colina",
    "conchali": "Conchalí", "curacavi": "Curacaví", "el-bosque": "El Bosque",
    "el-monte": "El Monte", "estacion-central": "Estación Central",
    "independencia": "Independencia", "isla-de-maipo": "Isla de Maipo",
    "la-cisterna": "La Cisterna", "la-florida": "La Florida",
    "la-granja": "La Granja", "la-pintana": "La Pintana", "lampa": "Lampa",
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
    "talagante": "Talagante", "tiltil": "Tiltil",
}

VEHICLE_NAMES = {
    "chevrolet-sail": "Chevrolet Sail", "chevrolet-sonic": "Chevrolet Sonic",
    "chevrolet-spark": "Chevrolet Spark", "fiat-bravo-tjet": "Fiat Bravo T-Jet",
    "ford-ecosport": "Ford EcoSport", "ford-fiesta": "Ford Fiesta",
    "honda-city": "Honda City", "honda-civic": "Honda Civic",
    "honda-cr-v": "Honda CR-V", "hyundai-accent": "Hyundai Accent",
    "hyundai-grand-i10": "Hyundai Grand i10", "hyundai-tucson": "Hyundai Tucson",
    "kia-morning": "Kia Morning", "kia-rio": "Kia Rio", "mazda-3": "Mazda 3",
    "mazda-cx-5": "Mazda CX-5", "mg-3": "MG 3", "mg-zs": "MG ZS",
    "nissan-kicks": "Nissan Kicks", "nissan-versa": "Nissan Versa",
    "peugeot-208": "Peugeot 208", "peugeot-3008": "Peugeot 3008",
    "renault-duster": "Renault Duster", "renault-logan": "Renault Logan",
    "subaru-forester": "Subaru Forester", "subaru-xv": "Subaru XV",
    "suzuki-baleno": "Suzuki Baleno", "suzuki-celerio": "Suzuki Celerio",
    "suzuki-swift": "Suzuki Swift", "toyota-corolla": "Toyota Corolla",
    "toyota-yaris": "Toyota Yaris", "volkswagen-gol": "Volkswagen Gol",
}


def build_comuna_h2_blocks(comuna):
    """
    8 H2 blocks for comuna pages.
    COMPLETELY different headings and content structure from the other repo.
    """

    blocks = []

    # ── H2-1: Reparación de Automóviles a Domicilio en [Comuna] ──
    # (instead of "Taller Mecánico Cerca de Mí")
    h2_es = f"Reparación de Automóviles a Domicilio en {comuna}"
    h2_en = f"Car Repair at Your Doorstep in {comuna}"
    content = f"""<section class="seo-section" style="background-color:#fff; padding:50px 0;">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2 class="seo-h2" style="color:#E87722; font-size:1.7rem; font-weight:700; margin-bottom:8px;">{h2_es}</h2>
        <p style="font-style:italic; color:#888; font-size:1rem; margin-bottom:20px;">({h2_en})</p>
        <div class="seo-text">
          <p>Cuando tu vehículo presenta una falla en <strong>{comuna}</strong>, lo habitual es pensar en remolcarlo hasta un taller. Sin embargo, {BRAND} te ofrece una alternativa mucho más práctica: la <strong>reparación de automóviles a domicilio en {comuna}</strong>. Nuestro equipo se traslada con unidad móvil completamente equipada —escáner profesional, herramientas especializadas y repuestos de alta gama— para resolver la avería en el mismo sitio donde se encuentra tu auto, ya sea en tu casa, oficina o estacionamiento.</p>
          <p>Con más de 15 años de experiencia atendiendo vehículos en la Región Metropolitana, hemos perfeccionado un modelo de servicio que elimina los tiempos de espera y los costos de traslado. Cada intervención en <strong>{comuna}</strong> es ejecutada por técnicos certificados que entregan un diagnóstico preciso, un presupuesto sin sorpresas y una garantía escrita por cada trabajo realizado. Todo el proceso se coordina por WhatsApp al {PHONE}, donde confirmas horario, recibes el informe del diagnóstico y apruebas la reparación antes de que comencemos.</p>
          <p>Ya no necesitas buscar dónde dejar tu auto por días. Con {BRAND}, la <strong>reparación de automóviles a domicilio</strong> llega a <strong>{comuna}</strong> con la misma calidad de un taller establecido, pero con la comodidad de no moverte de tu lugar.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    blocks.append(content)

    # ── H2-2: Asistencia Técnica Vehicular en [Comuna] — Disponibilidad Inmediata ──
    # (instead of "Mecánico Cerca de Mí")
    h2_es = f"Asistencia Técnica Vehicular en {comuna} — Disponibilidad Inmediata"
    h2_en = f"Vehicle Breakdown Assistance in {comuna} — Immediate Availability"
    content = f"""<section class="seo-section" style="background-color:#f8f9fa; padding:50px 0; border-top:3px solid #E87722;">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2 class="seo-h2" style="color:#E87722; font-size:1.7rem; font-weight:700; margin-bottom:8px;">{h2_es}</h2>
        <p style="font-style:italic; color:#888; font-size:1rem; margin-bottom:20px;">({h2_en})</p>
        <div class="seo-text">
          <p>Una avería imprevista puede ocurrir a cualquier hora, y en {BRAND} lo sabemos. Por eso ofrecemos <strong>asistencia técnica vehicular en {comuna}</strong> con disponibilidad inmediata, los 7 días de la semana, incluyendo domingos y festivos. Nuestro compromiso es que un profesional se presente en tu ubicación dentro de <strong>{comuna}</strong> en el menor tiempo posible, llevando el equipamiento necesario para resolver desde una batería descargada hasta una falla del sistema de inyección electrónica.</p>
          <p>A diferencia de los servicios convencionales que requieren que lleves tu auto al taller, nuestra <strong>asistencia técnica a domicilio en {comuna}</strong> funciona al revés: el taller va hasta ti. Esto significa cero tiempos de traslado, cero grúas y cero molestias. Además, nuestro equipo cuenta con experiencia directa en las fallas más comunes de las marcas que circulan en Chile —Toyota, Hyundai, Kia, Chevrolet, Nissan, Renault, Ford, Volkswagen, Mazda, Suzuki, entre otras—, lo que agiliza enormemente el diagnóstico y la reparación.</p>
          <p>Si tu auto no arranca, pierde potencia o enciende una luz de alerta en el tablero mientras conduces por <strong>{comuna}</strong>, no lo pienses dos veces: escríbenos por WhatsApp y coordinaremos la asistencia de inmediato.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    blocks.append(content)

    # ── H2-3: Solución de Fallas Eléctricas del Vehículo en [Comuna] ──
    # (instead of "Electricidad Automotriz a Domicilio")
    h2_es = f"Solución de Fallas Eléctricas del Vehículo en {comuna}"
    h2_en = f"Vehicle Electrical Fault Repair in {comuna}"
    content = f"""<section class="seo-section" style="background-color:#fff; padding:50px 0;">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2 class="seo-h2" style="color:#E87722; font-size:1.7rem; font-weight:700; margin-bottom:8px;">{h2_es}</h2>
        <p style="font-style:italic; color:#888; font-size:1rem; margin-bottom:20px;">({h2_en})</p>
        <div class="seo-text">
          <p>Los sistemas eléctricos de los vehículos actuales son cada vez más complejos: redes CAN bus, módulos de control interconectados, sensores de todo tipo y cableado extenso que, al fallar, generan síntomas difíciles de interpretar sin la herramienta adecuada. En {BRAND} resolvemos <strong>fallas eléctricas del vehículo en {comuna}</strong> con un enfoque metódico: primero escaneamos todos los módulos con equipo de diagnóstico de última generación, luego identificamos la causa raíz y finalmente aplicamos la reparación precisa, ya sea en el cableado, un sensor, un actuador o una unidad de control.</p>
          <p>Las situaciones más frecuentes que atendemos en <strong>{comuna}</strong> incluyen: batería que no retiene carga, alternador con regulador defectuoso, motor de arranque que gira lento, luces del tablero encendidas sin motivo aparente, y sistemas de confort (vidrios, cerraduras, espejos) que dejan de funcionar. Cada una de estas fallas tiene un protocolo de diagnóstico específico que nuestros eléctricos automotrices dominan a la perfección.</p>
          <p>Si tu vehículo en <strong>{comuna}</strong> presenta cualquier síntoma eléctrico, contáctanos al {PHONE}. Un técnico especializado se desplazará a tu dirección con el escáner y las herramientas necesarias para devolver la normalidad a tu auto en una sola visita.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    blocks.append(content)

    # ── H2-4: Plan de Mantención para tu Auto en [Comuna] ──
    # (instead of "Mantención Preventiva a Domicilio")
    h2_es = f"Plan de Mantención para tu Auto en {comuna}"
    h2_en = f"Car Maintenance Plan in {comuna}"
    content = f"""<section class="seo-section" style="background-color:#f8f9fa; padding:50px 0; border-top:3px solid #E87722;">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2 class="seo-h2" style="color:#E87722; font-size:1.7rem; font-weight:700; margin-bottom:8px;">{h2_es}</h2>
        <p style="font-style:italic; color:#888; font-size:1rem; margin-bottom:20px;">({h2_en})</p>
        <div class="seo-text">
          <p>Un vehículo bien mantenido rinde mejor, consume menos combustible y, sobre todo, no te deja varado. En {BRAND} diseñamos un <strong>plan de mantención para tu auto en {comuna}</strong> adaptado al kilometraje, modelo y año de fabricación. Cada plan incluye: cambio de aceite y filtro (con lubricantes sintéticos y semi-sintéticos de marcas premium como Castrol y Mobil), reemplazo de filtros de aire y habitáculo, revisión del sistema de enfriamiento, inspección de correas y mangueras, y control de los niveles de líquido de frenos, dirección y refrigerante.</p>
          <p>Lo que diferencia nuestro servicio en <strong>{comuna}</strong> es que todo se ejecuta en el lugar que tú elijas, sin traslados ni filas de espera. Nuestros operarios llevan todo el insumo necesario en la unidad móvil, de modo que la mantención se completa en una sola visita. Además, al finalizar, te entregamos un informe detallado con el estado de cada componente revisado y las recomendaciones para la próxima intervención según tu kilometraje.</p>
          <p>Cuidar tu auto con un <strong>plan de mantención en {comuna}</strong> es la inversión más rentable que puedes hacer por tu vehículo. Agenda tu próxima revisión por WhatsApp y recibe atención personalizada sin salir de casa.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    blocks.append(content)

    # ── H2-5: Escaneo Computarizado de tu Vehículo en [Comuna] ──
    # (instead of "Diagnóstico Automotriz con Scanner")
    h2_es = f"Escaneo Computarizado de tu Vehículo en {comuna}"
    h2_en = f"Computerized Vehicle Scan in {comuna}"
    content = f"""<section class="seo-section" style="background-color:#fff; padding:50px 0;">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2 class="seo-h2" style="color:#E87722; font-size:1.7rem; font-weight:700; margin-bottom:8px;">{h2_es}</h2>
        <p style="font-style:italic; color:#888; font-size:1rem; margin-bottom:20px;">({h2_en})</p>
        <div class="seo-text">
          <p>La luz check engine encendida es la señal más clara de que algo no está bien en tu motor, pero también puede ser engañosa: a veces indica un problema menor y otras una falla grave. El <strong>escaneo computarizado de tu vehículo en {comuna}</strong> que realiza {BRAND} elimina las dudas. Conectamos nuestro equipo de diagnóstico directamente al conector OBD-II de tu auto y en minutos obtenemos la lectura completa de todos los códigos de falla almacenados, junto con los datos en tiempo real de los sensores clave (temperatura, RPM, flujo de aire, sonda lambda, posición del acelerador, entre otros).</p>
          <p>Este servicio de <strong>escaneo automotriz en {comuna}</strong> no se limita a leer códigos: nuestros técnicos analizan la información, la correlacionan con los síntomas que tú describes y te entregan un diagnóstico claro con la causa más probable del problema, el costo estimado de la reparación y la urgencia de la intervención. Si decides reparar con nosotros, el costo del escaneo se descuenta del presupuesto final.</p>
          <p>No sigas conduciendo con la luz de alerta encendida. Un <strong>escaneo computarizado en {comuna}</strong> puede prevenir daños mayores. Llámanos o escríbenos por WhatsApp para agendar tu cita a domicilio.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    blocks.append(content)

    # ── H2-6: Revisión y Reparación de Frenos en [Comuna] ──
    # (instead of "Taller de Frenos Cerca de Mí")
    h2_es = f"Revisión y Reparación de Frenos en {comuna}"
    h2_en = f"Brake Inspection & Repair in {comuna}"
    content = f"""<section class="seo-section" style="background-color:#f8f9fa; padding:50px 0; border-top:3px solid #E87722;">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2 class="seo-h2" style="color:#E87722; font-size:1.7rem; font-weight:700; margin-bottom:8px;">{h2_es}</h2>
        <p style="font-style:italic; color:#888; font-size:1rem; margin-bottom:20px;">({h2_en})</p>
        <div class="seo-text">
          <p>Un sistema de frenos en buen estado es la diferencia entre detenerse a tiempo y sufrir un accidente. En {BRAND} realizamos <strong>revisión y reparación de frenos en {comuna}</strong> con un procedimiento exhaustivo que incluye: medición del espesor de pastillas con calibrador digital, inspección de discos (verificando espesor mínimo y planitud), evaluación del líquido hidráulico (punto de ebullición y contaminación), revisión de latiguillos y mangueras, y prueba del servofreno. Todo esto se lleva a cabo en tu propia puerta en <strong>{comuna}</strong>, sin necesidad de llevar tu vehículo a un taller.</p>
          <p>Si la inspección revela desgaste, procedemos al reemplazo con repuestos que respetan las especificaciones del fabricante de tu vehículo. Trabajamos con pastillas cerámicas, semi-metalizadas y orgánicas según el tipo de conducción y el modelo del auto. Para los discos, evaluamos si es posible la rectificación o si requiere reemplazo. El servicio de <strong>reparación de frenos en {comuna}</strong> incluye además la purga del circuito hidráulico con fluido DOT 4 de alta especificación.</p>
          <p>Si escuchas chirridos al frenar, sientes vibraciones en el pedal o la distancia de frenado ha aumentado, no esperes más. Contáctanos por WhatsApp y un especialista en frenos se presentará en <strong>{comuna}</strong> con todo el equipamiento necesario.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    blocks.append(content)

    # ── H2-7: Servicio de Neumáticos a Domicilio en [Comuna] ──
    # (instead of "Vulcanización a Domicilio")
    h2_es = f"Servicio de Neumáticos a Domicilio en {comuna}"
    h2_en = f"Mobile Tire Service in {comuna}"
    content = f"""<section class="seo-section" style="background-color:#fff; padding:50px 0;">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2 class="seo-h2" style="color:#E87722; font-size:1.7rem; font-weight:700; margin-bottom:8px;">{h2_es}</h2>
        <p style="font-style:italic; color:#888; font-size:1rem; margin-bottom:20px;">({h2_en})</p>
        <div class="seo-text">
          <p>Un neumático pinchado o desinflado puede dejarte varado en cualquier momento, y no siempre es posible llevar el auto a un taller de neumáticos. Por eso {BRAND} ofrece un <strong>servicio de neumáticos a domicilio en {comuna}</strong> que resuelve el inconveniente en el acto. Nuestra unidad móvil porta compresor, kit de parchado en caliente y en frío, herramientas de desmonte, balanza de balanceo y un stock de válvulas y tapas, lo que nos permite reparar pinchaduras, rotar cubiertas, ajustar presiones y balancear ruedas sin que muevas tu vehículo de su ubicación en <strong>{comuna}</strong>.</p>
          <p>Además de la reparación de pinchaduras, nuestro <strong>servicio de neumáticos en {comuna}</strong> contempla la evaluación del estado general de las cuatro cubiertas: medición de profundidad del dibujo, detección de deformaciones, cortes o abultamientos en la pared lateral, y revisión de la presión correcta según las especificaciones del fabricante. Si alguna cubierta necesita reemplazo, te asesoramos sobre la mejor opción según tu presupuesto y tipo de vehículo.</p>
          <p>Escríbenos por WhatsApp con tu ubicación en <strong>{comuna}</strong> y el problema que presentas. En breve un técnico se presentará con la solución para que retomes tu camino con total seguridad.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    blocks.append(content)

    # ── H2-8: Tratamiento de Componentes de Alto Desgaste en [Comuna] ──
    # (instead of "Servicios Especializados: Turbos, Bujías...")
    h2_es = f"Tratamiento de Componentes de Alto Desgaste en {comuna}"
    h2_en = f"High-Wear Component Service in {comuna}"
    content = f"""<section class="seo-section" style="background-color:#f8f9fa; padding:50px 0; border-top:3px solid #E87722; border-bottom:5px solid #E87722;">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2 class="seo-h2" style="color:#E87722; font-size:1.7rem; font-weight:700; margin-bottom:8px;">{h2_es}</h2>
        <p style="font-style:italic; color:#888; font-size:1rem; margin-bottom:20px;">({h2_en})</p>
        <div class="seo-text">
          <p>Existen componentes del vehículo que, por su naturaleza, sufren un desgaste acelerado y requieren atención especializada cuando empiezan a fallar. En {BRAND} nos hemos especializado en el <strong>tratamiento de componentes de alto desgaste en {comuna}</strong>, lo que incluye: turbocompresores (pérdida de sobrepresión, fuga de aceite por el eje, holgura excesiva en los rodamientos), bujías de encendido e inyectores (que afectan directamente la combustión y el rendimiento), suspensión y amortiguación (rótulas, brazos, bujes, amortiguadores que comprometen la estabilidad), y alternadores (que dejan sin carga a la batería y pueden detener el vehículo por completo).</p>
          <p>Cada uno de estos componentes tiene un protocolo de diagnóstico propio. Por ejemplo, para evaluar un turbo realizamos prueba de presión de soplado con manómetro; para las bujías, medimos resistencia y verificamos la apertura del electrodo; para la suspensión, ejecutamos la prueba de rebote y revisamos holguras con palanca; y para el alternador, medimos voltaje de carga con el motor a distintas revoluciones. Este nivel de detalle es lo que distingue nuestro servicio de <strong>componentes de alto desgaste en {comuna}</strong>.</p>
          <p>Somos un taller multimarca que atiende todas las marcas que circulan en Chile. Si tu vehículo en <strong>{comuna}</strong> presenta síntomas en alguno de estos componentes, solicita tu evaluación por WhatsApp y recibe un diagnóstico profesional a domicilio.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    blocks.append(content)

    return "\n\n".join(blocks)


def build_vehicle_h2_blocks(vehicle):
    """
    3 H2 blocks for vehicle pages.
    COMPLETELY different headings and content from the other repo.
    """

    blocks = []

    # ── H2-1: Atención Mecánica a Domicilio para [Vehículo] en Santiago ──
    # (instead of "Mecánico Cerca de Mí para [Vehículo]")
    h2_es = f"Atención Mecánica a Domicilio para {vehicle} en Santiago"
    h2_en = f"Mobile Mechanic Service for {vehicle} in Santiago"
    content = f"""<section class="seo-section" style="background-color:#fff; padding:50px 0;">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2 class="seo-h2" style="color:#E87722; font-size:1.7rem; font-weight:700; margin-bottom:8px;">{h2_es}</h2>
        <p style="font-style:italic; color:#888; font-size:1rem; margin-bottom:20px;">({h2_en})</p>
        <div class="seo-text">
          <p>Tu <strong>{vehicle}</strong> necesita cuidado profesional, pero trasladarlo a un taller convencional no siempre es posible o conveniente. En {BRAND} brindamos <strong>atención mecánica a domicilio para {vehicle} en Santiago</strong>, llevando el taller hasta el lugar donde esté tu auto. Nuestros técnicos conocen las particularidades de este modelo —sus fallas típicas, los intervalos de mantención recomendados, los repuestos que mejor se adaptan— y se presentan con el equipamiento necesario para resolver la mayoría de las intervenciones en una sola visita.</p>
          <p>El servicio cubre desde una mantención de rutina (aceite, filtros, líquidos) hasta reparaciones más complejas como reemplazo de embrague, corrección de fallas eléctricas, ajuste de suspensión y resolución de problemas en el sistema de inyección. Todo se coordina por WhatsApp: nos envías los datos de tu <strong>{vehicle}</strong>, el síntoma que presenta y tu dirección en la Región Metropolitana, y nosotros confirmamos un horario de atención.</p>
          <p>Con {BRAND}, el <strong>servicio mecánico a domicilio para {vehicle}</strong> es rápido, transparente y con garantía. Evita filas, evita grúas, evita tiempos perdidos. Escríbenos yagenda tu cita hoy.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    blocks.append(content)

    # ── H2-2: Detección y Resolución de Fallas Electrónicas en [Vehículo] ──
    # (instead of "Electricidad Automotriz y Diagnóstico con Scanner")
    h2_es = f"Detección y Resolución de Fallas Electrónicas en {vehicle}"
    h2_en = f"Electronic Fault Detection & Repair for {vehicle}"
    content = f"""<section class="seo-section" style="background-color:#f8f9fa; padding:50px 0; border-top:3px solid #E87722;">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2 class="seo-h2" style="color:#E87722; font-size:1.7rem; font-weight:700; margin-bottom:8px;">{h2_es}</h2>
        <p style="font-style:italic; color:#888; font-size:1rem; margin-bottom:20px;">({h2_en})</p>
        <div class="seo-text">
          <p>El <strong>{vehicle}</strong> incorpora múltiples sistemas electrónicos que controlan desde la inyección de combustible hasta los sistemas de seguridad. Cuando uno de estos módulos presenta una anomalía, los síntomas pueden ser confusos: pérdida de potencia intermitente, consumo elevado de gasolina, luces de advertencia que se encienden y apagan, o dificultad para arrancar en frío. En {BRAND} nos especializamos en la <strong>detección y resolución de fallas electrónicas en {vehicle}</strong>, utilizando tecnología de escaneo que accede a cada módulo del vehículo y nos permite identificar con precisión qué sensor, actuador o circuito está fallando.</p>
          <p>Nuestro procedimiento no se limita a borrar códigos de error. Analizamos los datos en tiempo real, comparamos con los valores de referencia del fabricante y, si es necesario, realizamos pruebas de componentes con multímetro y osciloscopio para confirmar el diagnóstico. El servicio de <strong>fallas electrónicas para {vehicle}</strong> incluye la reparación de cableado, reemplazo de sensores defectuosos, recuperación de módulos y programación de componentes nuevos, todo ejecutado a domicilio en Santiago.</p>
          <p>Si tu <strong>{vehicle}</strong> tiene luces encendidas en el tablero o un comportamiento errático, no lo ignores. Una falla electrónica pequeña puede escalar rápidamente. Contáctanos por WhatsApp y recibe un escaneo profesional en tu propia puerta.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    blocks.append(content)

    # ── H2-3: Inspección y Renovación de Frenos y Suspensión para [Vehículo] ──
    # (instead of "Taller de Frenos y Suspensión")
    h2_es = f"Inspección y Renovación de Frenos y Suspensión para {vehicle}"
    h2_en = f"Brake & Suspension Inspection & Renewal for {vehicle}"
    content = f"""<section class="seo-section" style="background-color:#fff; padding:50px 0; border-bottom:5px solid #E87722;">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2 class="seo-h2" style="color:#E87722; font-size:1.7rem; font-weight:700; margin-bottom:8px;">{h2_es}</h2>
        <p style="font-style:italic; color:#888; font-size:1rem; margin-bottom:20px;">({h2_en})</p>
        <div class="seo-text">
          <p>Los sistemas de frenado y suspensión de tu <strong>{vehicle}</strong> trabajan en conjunto para garantizar la seguridad y el confort de conducción. En {BRAND} ofrecemos un servicio integral de <strong>inspección y renovación de frenos y suspensión para {vehicle}</strong> que se realiza completamente a domicilio en Santiago. El proceso comienza con una revisión detallada: medimos el espesor de pastillas y discos con instrumento de precisión, verificamos el estado de los amortiguadores con la prueba de rebote, evaluamos las holguras de rótulas y terminales, y controlamos el nivel y la condición del líquido de frenos.</p>
          <p>Cuando algún componente está fuera de especificación, procedemos con la renovación utilizando repuestos que respetan las normativas del fabricante. Para el <strong>{vehicle}</strong>, esto puede incluir: reemplazo de pastillas cerámicas o semi-metalizadas, rectificación o cambio de discos, instalación de amortiguadores nuevos, renovación de bujes y brazos de suspensión, y purga del circuito hidráulico. Cada pieza instalada cuenta con garantía de funcionamiento.</p>
          <p>Un <strong>{vehicle}</strong> con frenos y suspensión en mal estado es un riesgo para ti y para los demás. Si sientes vibraciones al frenar, ruidos al pasar por baches o el auto se desvía al frenar, contáctanos por WhatsApp al {PHONE}. Un especialista de {BRAND} se presentará en tu ubicación con la solución.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""
    blocks.append(content)

    return "\n\n".join(blocks)


def remove_old_round2(html):
    """Remove the old Round 2 content that was inserted previously."""
    # Find and remove everything between the old SEO ROUND 2 markers
    pattern = r'\n*<!-- =+\n<!-- SEO ROUND 2 - H2 KEYWORD CONTENT \(LLANOCAR\)\n<!-- =+\n.*?(?=\n*<!-- PREGUNTAS FRECUENTES|<section class="py-5 bg-light" id="faq")'
    # More robust: find the marker and remove until the FAQ section or the "Otros Vehiculos" section
    
    marker_start = "<!-- SEO ROUND 2 - H2 KEYWORD CONTENT (LLANOCAR) -->"
    
    if marker_start not in html:
        return html, False
    
    # Find the start (including the separator line before it)
    idx_start = html.find("<!-- ======================================================================= -->\n<!-- SEO ROUND 2")
    if idx_start == -1:
        idx_start = html.find(marker_start)
    if idx_start == -1:
        return html, False
    
    # Go back to include the blank line before the separator
    while idx_start > 0 and html[idx_start-1] == '\n':
        idx_start -= 1
    
    # Find the end - it's just before the FAQ section or "Otros Vehiculos" section
    # Look for the next major section after the Round 2 content
    faq_markers = [
        '<!-- ======================================================================= -->\n<!-- PREGUNTAS FRECUENTES',
        '<section class="py-5 bg-light" id="faq">',
        '<!-- ======================================================================= -->\n<!-- SEO ROUND 2',  # another round 2 block shouldn't exist
    ]
    
    # For vehicle pages, look for "Otros Vehiculos" section
    otros_marker = '<section class="py-5">\n  <div class="container">\n    <div class="text-center mb-5">\n      <h2 class="fw-bold" style="color: var(--gp-blood-red);">Otros Veh'
    
    idx_end = len(html)
    for m in faq_markers:
        pos = html.find(m, idx_start + 100)
        if pos != -1 and pos < idx_end:
            idx_end = pos
    
    otros_pos = html.find("Otros Vehiculos", idx_start + 100)
    if otros_pos != -1:
        # Go back to find the section start
        section_pos = html.rfind("<section", idx_start + 100, otros_pos)
        if section_pos != -1 and section_pos < idx_end:
            idx_end = section_pos
    
    if idx_end == len(html):
        return html, False
    
    # Remove the old Round 2 content
    new_html = html[:idx_start] + "\n" + html[idx_end:]
    return new_html, True


def process_comunas():
    """Process all comuna HTML files."""
    files = sorted(glob.glob(os.path.join(COMUNAS_DIR, "*.html")))
    total_lines = 0
    modified = 0

    for fpath in files:
        slug = os.path.splitext(os.path.basename(fpath))[0]
        if slug not in COMUNA_NAMES:
            continue
        comuna = COMUNA_NAMES[slug]

        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()

        # First, remove old Round 2 content
        html, was_removed = remove_old_round2(html)
        if was_removed:
            print(f"  [CLEAN] Removed old Round 2 from {comuna}")

        # Check if already has the NEW content
        if f"Reparación de Automóviles a Domicilio en {comuna}" in html:
            print(f"  [SKIP] {comuna} - already has new Round 2 content")
            continue

        # Find insertion point: before FAQ
        faq_marker = '<section class="py-5 bg-light" id="faq">'
        if faq_marker not in html:
            for alt in ['id="faq"', '<!-- PREGUNTAS FRECUENTES']:
                if alt in html:
                    faq_marker = alt
                    break
            else:
                print(f"  [WARN] No FAQ marker in {comuna}, skipping")
                continue

        h2_content = build_comuna_h2_blocks(comuna)
        lines_added = h2_content.count("\n") + 1

        idx = html.find(faq_marker)
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
        if slug == "index" or slug not in VEHICLE_NAMES:
            continue
        vehicle = VEHICLE_NAMES[slug]

        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()

        # First, remove old Round 2 content
        html, was_removed = remove_old_round2(html)
        if was_removed:
            print(f"  [CLEAN] Removed old Round 2 from {vehicle}")

        # Check if already has the NEW content
        if f"Atención Mecánica a Domicilio para {vehicle}" in html:
            print(f"  [SKIP] {vehicle} - already has new Round 2 content")
            continue

        # Find insertion point
        insert_marker = "Otros Vehiculos"
        if insert_marker not in html:
            for alt in ["Otros Veh", "Otros veh"]:
                if alt in html:
                    insert_marker = alt
                    break
            else:
                print(f"  [WARN] No marker in {vehicle}, skipping")
                continue

        h2_content = build_vehicle_h2_blocks(vehicle)
        lines_added = h2_content.count("\n") + 1

        idx = html.find(insert_marker)
        section_start = html.rfind("<section", 0, idx)
        if section_start == -1:
            section_start = idx
        else:
            newline_before = html.rfind("\n", 0, section_start)
            if newline_before != -1 and section_start - newline_before < 5:
                section_start = newline_before

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
    print("LLANOCAR SEO Round 2 — REESCRITURA ANTIDUPLICADO")
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
        print(f"  {errors} files have issues")

    print(f"\n{'=' * 60}")
    print(f"TOTAL: {c_mod + v_mod} files modified, ~{c_lines + v_lines} lines")
    print(f"{'=' * 60}")
