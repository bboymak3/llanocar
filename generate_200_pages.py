#!/usr/bin/env python3
"""
LLANOCAR SEO Landing Page Generator
Generates 200 unique HTML landing pages for llanocar.pages.dev
Types: A (80 servicio+comuna), B (60 servicio+vehiculo), C (30 servicio general), D (30 servicio+vehiculo+comuna)
"""

import os
import random
import hashlib
import time
import json

# ─── CONFIG ───────────────────────────────────────────────────────────────
BASE_DIR = "/home/z/my-project/llanocar"
DOMAIN = "https://llanocar.pages.dev"
PHONE = "+56 9 3326 1085"
WA_NUMBER = "56933261085"
EMAIL = "llanocar2019@gmail.com"
ADDRESS = "Puerto Madero 9678, Pudahuel, RM, Chile"
BUSINESS = "LLANOCAR Servicios Automotrices"

# ─── COMUNAS (47) ─────────────────────────────────────────────────────────
COMUNAS = [
    "pudahuel","estacion-central","la-cisterna","san-bernardo","la-granja",
    "la-florida","maipu","puente-alto","san-miguel","santiago",
    "las-condes","providencia","nunoa","la-reina","penalolen",
    "vitacura","lo-barnechea","huechuraba","quilicura","recoleta",
    "independencia","renca","cerro-navia","lo-prado","conchali",
    "cerrillos","el-bosque","lo-espejo","pedro-aguirre-cerda","san-joaquin",
    "la-pintana","san-ramon","macul","san-jose-de-maipo","colina",
    "lampa","buin","talagante","penaflor","melipilla",
    "calera-de-tango","el-monte","isla-de-maipo","pirque","curacavi",
    "tiltil","padre-hurtado","paine","maria-pinto","san-pedro"
]

COMUNA_DISPLAY = {
    "pudahuel":"Pudahuel","estacion-central":"Estación Central",
    "la-cisterna":"La Cisterna","san-bernardo":"San Bernardo",
    "la-granja":"La Granja","la-florida":"La Florida","maipu":"Maipú",
    "puente-alto":"Puente Alto","san-miguel":"San Miguel",
    "santiago":"Santiago Centro","las-condes":"Las Condes",
    "providencia":"Providencia","nunoa":"Ñuñoa","la-reina":"La Reina",
    "penalolen":"Peñalolén","vitacura":"Vitacura","lo-barnechea":"Lo Barnechea",
    "huechuraba":"Huechuraba","quilicura":"Quilicura","recoleta":"Recoleta",
    "independencia":"Independencia","renca":"Renca","cerro-navia":"Cerro Navia",
    "lo-prado":"Lo Prado","conchali":"Conchalí","cerrillos":"Cerrillos",
    "el-bosque":"El Bosque","lo-espejo":"Lo Espejo",
    "pedro-aguirre-cerda":"Pedro Aguirre Cerda","san-joaquin":"San Joaquín",
    "la-pintana":"La Pintana","san-ramon":"San Ramón","macul":"Macul",
    "san-jose-de-maipo":"San José de Maipo","colina":"Colina","lampa":"Lampa",
    "buin":"Buín","talagante":"Talagante","penaflor":"Peñaflor",
    "melipilla":"Melipilla","calera-de-tango":"Calera de Tango",
    "el-monte":"El Monte","isla-de-maipo":"Isla de Maipo","pirque":"Pirque",
    "curacavi":"Curacaví","tiltil":"Tiltil","padre-hurtado":"Padre Hurtado",
    "paine":"Paine","maria-pinto":"María Pinto","san-pedro":"San Pedro"
}

# ─── VEHICLES (32) ────────────────────────────────────────────────────────
VEHICLES = [
    ("nissan-kicks","Nissan Kicks","1.6L","SUV compacto"),
    ("toyota-corolla","Toyota Corolla","1.8L","Sedán"),
    ("honda-civic","Honda Civic","1.5L","Sedán"),
    ("hyundai-tucson","Hyundai Tucson","2.0L","SUV"),
    ("chevrolet-sail","Chevrolet Sail","1.5L","Sedán"),
    ("kia-rio","Kia Rio","1.4L","Sedán"),
    ("renault-duster","Renault Duster","1.6L","SUV"),
    ("ford-ecosport","Ford EcoSport","2.0L","SUV"),
    ("mazda-3","Mazda 3","2.0L","Sedán"),
    ("toyota-yaris","Toyota Yaris","1.5L","Sedán"),
    ("chevrolet-spark","Chevrolet Spark","1.0L","City car"),
    ("suzuki-swift","Suzuki Swift","1.4L","Hatchback"),
    ("nissan-versa","Nissan Versa","1.6L","Sedán"),
    ("hyundai-accent","Hyundai Accent","1.4L","Sedán"),
    ("kia-morning","Kia Morning","1.0L","City car"),
    ("peugeot-208","Peugeot 208","1.6L","Hatchback"),
    ("ford-fiesta","Ford Fiesta","1.5L","Sedán"),
    ("chevrolet-sonic","Chevrolet Sonic","1.6L","Sedán"),
    ("renault-logan","Renault Logan","1.6L","Sedán"),
    ("suzuki-celerio","Suzuki Celerio","1.0L","City car"),
    ("honda-city","Honda City","1.5L","Sedán"),
    ("suzuki-baleno","Suzuki Baleno","1.4L","Hatchback"),
    ("mg-3","MG 3","1.5L","Hatchback"),
    ("mg-zs","MG ZS","1.5L","SUV compacto"),
    ("mazda-cx-5","Mazda CX-5","2.5L","SUV"),
    ("honda-cr-v","Honda CR-V","2.4L","SUV"),
    ("subaru-forester","Subaru Forester","2.5L","SUV"),
    ("subaru-xv","Subaru XV","2.0L","SUV crossover"),
    ("peugeot-3008","Peugeot 3008","1.6L","SUV"),
    ("hyundai-grand-i10","Hyundai Grand i10","1.0L","City car"),
    ("fiat-bravo-tjet","Fiat Bravo T-Jet","1.4T","Sedán deportivo"),
    ("volkswagen-gol","Volkswagen Gol","1.6L","Hatchback")
]

# ─── SERVICES (20) ────────────────────────────────────────────────────────
SERVICES = [
    {"slug":"mecanico-a-domicilio","name":"Mecánico a Domicilio","icon":"fa-house-chimney-medical",
     "desc":"Atención mecánica profesional directamente en tu hogar u oficina"},
    {"slug":"scanner-automotriz","name":"Scanner Automotriz","icon":"fa-barcode",
     "desc":"Diagnóstico computarizado avanzado para detectar fallas electrónicas"},
    {"slug":"cambio-de-frenos","name":"Cambio de Frenos","icon":"fa-compact-disc",
     "desc":"Reparación y reemplazo de pastillas, discos y sistema de frenado completo"},
    {"slug":"cambio-de-pastillas","name":"Cambio de Pastillas de Freno","icon":"fa-compact-disc",
     "desc":"Reemplazo de pastillas de freno con medición de desgaste profesional"},
    {"slug":"cambio-de-aceite","name":"Cambio de Aceite","icon":"fa-oil-can",
     "desc":"Cambio de aceite y filtros con productos de alta calidad y especificaciones originales"},
    {"slug":"alineacion-y-balanceo","name":"Alineación y Balanceo","icon":"fa-bullseye",
     "desc":"Alineación computarizada y balanceo de neumáticos para manejo seguro"},
    {"slug":"reparacion-de-motor","name":"Reparación de Motor","icon":"fa-cogs",
     "desc":"Diagnóstico y reparación completa de motores a gasolina y diésel"},
    {"slug":"compresion-de-motor","name":"Compresión de Motor","icon":"fa-gauge-high",
     "desc":"Prueba de compresión y pre-compresión para evaluar estado interno del motor"},
    {"slug":"revision-por-kilometraje","name":"Revisión por Kilometraje","icon":"fa-road",
     "desc":"Mantención programada según kilometraje del fabricante"},
    {"slug":"reparacion-de-embrague","name":"Reparación de Embrague","icon":"fa-sync-alt",
     "desc":"Reemplazo y reparación de sistema de embrague completo"},
    {"slug":"correa-de-distribucion","name":"Correa de Distribución","icon":"fa-clock",
     "desc":"Cambio de correa de distribución con kit completo: tensor, rodillos y bomba de agua"},
    {"slug":"servicio-de-bateria","name":"Servicio de Batería","icon":"fa-car-battery",
     "desc":"Carga, reemplazo e instalación de baterías automotrices"},
    {"slug":"suspension-y-direccion","name":"Suspensión y Dirección","icon":"fa-arrows-alt-v",
     "desc":"Reparación de amortiguadores, rotulas, terminales y tren delantero"},
    {"slug":"electricidad-automotriz","name":"Electricidad Automotriz","icon":"fa-bolt",
     "desc":"Diagnóstico y reparación de sistemas eléctricos, alternadores y motores de arranque"},
    {"slug":"cambio-de-bujias","name":"Cambio de Bujías","icon":"fa-fire",
     "desc":"Reemplazo de bujías con apertura de gap según especificaciones técnicas"},
    {"slug":"mantencion-automotriz","name":"Mantención Automotriz","icon":"fa-clipboard-check",
     "desc":"Mantención preventiva integral para mantener tu vehículo en óptimas condiciones"},
    {"slug":"emergencias-mecanicas","name":"Emergencias Mecánicas","icon":"fa-truck-medical",
     "desc":"Auxilio mecánico 24/7 para averías en vía pública"},
    {"slug":"taller-mecanico-cerca","name":"Taller Mecánico Cerca","icon":"fa-map-marker-alt",
     "desc":"Servicio de taller mecánico profesional cerca de tu ubicación"},
    {"slug":"embragues-y-distribucion","name":"Embragues y Distribución","icon":"fa-cog",
     "desc":"Servicio especializado en sistemas de embrague y correa de distribución"},
    {"slug":"tren-delantero","name":"Tren Delantero","icon":"fa-car-side",
     "desc":"Revisión y reparación completa del tren delantero: rotulas, bieletas, terminales y amortiguadores"}
]

# ─── CROSS-LINK DATA ──────────────────────────────────────────────────────
# For each page type, we need related links to other comunas and vehicles
MAIN_COMUNAS = ["pudahuel","estacion-central","la-cisterna","san-bernardo","la-granja","la-florida","maipu"]

# FAQ templates per service type
FAQ_TEMPLATES = {
    "mecanico-a-domicilio": [
        ("¿Cuánto cuesta un mecánico a domicilio{extra}?",
         "El costo depende del servicio requerido. Un cambio de aceite parte desde valores accesibles, mientras que reparaciones mayores varían según complejidad. Cotiza sin compromiso por WhatsApp con {business} y recibe un presupuesto transparente a domicilio."),
        ("¿Cuánto demoran en llegar{extra}?",
         "En la mayoría de los casos atendemos en menos de 24 horas. Nuestro servicio de emergencia 24/7 puede llegar incluso el mismo día. La zona poniente de Santiago está cubierta con alta disponibilidad por nuestros técnicos."),
        ("¿Qué servicios ofrecen a domicilio{extra}?",
         "Ofrecemos mecánica general, reparación de frenos, embrague, electricidad automotriz, scanner diagnóstico, cambio de aceite, alineación, suspensión, batería, bujías, correa de distribución, mantención preventiva y emergencias 24/7."),
        ("¿Atienden emergencias las 24 horas{extra}?",
         "Sí, {business} ofrece servicio de emergencias mecánicas 24/7. Si tu auto no arranca, tiene una falla en la vía pública o necesita auxilio inmediato, llámanos o escribe por WhatsApp y un técnico estará contigo en menos de 60 minutos."),
        ("¿Qué marcas de vehículos atienden{extra}?",
         "Atendemos todas las marcas: Toyota, Hyundai, Kia, Chevrolet, Nissan, Renault, Peugeot, Ford, Volkswagen, Honda, Mazda, Suzuki, Subaru, Fiat, MG y más. Nuestros técnicos se desplazan con herramientas especializadas para cada tipo de vehículo.")
    ],
    "scanner": [
        ("¿Qué es un scanner automotriz{extra}?",
         "Un scanner automotriz es un equipo de diagnóstico electrónico que se conecta al puerto OBD-II de tu vehículo para leer códigos de falla de todos los sistemas: motor, transmisión, ABS, airbags y más. En {business} usamos escáneres de última generación."),
        ("¿Cuánto cuesta el scanner automotriz{extra}?",
         "El servicio de escaneo diagnóstico tiene precios accesibles. Incluye lectura de códigos, diagnóstico del problema y presupuesto de reparación. Cotiza por WhatsApp con {business} para conocer el costo exacto según tu vehículo."),
        ("¿Pueden borrar códigos de falla{extra}?",
         "Sí, nuestro equipo puede borrar códigos de falla una vez que el problema mecánico ha sido resuelto. Es importante no borrar códigos sin antes diagnosticar la causa raíz para evitar que la falla reaparezca."),
        ("¿Cuándo debo hacer un escaneo a mi vehículo{extra}?",
         "Debes escanear tu vehículo cuando se encienda el check engine, haya fallas en el motor, pérdida de potencia, consumo excesivo de combustible o cualquier luz de advertencia en el tablero."),
        ("¿El scanner funciona en cualquier vehículo{extra}?",
         "Sí, nuestro escáner es compatible con todos los vehículos fabricados desde 1996 que cuenten con puerto OBD-II. Atendemos todas las marcas y modelos en la Región Metropolitana de Santiago de Chile.")
    ],
    "frenos": [
        ("¿Cuánto cuesta el cambio de frenos{extra}?",
         "El costo del cambio de frenos depende del modelo del vehículo y el tipo de pastillas y discos requeridos. Cotiza por WhatsApp con {business} para un presupuesto detallado y transparente sin costo adicional por el diagnóstico."),
        ("¿Cada cuánto debo cambiar las pastillas de freno?",
         "Las pastillas de freno deben revisarse cada 10.000 km y generalmente se reemplazan entre los 25.000 y 40.000 km dependiendo del tipo de conducción. La conducción urbana con tráfico acelera el desgaste."),
        ("¿Cómo sé si mis frenos están malos?",
         "Los síntomas principales son: chirrido al frenar, vibración en el volante, pedal suave o esponjoso, el auto tira hacia un lado al frenar, o el check de frenos encendido en el tablero. {business} realiza diagnóstico gratuito."),
        ("¿Usan pastillas originales{extra}?",
         "En {business} trabajamos con pastillas y discos de marcas reconocidas que cumplen o superan las especificaciones originales del fabricante. Ofrecemos opciones premium y estándar según tu presupuesto."),
        ("¿El cambio de frenos incluye garantía{extra}?",
         "Sí, todos nuestros servicios de frenos incluyen garantía. En {business} respaldamos cada trabajo realizado con repuestos de calidad instalados por técnicos certificados.")
    ],
    "aceite": [
        ("¿Cuánto cuesta el cambio de aceite{extra}?",
         "El costo depende del tipo de aceite requerido (sintético, semi-sintético o mineral) y la cantidad según tu vehículo. Cotiza por WhatsApp con {business} para recibir un presupuesto inmediato y transparente."),
        ("¿Cada cuántos kilómetros debo cambiar el aceite?",
         "Generalmente cada 10.000 km si usas aceite sintético o cada 5.000 km con aceite mineral. Consulta el manual de tu vehículo para las especificaciones exactas del fabricante."),
        ("¿Qué tipo de aceite usan para mi vehículo{extra}?",
         "En {business} utilizamos aceites sintéticos y semi-sintéticos premium de marcas como Castrol, Mobil y Shell, ajustados a las especificaciones técnicas recomendadas por cada fabricante."),
        ("¿El cambio de aceite incluye filtro?",
         "Sí, nuestro servicio de cambio de aceite incluye el reemplazo del filtro de aceite, revisión del filtro de aire y checkeo de niveles de refrigerante y líquido de frenos sin costo adicional."),
        ("¿Cuánto demora el cambio de aceite a domicilio{extra}?",
         "El cambio de aceite a domicilio demora aproximadamente 30 a 45 minutos. Nuestros técnicos llegan a tu ubicación con todo el equipamiento necesario en la Región Metropolitana.")
    ],
    "motor": [
        ("¿Cuánto cuesta reparar un motor{extra}?",
         "El costo de reparación del motor varía según el tipo de falla y el modelo del vehículo. {business} realiza diagnóstico completo antes de presupuestar para garantizar transparencia. Cotiza por WhatsApp."),
        ("¿Qué es la prueba de compresión?",
         "La prueba de compresión mide la presión dentro de cada cilindro del motor para evaluar el estado de pistones, anillos y válvulas. Valores bajos o desiguales indican desgaste interno que requiere reparación."),
        ("¿Cuándo debo preocuparme por el motor de mi auto?",
         "Debes prestar atención a: pérdida de potencia, consumo excesivo de aceite o combustible, humo blanco/azul/negro del escape, ruidos metálicos, vibraciones anormales o fallas de encendido recurrentes."),
        ("¿Reparan motores de cualquier marca{extra}?",
         "Sí, en {business} contamos con experiencia en motores de todas las marcas y cilindrajes, desde motores pequeños de city cars hasta motores de SUV y pickups pesadas."),
        ("¿La reparación de motor incluye garantía{extra}?",
         "Sí, todas las reparaciones de motor realizadas por {business} incluyen garantía por el trabajo realizado y los repuestos utilizados.")
    ],
    "suspension": [
        ("¿Cuánto cuesta reparar la suspensión{extra}?",
         "El costo depende de los componentes a reemplazar: amortiguadores, rotulas, terminales, bieletas o resortes. {business} realiza diagnóstico completo para un presupuesto exacto sin sorpresas."),
        ("¿Cuándo debo cambiar los amortiguadores?",
         "Los amortiguadores deben revisarse cada 50.000 km y reemplazarse generalmente entre los 80.000 y 100.000 km. Si notas vibraciones, el auto rebota excesivamente o desgaste irregular de neumáticos, es hora de revisarlos."),
        ("¿Qué incluye el servicio de tren delantero{extra}?",
         "El servicio de tren delantero en {business} incluye revisión completa de: amortiguadores, rotulas, terminales de dirección, bieletas, bujes, resortes y coeficiente de amortiguación."),
        ("¿La mala suspensión afecta los frenos?",
         "Sí, una suspensión en mal estado afecta negativamente el sistema de frenado, aumenta la distancia de frenado, causa vibraciones y genera desgaste prematuro de neumáticos y componentes del tren delantero."),
        ("¿Ofrecen alineación y balanceo{extra}?",
         "Sí, {business} realiza alineación computarizada y balanceo de neumáticos como parte del servicio integral de suspensión y dirección a domicilio en la Región Metropolitana.")
    ],
    "electricidad": [
        ("¿Cuánto cuesta el diagnóstico eléctrico{extra}?",
         "El diagnóstico eléctrico automotriz tiene precios accesibles. Incluye medición de batería, alternador, motor de arranque y revisión del sistema de cableado. Cotiza por WhatsApp con {business}."),
        ("¿Por qué no arranca mi auto?",
         "Las causas más comunes son: batería descargada, falla en el motor de arranque, alternador defectuoso, fusibles quemados o problemas en el sistema de inyección electrónica. {business} diagnostica la causa exacta a domicilio."),
        ("¿Con qué frecuencia debo cambiar la batería?",
         "La batería automotriz dura entre 2 y 4 años según el uso y clima. En Santiago, las temperaturas extremas aceleran el desgaste. {business} mide la carga de tu batería sin costo para evaluar su estado."),
        ("¿Reparan sistemas eléctricos complejos{extra}?",
         "Sí, en {business} tenemos experiencia en sistemas eléctricos de cualquier complejidad: ECU, sensores, módulos electrónicos, sistemas de inyección, luces, centralitas y cableado completo."),
        ("¿Qué servicios de batería ofrecen{extra}?",
         "{business} ofrece: medición de carga gratuita, carga de batería, venta e instalación de baterías nuevas, limpieza de terminales y revisión del sistema de carga completo (alternador y regulador).")
    ],
    "embrague": [
        ("¿Cuánto cuesta reparar el embrague{extra}?",
         "El costo depende del modelo del vehículo y si se reemplaza solo el disco o el kit completo (disco, plato y collarín). Cotiza por WhatsApp con {business} para un presupuesto exacto y transparente."),
        ("¿Cuáles son los síntomas de un embrague gastado?",
         "Los síntomas principales son: dificultad para cambiar marchas, pedal suave o esponjoso, trepidaciones al arrancar, olor a quemado y pérdida de potencia al acelerar en pendientes."),
        ("¿Cuándo cambiar la correa de distribución?",
         "La correa de distribución debe cambiarse según las especificaciones del fabricante, generalmente entre los 80.000 y 120.000 km. No cambiarla a tiempo puede causar daños catastróficos al motor."),
        ("¿Qué incluye el servicio de embragues y distribución{extra}?",
         "El servicio completo incluye: reemplazo de kit de embrague, correa de distribución con tensor y rodillos, bomba de agua, y alineación del volante del motor con herramientas especializadas."),
        ("¿El servicio incluye garantía{extra}?",
         "Sí, {business} otorga garantía en todos los servicios de embrague y correa de distribución. Utilizamos repuestos de calidad que cumplen las especificaciones del fabricante.")
    ],
    "mantencion": [
        ("¿Qué incluye una mantención automotriz{extra}?",
         "La mantención incluye: cambio de aceite y filtros, revisión de frenos, suspensión, niveles de líquidos, bujías, correas, batería, luces y neumáticos. {business} ofrece planes personalizados según tu vehículo."),
        ("¿Cada cuánto debo llevar mi auto a mantención?",
         "Recomendamos mantención cada 10.000 km o cada 6 meses, lo que ocurra primero. Vehículos con uso intensivo en ciudad pueden requerir intervalos más cortos. Consulta el manual del fabricante."),
        ("¿Cuánto cuesta la mantención{extra}?",
         "El costo varía según el tipo de mantención (básica, intermedia o completa) y el modelo del vehículo. {business} ofrece presupuestos transparentes por WhatsApp sin costo ni compromiso."),
        ("¿Hacen mantención a domicilio{extra}?",
         "Sí, {business} realiza mantención automotriz completa a domicilio en la Región Metropolitana de Santiago de Chile. Llegamos a tu hogar u oficina con todas las herramientas y repuestos necesarios."),
        ("¿Por qué es importante la mantención preventiva?",
         "La mantención preventiva evita reparaciones costosas, prolonga la vida útil del motor, mejora el rendimiento de combustible, garantiza tu seguridad y ayuda a aprobar la revisión técnica sin problemas.")
    ],
    "emergencias": [
        ("¿Atienden emergencias las 24 horas{extra}?",
         "Sí, {business} ofrece auxilio mecánico las 24 horas del día, los 7 días de la semana en toda la Región Metropolitana de Santiago de Chile. Llámanos o escribe por WhatsApp para atención inmediata."),
        ("¿Qué hago si mi auto se daña en la carretera?",
         "Mantén la calma, señaliza tu vehículo con las luces de emergencia y triangles, ubícate en un lugar seguro y contáctanos por WhatsApp o llamada. {business} envía un técnico a tu ubicación de inmediato."),
        ("¿Cuánto cuesta el servicio de emergencia{extra}?",
         "El costo depende del tipo de avería y la ubicación. {business} cotiza en el momento sin costos ocultos. Puedes escribirnos por WhatsApp con una foto o descripción del problema."),
        ("¿Qué tipo de emergencias atienden{extra}?",
         "Atendemos: auto que no arranca, pinchaduras, fallas eléctricas, sobrecalentamiento, pérdida de frenos, accidentes menores, problemas con el embrague y cualquier emergencia mecánica en la vía pública."),
        ("¿Cuánto demoran en llegar a una emergencia{extra}?",
         "Tiempo promedio de llegada es de 30 a 60 minutos dentro de la Región Metropolitana. {business} tiene técnicos distribuidos estratégicamente para minimizar los tiempos de respuesta.")
    ],
    "general": [
        ("¿Cuánto cuesta el servicio{extra}?",
         "El costo depende del tipo de servicio y el modelo de tu vehículo. {business} ofrece presupuestos transparentes sin costo adicional por diagnóstico. Contáctanos por WhatsApp para una cotización inmediata."),
        ("¿Qué formas de pago aceptan{extra}?",
         "En {business} aceptamos efectivo, transferencia bancaria y tarjetas de débito/crédito. Facilitamos el pago con multiple opciones para tu comodidad."),
        ("¿Los repuestos tienen garantía{extra}?",
         "Sí, todos los repuestos instalados por {business} cuentan con garantía. Trabajamos con repuestos de calidad que cumplen o superan las especificaciones del fabricante original."),
        ("¿Atienden en mi comuna{extra}?",
         "Atendemos en todas las comunas de la Región Metropolitana de Santiago de Chile. {business} tiene cobertura total desde Lo Barnechea hasta Puente Alto, y desde Maipú hasta Las Condes."),
        ("¿Cómo puedo agendar un servicio{extra}?",
         "Puedes agendar fácilmente por WhatsApp al {wa}, llamando al {phone} o por email a {email}. {business} te confirma la fecha y hora según tu disponibilidad.")
    ],
    "tren-delantero": [
        ("¿Cuánto cuesta la reparación del tren delantero{extra}?",
         "El costo depende de los componentes dañados: rotulas, terminales, bieletas, amortiguadores o bujes. {business} realiza diagnóstico completo para un presupuesto exacto sin sorpresas."),
        ("¿Cuáles son los síntomas de tren delantero dañado?",
         "Síntomas incluyen: ruidos al pasar por baches o badenes, vibración en el volante, desgaste irregular de neumáticos, el auto tira hacia un lado, y dirección inestable a alta velocidad."),
        ("¿Cuándo debo revisar el tren delantero?",
         "Recomendamos revisar el tren delantero cada 20.000 km o cuando notes cualquier síntoma anormal. Una revisión oportuna evita daños mayores y costosos en el sistema de suspensión y dirección."),
        ("¿La revisión del tren delantero incluye alineación{extra}?",
         "Sí, {business} incluye revisión de alineación como parte del diagnóstico del tren delantero. Si se detecta desalineación, realizamos la corrección computarizada inmediatamente."),
        ("¿Trabajan con repuestos originales{extra}?",
         "En {business} usamos repuestos de marcas reconocidas que cumplen las especificaciones del fabricante. Ofrecemos opciones originales y alternativas de calidad premium según tu presupuesto.")
    ]
}

def get_faq_key(service_slug):
    """Map service slug to FAQ template key."""
    if "mecanico-a-domicilio" in service_slug or "taller" in service_slug:
        return "mecanico-a-domicilio"
    if "scanner" in service_slug:
        return "scanner"
    if "freno" in service_slug or "pastilla" in service_slug:
        return "frenos"
    if "aceite" in service_slug:
        return "aceite"
    if "motor" in service_slug or "compresion" in service_slug or "kilometraje" in service_slug:
        return "motor"
    if "suspension" in service_slug or "alineacion" in service_slug or "tren" in service_slug:
        return "suspension"
    if "electricidad" in service_slug or "bateria" in service_slug or "bujia" in service_slug:
        return "electricidad"
    if "embrague" in service_slug or "distribucion" in service_slug:
        return "embrague"
    if "mantencion" in service_slug or "mantenimiento" in service_slug:
        return "mantencion"
    if "emergencia" in service_slug:
        return "emergencias"
    return "general"

def pick_related_comunas(current_comuna, count=8):
    """Pick related comunas for cross-linking."""
    if current_comuna:
        others = [c for c in MAIN_COMUNAS if c != current_comuna]
        remaining = [c for c in COMUNAS if c != current_comuna and c not in others]
        random.shuffle(remaining)
        return (others + remaining[:count - len(others)])[:count]
    return MAIN_COMUNAS[:count]

def pick_related_vehicles(current_vehicle, count=6):
    """Pick related vehicles for cross-linking."""
    if current_vehicle:
        others = [v for v in VEHICLES if v[0] != current_vehicle]
        random.shuffle(others)
        return others[:count]
    return VEHICLES[:count]

def pick_related_services(current_service, count=6):
    """Pick related services for cross-linking."""
    if current_service:
        others = [s for s in SERVICES if s["slug"] != current_service]
        random.shuffle(others)
        return others[:count]
    return SERVICES[:count]

# ─── CONTENT GENERATION ───────────────────────────────────────────────────

SEO_INTROS = {
    "mecanico-a-domicilio": [
        "Necesitas un mecánico de confianza que llegue a tu puerta sin complicaciones? En {business} llevamos el taller mecánico directamente a tu hogar u oficina con herramientas de diagnóstico de última generación y técnicos con más de 15 años de experiencia.",
        "Olvídate de esperar horas en un taller. Con el servicio de mecánico a domicilio de {business}, un técnico certificado llega a tu ubicación con todo el equipamiento necesario para resolver cualquier problema mecánico de forma profesional.",
        "El servicio mecánico a domicilio de {business} es la alternativa moderna al taller tradicional. Atendemos en toda la Región Metropolitana con precios competitivos, garantía en cada trabajo y la comodidad que mereces."
    ],
    "scanner": [
        "El diagnóstico computarizado es la primera herramienta profesional para detectar fallas ocultas en tu vehículo. En {business} usamos escáneres de última generación que leen códigos de todos los sistemas electrónicos.",
        "Un escaneo automotriz profesional puede ahorrarte miles de pesos en reparaciones innecesarias. {business} identifica la falla exacta de tu vehículo sin adivinar, con tecnología OBD-II de diagnóstico avanzado.",
        "Cuando se enciende el check engine o alguna luz de advertencia en el tablero, no ignores la señal. {business} realiza un escaneo completo que determina la causa raíz del problema con precisión."
    ],
    "frenos": [
        "Los frenos son el sistema de seguridad más importante de tu vehículo. En {business} evaluamos el estado de pastillas, discos, latiguillos y fluido hidráulico para garantizar tu seguridad y la de tu familia.",
        "Un sistema de frenos en buen estado marca la diferencia entre una conducción segura y un accidente. {business} reemplaza pastillas, rectifica discos y purga el sistema hidráulico con productos de alta especificación.",
        "No esperes a escuchar chirridos al frenar para revisar tus frenos. {business} realiza diagnóstico gratuito del estado de tus pastillas y discos con medición digital profesional."
    ],
    "aceite": [
        "El cambio de aceite periódico es la inversión más económica para prolongar la vida útil del motor de tu vehículo. {business} usa aceites sintéticos y semi-sintéticos premium que cumplen las especificaciones del fabricante.",
        "Un motor con aceite limpio y en el nivel correcto funciona mejor, consume menos combustible y dura más años. {business} realiza el cambio a domicilio con filtros nuevos y verificación de niveles completa.",
        "El aceite de motor degrada con el uso y las altas temperaturas, perdiendo sus propiedades lubricantes. {business} recomienda intervalos de cambio según las especificaciones de cada marca y modelo."
    ],
    "motor": [
        "La reparación de motores es una especialidad que requiere experiencia y herramientas precisas. En {business} diagnosticamos fallas con pruebas de compresión, pre-compresión y análisis de gases de escape.",
        "Problemas como pérdida de potencia, consumo excesivo de aceite, ruidos metálicos o humo del escape requieren atención inmediata. {business} evalúa el estado interno de tu motor antes de intervenir.",
        "La prueba de compresión es el examen médico del motor: mide la presión en cada cilindro para detectar desgaste de anillos, válvulas o juntas de culata. {business} ofrece este servicio a domicilio."
    ],
    "suspension": [
        "La suspensión es responsable de la estabilidad, comodidad y adherencia de tu vehículo al camino. {business} revisa amortiguadores, rotulas, terminales, bieletas y resortes con diagnóstico profesional.",
        "Conducir con la suspensión dañada genera desgaste prematuro de neumáticos, pérdida de control en curvas y aumento de la distancia de frenado. {business} restaura el tren delantero a condiciones óptimas.",
        "El tren delantero es el conjunto de componentes que conectan las ruedas con el chasis. {business} revisa y repara cada pieza: rotulas, terminales de dirección, bieletas y bujes con herramientas especializadas."
    ],
    "electricidad": [
        "Los sistemas eléctricos modernos son complejos y requieren diagnóstico especializado. {business} detecta fallas en baterías, alternadores, motores de arranque, sensores y módulos electrónicos con equipos profesionales.",
        "Si tu auto no arranca, las luces fallan o hay problemas intermitentes en el tablero, la causa puede ser eléctrica. {business} realiza un diagnóstico completo del sistema eléctrico a domicilio.",
        "La batería es el corazón del sistema eléctrico de tu vehículo. {business} mide la carga, revisa terminales, verifica el alternador y determina si necesitas carga o reemplazo, todo a domicilio."
    ],
    "embrague": [
        "El embrague y la correa de distribución son componentes críticos que requieren reemplazo en los intervalos correctos. {business} realiza estos servicios con repuestos de calidad y herramientas especializadas.",
        "Ignorar un embrague gastado puede dañar el volante del motor y el sistema de transmisión. {business} reemplaza el kit completo (disco, plato y collarín) con garantía en el trabajo realizado.",
        "La correa de distribución sincroniza el movimiento del motor. Su rotura puede causar daños catastróficos. {business} la reemplaza con kit completo: correa, tensor, rodillos y bomba de agua."
    ],
    "mantencion": [
        "La mantención preventiva es la mejor inversión para tu vehículo. {business} ofrece planes personalizados que incluyen cambio de aceite, filtros, revisión de frenos, suspensión, batería, bujías y niveles de líquidos.",
        "Un vehículo bien mantenido gasta menos combustible, contamina menos, tiene menor riesgo de fallas y aprueba la revisión técnica sin problemas. {business} lleva la mantención a tu domicilio.",
        "No esperes a que algo falle. La mantención programada según kilometraje previene reparaciones costosas y prolonga la vida útil de tu motor, transmisión y sistemas críticos."
    ],
    "emergencias": [
        "Las averías no avisan. Cuando tu auto te deja varado en la vía pública, {business} ofrece auxilio mecánico las 24 horas para ayudarte a volver a la ruta lo antes posible.",
        "Un servicio de emergencias mecánicas rápido y confiable marca la diferencia entre una molestia menor y un problema grave. {business} tiene técnicos disponibles 24/7 en toda la Región Metropolitana.",
        "Ya sea que tu auto no arranque, se sobrecaliente o tenga una falla eléctrica en plena vía, {business} envía un técnico a tu ubicación en menos de 60 minutos con herramientas y repuestos."
    ],
    "tren-delantero": [
        "El tren delantero es fundamental para la estabilidad y seguridad de tu vehículo. {business} revisa rotulas, terminales, bieletas, amortiguadores y bujes con diagnóstico profesional completo.",
        "Ruidos al girar, vibraciones en el volante o desgaste irregular de neumáticos son señales de problemas en el tren delantero. {business} identifica y repara cada componente dañado.",
        "Una revisión periódica del tren delantero previene daños mayores y costosos. {business} recomienda chequear cada 20.000 km o ante cualquier síntoma anormal de dirección o suspensión."
    ],
    "general": [
        "En {business} ofrecemos una solución integral para el mantenimiento y reparación de tu vehículo. Con más de 15 años de experiencia en el rubro automotriz, garantizamos un servicio profesional y confiable.",
        "La confianza de más de 1.000 clientes respalda nuestro trabajo. {business} se destaca por la transparencia en precios, la calidad de los repuestos y la garantía en cada servicio realizado.",
        "Servicio profesional a domicilio con atención personalizada. {business} lleva la experiencia de un taller mecánico completo directamente a tu ubicación en la Región Metropolitana."
    ]
}

def get_seo_key(service_slug):
    if "mecanico-a-domicilio" in service_slug or "taller" in service_slug:
        return "mecanico-a-domicilio"
    if "scanner" in service_slug:
        return "scanner"
    if "freno" in service_slug or "pastilla" in service_slug:
        return "frenos"
    if "aceite" in service_slug:
        return "aceite"
    if "motor" in service_slug or "compresion" in service_slug or "kilometraje" in service_slug:
        return "motor"
    if "suspension" in service_slug or "alineacion" in service_slug:
        return "suspension"
    if "electricidad" in service_slug or "bateria" in service_slug or "bujia" in service_slug:
        return "electricidad"
    if "embrague" in service_slug or "distribucion" in service_slug:
        return "embrague"
    if "mantencion" in service_slug or "mantenimiento" in service_slug:
        return "mantencion"
    if "emergencia" in service_slug:
        return "emergencias"
    if "tren" in service_slug:
        return "tren-delantero"
    return "general"

# ─── HOW-TO STEPS ─────────────────────────────────────────────────────────
HOWTO_STEPS = {
    "mecanico-a-domicilio": [
        ("Contacta por WhatsApp","Escribe a {business} por WhatsApp describiendo el problema de tu vehículo y tu ubicación."),
        ("Diagnóstico a domicilio","Un técnico especializado se desplaza a tu ubicación con herramientas de diagnóstico de última generación."),
        ("Presupuesto transparente","Recibes un diagnóstico y presupuesto claro sin compromiso antes de cualquier reparación."),
        ("Reparación inmediata","El técnico realiza la reparación con repuestos de calidad y herramientas profesionales."),
        ("Verificación y garantía","Se verifica el funcionamiento correcto y se entrega garantía del trabajo realizado.")
    ],
    "scanner": [
        ("Conexión OBD-II","Se conecta el escáner al puerto de diagnóstico OBD-II de tu vehículo."),
        ("Lectura de códigos","Se leen todos los códigos de falla almacenados en los diferentes módulos electrónicos."),
        ("Diagnóstico del problema","Se interpreta cada código y se correlaciona con los síntomas del vehículo."),
        ("Verificación de componentes","Se verifican físicamente los componentes relacionados con las fallas detectadas."),
        ("Presupuesto de reparación","Se entrega un presupuesto detallado para la reparación necesaria con opciones de repuestos.")
    ],
    "frenos": [
        ("Inspección visual","Se revisan visualmente pastillas, discos, latiguillos y pinzas de freno."),
        ("Medición de desgaste","Se mide el espesor de pastillas y la variación de discos con calibrador digital."),
        ("Diagnóstico hidráulico","Se verifica el nivel y condición del fluido de frenos y el sistema hidráulico."),
        ("Reemplazo de componentes","Se reemplazan las pastillas y/o discos según corresponda con repuestos de calidad."),
        ("Purga y prueba","Se purga el sistema hidráulico y se realizan pruebas de frenado para verificar el correcto funcionamiento.")
    ],
    "aceite": [
        ("Preparación","Se estaciona el vehículo en superficie plana y se deja enfriar el motor 15 minutos."),
        ("Drenaje","Se retira el tapón de drenaje y se deja salir el aceite usado completamente."),
        ("Filtro nuevo","Se reemplaza el filtro de aceite por uno nuevo y se limpia la superficie de contacto."),
        ("Llenado","Se vierte aceite nuevo con la viscosidad y cantidad recomendada por el fabricante."),
        ("Verificación","Se enciende el motor, se verifica el nivel con la varilla y se revisan fugas.")
    ],
    "motor": [
        ("Diagnóstico inicial","Se realiza inspección visual del motor y se consulta los síntomas reportados por el conductor."),
        ("Prueba de compresión","Se mide la presión en cada cilindro con un compresímetro calibrado."),
        ("Análisis de resultados","Se comparan los valores de compresión con las especificaciones del fabricante."),
        ("Presupuesto de reparación","Se determina el tipo de reparación necesaria y se entrega presupuesto detallado."),
        ("Reparación","Se realizan las reparaciones mecánicas necesarias con repuestos de calidad y herramientas especializadas.")
    ],
    "suspension": [
        ("Prueba de manejo","Se realiza una prueba de manejo para detectar síntomas de suspensión dañada."),
        ("Inspección en taller","Se levanta el vehículo y se inspeccionan amortiguadores, rotulas, terminales y bieletas."),
        ("Medición de holguras","Se miden las holguras de cada componente del tren delantero con herramientas de precisión."),
        ("Reemplazo","Se reemplazan los componentes dañados con repuestos de calidad."),
        ("Alineación final","Se realiza alineación computarizada para asegurar el correcto manejo del vehículo.")
    ],
    "electricidad": [
        ("Medición de batería","Se mide el voltaje y la capacidad de arranque de la batería con tester profesional."),
        ("Prueba de alternador","Se verifica que el alternador genere la corriente correcta para cargar la batería."),
        ("Revisión de arranque","Se prueba el motor de arranque y el sistema de encendido."),
        ("Diagnóstico de cableado","Se revisan fusibles, relés y cableado en busca de cortocircuitos o conexiones defectuosas."),
        ("Reparación","Se reemplazan los componentes defectuosos y se verifica el correcto funcionamiento del sistema.")
    ],
    "embrague": [
        ("Diagnóstico del embrague","Se evalúa el desgaste del disco, plato y collarín del embrague según los síntomas."),
        ("Desmontaje","Se desmonta la transmisión para acceder al sistema de embrague completo."),
        ("Reemplazo de kit","Se reemplaza el kit de embrague (disco, plato, collarín y rodamiento) con repuestos de calidad."),
        ("Montaje","Se monta la transmisión y se ajustan los componentes según especificaciones técnicas."),
        ("Prueba de manejo","Se realiza prueba de manejo para verificar el correcto funcionamiento del embrague nuevo.")
    ],
    "mantencion": [
        ("Revisión general","Se inspecciona el estado general del vehículo: neumáticos, luces, limpiaparabrisas y niveles."),
        ("Cambio de aceite","Se realiza el cambio de aceite y filtro con productos según especificaciones del fabricante."),
        ("Revisión de frenos","Se mide el espesor de pastillas y se verifica el sistema de frenado completo."),
        ("Checkeo eléctrico","Se revisa batería, luces y sistemas electrónicos básicos del vehículo."),
        ("Entrega de informe","Se entrega un informe detallado del estado del vehículo con recomendaciones futuras.")
    ],
    "emergencias": [
        ("Comunicación inmediata","Contacta a {business} por WhatsApp o llamada telefónica las 24 horas."),
        ("Localización","Proporciona tu ubicación exacta o comparte tu posición por GPS."),
        ("Despacho de técnico","Se despacha un técnico con herramientas y repuestos básicos a tu ubicación."),
        ("Diagnóstico en sitio","El técnico diagnostica la falla y determina si puede repararse en el lugar."),
        ("Solución o traslado","Se repara el vehículo en sitio o se coordina el traslado al taller más cercano.")
    ],
    "tren-delantero": [
        ("Inspección visual","Se revisan visualmente todos los componentes del tren delantero buscando signos de desgaste."),
        ("Prueba de manejo","Se realiza prueba de manejo para detectar vibraciones, ruidos o inestabilidad en la dirección."),
        ("Medición de holguras","Se miden holguras de rotulas, terminales y bieletas con herramientas de precisión."),
        ("Reemplazo de piezas","Se reemplazan los componentes desgastados con repuestos nuevos de calidad garantizada."),
        ("Alineación computarizada","Se realiza alineación y balanceo para restablecer la estabilidad del vehículo.")
    ]
}

def get_howto_key(service_slug):
    k = get_seo_key(service_slug)
    if k == "general":
        return "mecanico-a-domicilio"
    if k == "suspension" and "tren" in service_slug:
        return "tren-delantero"
    if k == "electricidad" and "bujia" in service_slug:
        return "mantencion"
    if k == "electricidad" and "bateria" in service_slug:
        return "electricidad"
    if k == "motor" and "kilometraje" in service_slug:
        return "mantencion"
    if k == "motor" and "compresion" in service_slug:
        return "motor"
    return k

def make_hash(text):
    """Create a numeric hash for deterministic content selection."""
    return int(hashlib.md5(text.encode()).hexdigest()[:8], 16)

def pick_item(lst, key, index=0):
    """Deterministically pick an item from a list."""
    h = make_hash(key + str(index))
    return lst[h % len(lst)]

# ─── JSON HELPER ─────────────────────────────────────────────────────────
def json_s(text):
    return json.dumps(text, ensure_ascii=False)

# ─── PAGE BUILDER ─────────────────────────────────────────────────────────

def build_comuna_dropdown_links():
    links = ""
    for c in COMUNAS:
        name = COMUNA_DISPLAY.get(c, c)
        links += f'<li><a class="dropdown-item" href="comunas/{c}.html">{name}</a></li>\n'
    return links

def build_vehicle_dropdown_links():
    links = ""
    for v in VEHICLES:
        links += f'<li><a class="dropdown-item" href="vehiculos/{v[0]}.html">{v[1]}</a></li>\n'
    return links

def build_service_dropdown_links():
    links = ""
    for s in SERVICES:
        slug = s["slug"]
        name = s["name"]
        links += f'<li><a class="dropdown-item" href="{slug}.html">{name}</a></li>\n'
    return links

def build_footer_links():
    """Build footer columns."""
    # Comunas column
    comunas_html = ""
    for c in MAIN_COMUNAS + COMUNAS[7:15]:
        name = COMUNA_DISPLAY.get(c, c)
        comunas_html += f'<li><a href="comunas/{c}.html">{name}</a></li>\n'

    # Services column
    services_html = ""
    for s in SERVICES[:10]:
        services_html += f'<li><a href="{s["slug"]}.html">{s["name"]}</a></li>\n'

    # Vehicles column
    vehicles_html = ""
    for v in VEHICLES[:10]:
        vehicles_html += f'<li><a href="vehiculos/{v[0]}.html">{v[1]}</a></li>\n'

    return comunas_html, services_html, vehicles_html

FOOTER_COMUNAS, FOOTER_SERVICES, FOOTER_VEHICLES = build_footer_links()

def generate_page(page_type, service_slug, service_name, service_icon, service_desc,
                   comuna_slug=None, comuna_display=None,
                   vehicle_slug=None, vehicle_display=None, vehicle_engine=None, vehicle_type=None,
                   page_index=0):
    """Generate a complete HTML landing page."""

    seo_key = get_seo_key(service_slug)
    faq_key = get_faq_key(service_slug)
    howto_key = get_howto_key(service_slug)

    # Build context strings
    loc_str = ""
    if comuna_display:
        loc_str = f" en {comuna_display}"
    veh_str = ""
    if vehicle_display:
        veh_str = f" para {vehicle_display}"

    page_id = f"{service_slug}-{comuna_slug or 'x'}-{vehicle_slug or 'x'}-{page_index}"
    h = make_hash(page_id)

    # ─── TITLE & META ─────────────────────────────────────────────────
    if page_type == "A":
        title = f"{service_name} en {comuna_display} | LLANOCAR Servicios Automotrices"
        meta_desc = f"{service_name} en {comuna_display}, Santiago. Atención a domicilio con garantía. {service_desc}. Cotiza por WhatsApp al {PHONE}. Region Metropolitana de Chile."
        breadcrumb_2 = {"name": "Comunas", "item": f"{DOMAIN}/comunas/"}
        breadcrumb_3 = {"name": comuna_display, "item": f"{DOMAIN}/comunas/{comuna_slug}.html"}
        breadcrumb_4 = {"name": service_name, "item": f"{DOMAIN}/{service_slug}-en-{comuna_slug}.html"}
    elif page_type == "B":
        title = f"{service_name} para {vehicle_display} | LLANOCAR Servicios Automotrices"
        meta_desc = f"{service_name} para {vehicle_display} ({vehicle_engine}) en Santiago. Atención a domicilio con garantía. Cotiza por WhatsApp al {PHONE}. Region Metropolitana de Chile."
        breadcrumb_2 = {"name": "Vehículos", "item": f"{DOMAIN}/vehiculos/"}
        breadcrumb_3 = {"name": vehicle_display, "item": f"{DOMAIN}/vehiculos/{vehicle_slug}.html"}
        breadcrumb_4 = {"name": service_name, "item": f"{DOMAIN}/{service_slug}-{vehicle_slug}.html"}
    elif page_type == "C":
        title = f"{service_name} en Santiago | LLANOCAR Servicios Automotrices"
        meta_desc = f"{service_name} en Santiago, Chile. Servicio profesional a domicilio con garantía. {service_desc}. Cotiza por WhatsApp al {PHONE}. Todas las comunas de la RM."
        breadcrumb_2 = {"name": "Servicios", "item": f"{DOMAIN}/#servicios"}
        breadcrumb_3 = {"name": service_name, "item": f"{DOMAIN}/{service_slug}.html"}
        breadcrumb_4 = None
    else:  # D
        title = f"{service_name} para {vehicle_display} en {comuna_display} | LLANOCAR"
        meta_desc = f"{service_name} para {vehicle_display} en {comuna_display}, Santiago. Servicio a domicilio con garantía. {service_desc}. WhatsApp {PHONE}. Region Metropolitana."
        breadcrumb_2 = {"name": "Comunas", "item": f"{DOMAIN}/comunas/"}
        breadcrumb_3 = {"name": comuna_display, "item": f"{DOMAIN}/comunas/{comuna_slug}.html"}
        breadcrumb_4 = {"name": f"{service_name} - {vehicle_display}", "item": f"{DOMAIN}/{service_slug}-{vehicle_slug}-en-{comuna_slug}.html"}

    # ─── FAQ ──────────────────────────────────────────────────────────
    faq_template = FAQ_TEMPLATES.get(faq_key, FAQ_TEMPLATES["general"])
    faqs = []
    for i, (q, a) in enumerate(faq_template):
        extra_q = loc_str if "extra" in q else ""
        extra_q = extra_q or veh_str
        faqs.append({
            "question": q.format(extra=extra_q),
            "answer": a.format(extra=extra_q, business=BUSINESS, wa=WA_NUMBER, phone=PHONE, email=EMAIL)
        })

    faq_json = '{"mainEntity":[' + ','.join(
        '{"@type":"Question","name":' + json_s(f["question"]) + ',"acceptedAnswer":{"@type":"Answer","text":' + json_s(f["answer"]) + '}}'
        for f in faqs
    ) + ']}'

    # ─── BREADCRUMB JSON-LD ──────────────────────────────────────────
    crumbs = [
        '{"@type":"ListItem","position":1,"name":"Inicio","item":"' + DOMAIN + '/"}',
        '{"@type":"ListItem","position":2,"name":"' + breadcrumb_2["name"] + '","item":"' + breadcrumb_2["item"] + '"}',
        '{"@type":"ListItem","position":3,"name":"' + breadcrumb_3["name"] + '","item":"' + breadcrumb_3["item"] + '"}'
    ]
    if breadcrumb_4:
        crumbs.append('{"@type":"ListItem","position":4,"name":"' + breadcrumb_4["name"] + '","item":"' + breadcrumb_4["item"] + '"}')
    breadcrumb_json = '{"itemListElement":[' + ','.join(crumbs) + ']}'

    # ─── SERVICE JSON-LD ─────────────────────────────────────────────
    service_json = json.dumps({
        "serviceType": service_name,
        "name": f"{service_name}{loc_str}{veh_str}",
        "description": f"{service_desc}{loc_str}{veh_str}. Atención a domicilio en la Región Metropolitana de Santiago de Chile.",
        "provider": {
            "@type": "LocalBusiness",
            "name": BUSINESS,
            "telephone": PHONE,
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "Puerto Madero 9678",
                "addressLocality": comuna_display or "Pudahuel",
                "addressRegion": "Región Metropolitana",
                "addressCountry": "CL"
            }
        },
        "areaServed": {"@type": "City", "name": comuna_display or "Santiago"},
        "url": f"{DOMAIN}/{service_slug}-en-{comuna_slug}.html" if comuna_slug else f"{DOMAIN}/{service_slug}.html"
    }, ensure_ascii=False)

    # ─── HOWTO JSON-LD ───────────────────────────────────────────────
    steps = HOWTO_STEPS.get(howto_key, HOWTO_STEPS["mecanico-a-domicilio"])
    howto_steps_json = '[' + ','.join(
        '{"@type":"HowToStep","name":' + json_s(s[0]) + ',"text":' + json_s(s[1].format(business=BUSINESS)) + '}'
        for s in steps
    ) + ']'
    howto_json = json.dumps({
        "name": f"Cómo realizar {service_name.lower()}{loc_str}{veh_str}",
        "description": f"Guía paso a paso para {service_name.lower()}{loc_str}{veh_str} por un profesional certificado.",
        "totalTime": "PT45M",
        "step": json.loads(howto_steps_json)
    }, ensure_ascii=False)

    # ─── SEO CONTENT SECTIONS ────────────────────────────────────────
    intro = pick_item(SEO_INTROS.get(seo_key, SEO_INTROS["general"]), page_id, 0).format(business=BUSINESS)

    # Related items for cross-links
    rel_comunas = pick_related_comunas(comuna_slug)
    rel_vehicles = pick_related_vehicles(vehicle_slug)
    rel_services = pick_related_services(service_slug)

    # Build H1
    h1_parts = [service_name]
    if vehicle_display:
        h1_parts.append(f"para {vehicle_display}")
    if comuna_display:
        h1_parts.append(f"en {comuna_display}")
    h1_text = " | ".join(h1_parts)

    # Build unique paragraph content using hash for variety
    random.seed(h)

    seo_para1 = f"""Buscando <strong>{service_name.lower()}{loc_str}</strong>? En <strong>{BUSINESS}</strong> somos especialistas en servicios automotrices con atención a domicilio en toda la Región Metropolitana de Santiago de Chile. {intro}"""
    if vehicle_display:
        seo_para1 += f""" Nuestro equipo conoce a fondo cada componente del <strong>{vehicle_display}</strong> ({vehicle_engine}, tipo {vehicle_type}), desde su motor hasta sus sistemas electrónicos y de suspensión."""

    para2_variants = [
        f"Ya sea que necesites una {service_name.lower()} de emergencia o una revisión programada, en {BUSINESS} ofrecemos la flexibilidad de atenderte donde te encuentres sin tener que trasladarte a un taller.",
        f"La {service_name.lower()} es uno de los servicios más solicitados en {comuna_display or 'Santiago'}. Por eso hemos optimizado nuestros tiempos de respuesta para que un técnico esté contigo lo antes posible.",
        f"Nuestros técnicos certificados cuentan con experiencia en {service_name.lower()} para todas las marcas y modelos{veh_str}. Utilizamos herramientas de diagnóstico de última generación para garantizar resultados precisos.",
        f"En {BUSINESS} entendemos que tu tiempo es valioso. Nuestra {service_name.lower()} a domicilio te ahorra traslados, esperas y el estrés de ir a un taller. Atendemos de lunes a domingo.",
    ]
    seo_para2 = pick_item(para2_variants, page_id, 1)

    para3_variants = [
        f"Los residentes de {comuna_display or 'Santiago'} confían en {BUSINESS} por nuestra transparencia en precios, la calidad de nuestros repuestos y la garantía en cada trabajo. Más de 1.000 vehículos han sido atendidos por nuestro equipo.",
        f"Si vives en {comuna_display or 'Santiago'} o sus alrededores, estás a un WhatsApp de recibir atención profesional. Escribenos al {WA_NUMBER} y un técnico estará contigo en menos de lo que imaginas.",
        f"El servicio de {service_name.lower()} de {BUSINESS} se distingue por la atención personalizada. No tratamos a todos los vehículos igual: cada diagnóstico es único y cada presupuesto se adapta a tu situación.",
        f"Trabajamos con repuestos de marcas reconocidas que cumplen las especificaciones del fabricante, garantizando durabilidad y rendimiento. Cada {service_name.lower()} incluye una verificación completa del sistema.",
    ]
    seo_para3 = pick_item(para3_variants, page_id, 2)

    # Why choose us section
    why_items = [
        ("fa-clock", "Atención Rápida", f"Técnico{loc_str} en menos de 24 horas. Servicio de emergencia 24/7 disponible para urgencias."),
        ("fa-shield-alt", "Garantía Total", "Todos nuestros servicios incluyen garantía. Respaldamos cada reparación con repuestos de calidad."),
        ("fa-tools", "Técnicos Certificados", "Equipo de mecánicos con más de 15 años de experiencia y formación continua en nuevas tecnologías."),
        ("fa-hand-holding-usd", "Precios Transparentes", "Presupuesto claro sin costos ocultos. Cotiza sin compromiso por WhatsApp antes de cualquier intervención."),
        ("fa-map-marked-alt", "Cobertura Total RM", "Atendemos en todas las comunas de la Región Metropolitana de Santiago de Chile, desde Lo Barnechea hasta Puente Alto."),
        ("fa-star", "Más de 1.000 Clientes", "La confianza de nuestros clientes es nuestra mejor carta de presentación. Lee sus experiencias y decide con seguridad."),
    ]

    # Coverage section
    coverage_text = f"{BUSINESS} brinda cobertura completa en la Región Metropolitana de Santiago de Chile. Nuestras rutas de servicio cubren todas las comunas de la RM con tiempos de respuesta optimizados."

    # ─── BUILD HTML ──────────────────────────────────────────────────

    # Navbar dropdowns
    comuna_dd = build_comuna_dropdown_links()
    vehicle_dd = build_vehicle_dropdown_links()
    service_dd = build_service_dropdown_links()

    # Cross-link comuna items
    cross_comunas_html = ""
    for c in rel_comunas:
        name = COMUNA_DISPLAY.get(c, c)
        cross_comunas_html += f'<a href="{service_slug}-en-{c}.html" class="badge bg-secondary text-decoration-none m-1 p-2">{service_name} en {name}</a>\n'

    # Cross-link vehicle items
    cross_vehicles_html = ""
    for v in rel_vehicles:
        cross_vehicles_html += f'<a href="{service_slug}-{v[0]}.html" class="badge bg-secondary text-decoration-none m-1 p-2">{service_name} para {v[1]}</a>\n'

    # Cross-link service items
    cross_services_html = ""
    for s in rel_services:
        s_slug = s["slug"]
        s_icon = s["icon"]
        s_name = s["name"]
        target = f"{s_slug}-en-{comuna_slug}.html" if comuna_slug else f"{s_slug}-{vehicle_slug}.html" if vehicle_slug else f"{s_slug}.html"
        cross_services_html += f'<a href="{target}" class="badge bg-secondary text-decoration-none m-1 p-2"><i class="fas {s_icon} me-1"></i>{s_name}</a>\n'

    # Related comuna simple list
    related_comunas_list = ""
    for c in rel_comunas[:6]:
        name = COMUNA_DISPLAY.get(c, c)
        related_comunas_list += f'<a href="comunas/{c}.html" class="text-decoration-none" style="color:var(--primary);">{name}</a>, '

    related_vehicles_list = ""
    for v in rel_vehicles[:4]:
        related_vehicles_list += f'<a href="vehiculos/{v[0]}.html" class="text-decoration-none" style="color:var(--primary);">{v[1]}</a>, '

    # Service cards HTML
    service_cards = ""
    for i, svc in enumerate(rel_services[:6]):
        bg = "white" if i % 2 == 0 else "#f9fafb"
        border = "border-left" if i % 2 == 0 else "border-right"
        service_cards += f'''
      <div class="col-lg-6 col-md-6 mb-4">
        <div class="p-4 rounded shadow-sm" style="background:{bg};{border}:4px solid var(--primary);min-height:200px;">
          <div class="d-flex align-items-center gap-3 mb-3">
            <div style="min-width:45px;height:45px;border-radius:50%;background:var(--primary);display:flex;align-items:center;justify-content:center;color:white;font-size:1.1rem;flex-shrink:0;">
              <i class="fas {svc["icon"]}"></i>
            </div>
            <h3 class="fw-bold mb-0" style="color:#333;font-size:1.1rem;">{svc["name"]}{loc_str}</h3>
          </div>
          <p style="font-size:0.92rem;color:#555;line-height:1.8;text-align:justify;margin-bottom:0;">{svc["desc"]}{loc_str}. En {BUSINESS} ofrecemos atención profesional a domicilio{loc_str} con técnicos certificados y garantía en cada servicio realizado.</p>
        </div>
      </div>'''

    # HowTo steps HTML
    howto_html = ""
    steps_list = HOWTO_STEPS.get(howto_key, HOWTO_STEPS["mecanico-a-domicilio"])
    for i, (sname, stext) in enumerate(steps_list, 1):
        stext_filled = stext.format(business=BUSINESS)
        howto_html += f'''
        <div class="col-md-6 col-lg-4 mb-3">
          <div class="d-flex align-items-start gap-3 p-3 rounded" style="background:white;border-left:4px solid var(--primary);">
            <div style="min-width:40px;height:40px;border-radius:50%;background:var(--primary);display:flex;align-items:center;justify-content:center;color:white;font-weight:bold;font-size:1.1rem;flex-shrink:0;">{i}</div>
            <div>
              <h6 class="fw-bold text-dark mb-1" style="font-size:.9rem;">{sname}</h6>
              <p class="small text-muted mb-0" style="font-size:.8rem;">{stext_filled}</p>
            </div>
          </div>
        </div>'''

    # FAQ accordion HTML
    faq_accordion = ""
    for i, faq in enumerate(faqs):
        collapse_id = f"faq-collapse-{h}-{i}"
        header_id = f"faq-header-{h}-{i}"
        faq_accordion += f'''
        <div class="accordion-item">
          <h3 class="accordion-header" id="{header_id}">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#{collapse_id}" aria-expanded="false" aria-controls="{collapse_id}">
              {faq["question"]}
            </button>
          </h3>
          <div id="{collapse_id}" class="accordion-collapse collapse" aria-labelledby="{header_id}" data-bs-parent="#faqAccordion">
            <div class="accordion-body" style="color:#555;line-height:1.8;">
              {faq["answer"]}
            </div>
          </div>
        </div>'''

    # Why-us cards
    why_cards = ""
    for w_icon, w_title, w_desc in why_items:
        why_cards += f'''
        <div class="col-lg-4 col-md-6 mb-4">
          <div class="text-center p-4">
            <div class="mb-3"><i class="fas {w_icon}" style="font-size:2.5rem;color:var(--primary);"></i></div>
            <h4 class="fw-bold mb-2" style="font-size:1.1rem;">{w_title}</h4>
            <p class="text-muted" style="font-size:.9rem;">{w_desc}</p>
          </div>
        </div>'''

    # Coverage comuna list
    coverage_comunas = ""
    for c in rel_comunas:
        name = COMUNA_DISPLAY.get(c, c)
        coverage_comunas += f'<a href="comunas/{c}.html" class="badge bg-dark text-decoration-none m-1 p-2">{name}</a> '

    html = f'''<!DOCTYPE html>
<html lang="es-CL">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{meta_desc}">
<link rel="canonical" href="{DOMAIN}/{service_slug}{"-en-"+comuna_slug if comuna_slug else ""}{"-"+vehicle_slug if vehicle_slug else ""}.html">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta_desc}">
<meta property="og:image" content="{DOMAIN}/images/image1.jpg">
<meta property="og:url" content="{DOMAIN}/{service_slug}{"-en-"+comuna_slug if comuna_slug else ""}{"-"+vehicle_slug if vehicle_slug else ""}.html">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_CL">
<meta property="og:site_name" content="{BUSINESS}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{meta_desc}">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="icon" type="image/png" href="images/image1.jpg">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","@id":"{DOMAIN}/#{service_slug}-faq",{faq_json}}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Service","@id":"{DOMAIN}/#{service_slug}-service",{service_json}}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","@id":"{DOMAIN}/#{service_slug}-breadcrumb",{breadcrumb_json}}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"HowTo","@id":"{DOMAIN}/#{service_slug}-howto",{howto_json}}}
</script>
<style>
:root{{--primary:#E87722;--primary-dark:#C4611A;--black:#1A1A1A;--gold:#F5A623;--orange2:#FF8C00;--orange3:#FFB347;}}
*{{box-sizing:border-box;}}
html{{scroll-behavior:smooth;scroll-padding-bottom:100px;}}
body{{font-family:'Segoe UI',system-ui,-apple-system,sans-serif;color:#333;margin:0;padding:0;}}
.navbar{{background:var(--black)!important;padding:12px 0;border-bottom:3px solid var(--primary);}}
.navbar-brand,.logo-text{{font-weight:800;font-size:1.4rem;color:#fff!important;text-decoration:none;}}
.logo-sub{{font-size:.7rem;color:#999;text-transform:uppercase;letter-spacing:1px;}}
.logo-box{{width:42px;height:42px;background:var(--primary);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:1.1rem;margin-right:10px;}}
.nav-link{{color:#ccc!important;font-size:.92rem;transition:.3s;}}
.nav-link:hover,.nav-link.active{{color:var(--primary)!important;}}
.dropdown-menu{{background:var(--black);border:1px solid #333;max-height:400px;overflow-y:auto;}}
.dropdown-item{{color:#ccc!important;font-size:.88rem;}}
.dropdown-item:hover,.dropdown-item.active{{background:var(--primary)!important;color:#fff!important;}}
.hero{{background:linear-gradient(135deg,rgba(26,26,26,.92),rgba(26,26,26,.78)),url(images/image1.jpg) center/cover no-repeat;min-height:80vh;display:flex;align-items:center;color:#fff;padding:100px 0 60px;}}
.hero h1{{font-weight:800;font-size:clamp(1.8rem,5vw,3.2rem);line-height:1.15;margin-bottom:20px;}}
.hero .lead{{font-size:1.1rem;max-width:600px;color:#ddd;line-height:1.7;}}
.btn-wa{{background:#25D366;color:#fff;border:none;padding:12px 28px;border-radius:50px;font-weight:700;font-size:1.05rem;text-decoration:none;display:inline-flex;align-items:center;gap:8px;transition:.3s;}}
.btn-wa:hover{{background:#1ebc57;color:#fff;transform:translateY(-2px);}}
.btn-call{{background:var(--primary);color:#fff;border:none;padding:12px 28px;border-radius:50px;font-weight:700;font-size:1.05rem;text-decoration:none;display:inline-flex;align-items:center;gap:8px;transition:.3s;}}
.btn-call:hover{{background:var(--primary-dark);color:#fff;transform:translateY(-2px);}}
.seo-section{{background:#f8f9fa;padding:60px 0;border-bottom:4px solid var(--primary);}}
.seo-section h2{{font-weight:700;font-size:1.6rem;color:var(--primary);margin-bottom:20px;text-align:center;}}
.seo-section p{{font-size:1.02rem;line-height:1.85;color:#444;text-align:justify;margin-bottom:18px;}}
.section-dark{{background:var(--black);padding:60px 0;color:#fff;}}
.section-dark h2{{color:var(--primary);font-weight:700;font-size:1.8rem;text-align:center;margin-bottom:40px;}}
.section-dark p{{color:#ccc;line-height:1.8;}}
.section-light{{background:#fff;padding:60px 0;}}
.section-light h2{{color:var(--primary);font-weight:700;font-size:1.8rem;text-align:center;margin-bottom:10px;}}
.section-light .subtitle{{color:#888;text-align:center;max-width:700px;margin:0 auto 40px auto;font-size:1rem;}}
.cta-bar{{background:linear-gradient(135deg,var(--primary) 0%,var(--orange2) 100%);padding:40px 0;color:#fff;text-align:center;}}
.cta-bar h2{{font-weight:800;margin-bottom:15px;}}
.cta-bar p{{font-size:1.1rem;margin-bottom:25px;opacity:.9;}}
.accordion-button:not(.collapsed){{background:var(--primary);color:#fff;}}
.accordion-button:focus{{box-shadow:0 0 0 .25rem rgba(232,119,34,.25);}}
.footer{{background:#000;color:#999;padding:50px 0 20px;border-top:4px solid var(--primary);font-size:.88rem;}}
.footer h5{{color:#fff;font-weight:700;text-transform:uppercase;margin-bottom:18px;font-size:1rem;border-bottom:2px solid var(--primary);display:inline-block;padding-bottom:5px;}}
.footer ul{{list-style:none;padding:0;margin:0;}}
.footer li{{margin-bottom:8px;}}
.footer a{{color:#999;text-decoration:none;transition:.3s;}}
.footer a:hover{{color:var(--primary);padding-left:5px;}}
.footer .contact-item{{display:flex;gap:10px;margin-bottom:12px;align-items:flex-start;}}
.footer .contact-item i{{color:var(--primary);margin-top:4px;}}
.copyright{{background:#0a0a0a;padding:15px 0;text-align:center;font-size:.82rem;color:#666;border-top:1px solid #222;margin-top:30px;}}
.sticky-bar{{position:fixed;bottom:0;left:0;width:100%;background:var(--black);padding:10px 15px;z-index:9999;border-top:3px solid var(--primary);display:flex;gap:10px;justify-content:center;align-items:center;}}
.sticky-bar a{{flex:1;max-width:250px;text-align:center;padding:14px 10px;border-radius:10px;color:#fff!important;font-weight:700;font-size:1rem;text-decoration:none;display:flex;align-items:center;justify-content:center;gap:8px;transition:.2s;}}
.sticky-wa{{background:#25D366;}}
.sticky-wa:hover{{background:#1ebc57;}}
.sticky-call{{background:var(--primary);}}
.sticky-call:hover{{background:var(--primary-dark);}}
@media(min-width:992px){{.sticky-bar a{{max-width:300px;font-size:1.15rem;padding:16px 20px;}}}}
@media(max-width:768px){{.hero{{min-height:auto;padding:100px 0 50px;text-align:center;}}.hero .lead{{margin:0 auto;}}}}
</style>
</head>
<body>

<!-- NAVBAR -->
<nav class="navbar navbar-expand-lg fixed-top">
<div class="container">
  <a href="index.html" class="navbar-brand d-flex align-items-center">
    <div class="logo-box"><i class="fas fa-wrench"></i></div>
    <div><div class="logo-text">LLANOCAR</div><div class="logo-sub">Servicios Automotrices</div></div>
  </a>
  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navMenu"><span class="navbar-toggler-icon"></span></button>
  <div class="collapse navbar-collapse" id="navMenu">
    <ul class="navbar-nav ms-auto">
      <li class="nav-item"><a class="nav-link" href="index.html">Inicio</a></li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown">Servicios</a>
        <ul class="dropdown-menu">{service_dd}</ul>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown">Vehículos</a>
        <ul class="dropdown-menu">{vehicle_dd}</ul>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown">Comunas</a>
        <ul class="dropdown-menu">{comuna_dd}</ul>
      </li>
      <li class="nav-item"><a class="nav-link" href="contacto.html">Contacto</a></li>
      <li class="nav-item"><a class="nav-link" href="quienes-somos.html">Quiénes Somos</a></li>
    </ul>
  </div>
</div>
</nav>

<!-- HERO -->
<section class="hero">
<div class="container">
  <div class="row align-items-center">
    <div class="col-lg-7">
      <h1>{h1_text}</h1>
      <p class="lead">{service_desc}{loc_str}{veh_str}. En <strong>{BUSINESS}</strong> brindamos atención profesional a domicilio en la Región Metropolitana de Santiago de Chile. Más de 15 años de experiencia y más de 1.000 vehículos atendidos con garantía.</p>
      <div class="d-flex flex-wrap gap-3 mt-4">
        <a href="https://wa.me/{WA_NUMBER}?text=Hola%20necesito%20{service_slug.replace('-','%20')}{loc_str.replace(' ', '%20')}{veh_str.replace(' ', '%20')}" class="btn-wa" target="_blank"><i class="fab fa-whatsapp"></i> Cotizar por WhatsApp</a>
        <a href="tel:{PHONE.replace(' ','')}" class="btn-call"><i class="fas fa-phone-alt"></i> Llamar</a>
      </div>
    </div>
    <div class="col-lg-5 text-center mt-4 mt-lg-0">
      <div style="background:rgba(255,255,255,.08);border-radius:16px;padding:30px;border:1px solid rgba(255,255,255,.1);">
        <div style="font-size:3rem;font-weight:800;color:var(--gold);">+1000</div>
        <div style="color:#ccc;margin-bottom:20px;">Vehículos Atendidos</div>
        <div style="font-size:3rem;font-weight:800;color:var(--orange3);">+15</div>
        <div style="color:#ccc;margin-bottom:20px;">Años de Experiencia</div>
        <div style="font-size:2rem;font-weight:800;color:#fff;">24/7</div>
        <div style="color:#ccc;">Emergencias Mecánicas</div>
      </div>
    </div>
  </div>
</div>
</section>

<!-- SEO MAIN SECTION -->
<section class="seo-section">
<div class="container">
  <div class="row justify-content-center">
    <div class="col-lg-10">
      <h2><i class="fas {service_icon} me-2"></i>{service_name}{loc_str}{veh_str} - Servicio Profesional a Domicilio</h2>
      <p>{seo_para1}</p>
      <p>{seo_para2}</p>
      <p>{seo_para3}</p>
    </div>
  </div>
</div>
</section>

<!-- SERVICES LIST -->
<section class="section-light">
<div class="container">
  <h2><i class="fas fa-tools me-2"></i>Servicios Relacionados{loc_str}</h2>
  <p class="subtitle">Conoce todos los servicios automotrices que ofrecemos{loc_str} con atención a domicilio</p>
  <div class="row g-4">{service_cards}</div>
</div>
</section>

<!-- WHY CHOOSE US -->
<section class="section-dark">
<div class="container">
  <h2>¿Por Qué Elegir {BUSINESS}?</h2>
  <p class="text-center mb-5" style="max-width:700px;margin-left:auto;margin-right:auto;">Nos distinguimos por la calidad, transparencia y compromiso con cada cliente. Estas son las razones por las que miles de conductores confían en nosotros.</p>
  <div class="row g-4">{why_cards}</div>
</div>
</section>

<!-- HOW TO -->
<section class="section-light">
<div class="container">
  <h2><i class="fas fa-list-ol me-2"></i>Proceso de {service_name}</h2>
  <p class="subtitle">Así trabajamos paso a paso para garantizar un servicio profesional y confiable</p>
  <div class="row g-3">{howto_html}</div>
</div>
</section>

<!-- FAQ -->
<section class="seo-section" id="faq">
<div class="container">
  <div class="row justify-content-center">
    <div class="col-lg-9">
      <h2 class="mb-4"><i class="fas fa-question-circle me-2"></i>Preguntas Frecuentes sobre {service_name}{loc_str}</h2>
      <div class="accordion" id="faqAccordion">
        {faq_accordion}
      </div>
    </div>
  </div>
</div>
</section>

<!-- COVERAGE -->
<section class="section-dark" id="cobertura">
<div class="container">
  <h2><i class="fas fa-map-marked-alt me-2"></i>Cobertura{loc_str}</h2>
  <p class="text-center mb-4" style="max-width:700px;margin:0 auto;">{coverage_text} Nuestros técnicos se desplazan a tu ubicación en toda la RM.</p>
  <div class="text-center">
    {coverage_comunas}
  </div>
</div>
</section>

<!-- CROSS-LINKS: Related Services -->
<section class="section-light">
<div class="container">
  <h2><i class="fas fa-link me-2"></i>Otros Servicios que Podrías Necesitar</h2>
  <p class="subtitle">Explora todos nuestros servicios automotrices disponibles a domicilio</p>
  <div class="text-center">{cross_services_html}</div>
</div>
</section>

<!-- CROSS-LINKS: Related Comunas -->
<section class="seo-section">
<div class="container">
  <h2 class="mb-3"><i class="fas fa-map-pin me-2"></i>{service_name} en Otras Comunas</h2>
  <div class="text-center">{cross_comunas_html}</div>
  <div class="mt-4 text-center" style="color:#666;font-size:.92rem;">
    También atendemos en: {related_comunas_list.rstrip(", ")} y más comunas de la RM.
  </div>
</div>
</section>

<!-- CROSS-LINKS: Related Vehicles -->
{'<section class="section-light"><div class="container"><h2><i class="fas fa-car me-2"></i>{service_name} para Otros Vehículos</h2><div class="text-center">{cross_vehicles_html}</div><div class="mt-4 text-center" style="color:#666;font-size:.92rem;">También atendemos: {related_vehicles_list.rstrip(", ")} y muchas más marcas.</div></div></section>' if vehicle_slug else ''}

<!-- CTA -->
<section class="cta-bar">
<div class="container">
  <h2><i class="fas fa-phone-alt me-2"></i>¿Necesitas {service_name.lower()}{loc_str}?</h2>
  <p>Agenda tu cita hoy mismo. Atención inmediata y presupuesto sin compromiso.</p>
  <div class="d-flex flex-wrap justify-content-center gap-3">
    <a href="https://wa.me/{WA_NUMBER}?text=Hola%20necesito%20{service_slug.replace('-','%20')}{loc_str.replace(' ','%20')}{veh_str.replace(' ','%20')}" class="btn-wa" target="_blank"><i class="fab fa-whatsapp"></i> Escribir por WhatsApp</a>
    <a href="tel:{PHONE.replace(' ','')}" class="btn-call"><i class="fas fa-phone-alt"></i> {PHONE}</a>
  </div>
</div>
</section>

<!-- FOOTER -->
<footer class="footer">
<div class="container">
  <div class="row g-4">
    <div class="col-lg-4">
      <h5><i class="fas fa-wrench me-2"></i>{BUSINESS}</h5>
      <p>Tu mecánico de confianza en la Región Metropolitana de Santiago de Chile. Más de 15 años de experiencia brindando servicios automotrices de calidad a domicilio.</p>
      <div class="contact-item"><i class="fas fa-map-marker-alt"></i><span>{ADDRESS}</span></div>
      <div class="contact-item"><i class="fas fa-phone-alt"></i><span>{PHONE}</span></div>
      <div class="contact-item"><i class="fab fa-whatsapp"></i><span>{WA_NUMBER}</span></div>
      <div class="contact-item"><i class="fas fa-envelope"></i><span>{EMAIL}</span></div>
    </div>
    <div class="col-lg-2 col-md-4">
      <h5>Comunas</h5>
      <ul>{FOOTER_COMUNAS}</ul>
    </div>
    <div class="col-lg-3 col-md-4">
      <h5>Servicios</h5>
      <ul>{FOOTER_SERVICES}</ul>
    </div>
    <div class="col-lg-3 col-md-4">
      <h5>Vehículos</h5>
      <ul>{FOOTER_VEHICLES}</ul>
    </div>
  </div>
</div>
<div class="copyright">
  &copy; 2024 {BUSINESS}. Todos los derechos reservados. | Región Metropolitana de Santiago de Chile
</div>
</footer>

<!-- STICKY BOTTOM BAR -->
<div class="sticky-bar">
  <a href="https://wa.me/{WA_NUMBER}?text=Hola%20necesito%20{service_slug.replace('-','%20')}" class="sticky-wa" target="_blank"><i class="fab fa-whatsapp"></i> WhatsApp</a>
  <a href="tel:{PHONE.replace(' ','')}" class="sticky-call"><i class="fas fa-phone-alt"></i> Llamar {PHONE}</a>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>'''

    return html


# ─── PAGE GENERATION PLAN ────────────────────────────────────────────────

def generate_pages():
    """Generate all 200 pages."""
    generated = []
    page_index = 0

    # ─── TYPE A: Servicio + Comuna (80 pages) ────────────────────────
    # Use all 20 services × 4 comunas each
    print("=" * 60)
    print("TYPE A: Servicio + Comuna (80 pages)")
    print("=" * 60)

    # Shuffle comunas for variety
    all_comunas_shuffled = COMUNAS[:]
    random.seed(42)
    random.shuffle(all_comunas_shuffled)

    for svc in SERVICES:
        # Pick 4 comunas per service for 80 total
        start = (SERVICES.index(svc) * 4) % len(all_comunas_shuffled)
        selected_comunas = []
        for j in range(4):
            selected_comunas.append(all_comunas_shuffled[(start + j) % len(all_comunas_shuffled)])
        # Ensure main comunas get priority
        if SERVICES.index(svc) < len(MAIN_COMUNAS):
            selected_comunas[0] = MAIN_COMUNAS[SERVICES.index(svc)]

        for comuna_slug in selected_comunas:
            comuna_display = COMUNA_DISPLAY.get(comuna_slug, comuna_slug)
            filename = f"{svc['slug']}-en-{comuna_slug}.html"
            filepath = os.path.join(BASE_DIR, filename)

            html = generate_page(
                page_type="A",
                service_slug=svc["slug"],
                service_name=svc["name"],
                service_icon=svc["icon"],
                service_desc=svc["desc"],
                comuna_slug=comuna_slug,
                comuna_display=comuna_display,
                page_index=page_index
            )

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)

            generated.append(filename)
            print(f"  [{len(generated):3d}] A: {filename}")
            page_index += 1

    # ─── TYPE B: Servicio + Vehículo (60 pages) ─────────────────────
    print("\n" + "=" * 60)
    print("TYPE B: Servicio + Vehículo (60 pages)")
    print("=" * 60)

    all_vehicles_shuffled = VEHICLES[:]
    random.seed(43)
    random.shuffle(all_vehicles_shuffled)

    # 60 pages = 12 services × 5 vehicles
    type_b_services = SERVICES[:12]
    for svc in type_b_services:
        start_idx = (SERVICES.index(svc) * 5) % len(all_vehicles_shuffled)
        for j in range(5):
            v = all_vehicles_shuffled[(start_idx + j) % len(all_vehicles_shuffled)]
            filename = f"{svc['slug']}-{v[0]}.html"
            filepath = os.path.join(BASE_DIR, filename)

            html = generate_page(
                page_type="B",
                service_slug=svc["slug"],
                service_name=svc["name"],
                service_icon=svc["icon"],
                service_desc=svc["desc"],
                vehicle_slug=v[0],
                vehicle_display=v[1],
                vehicle_engine=v[2],
                vehicle_type=v[3],
                page_index=page_index
            )

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)

            generated.append(filename)
            print(f"  [{len(generated):3d}] B: {filename}")
            page_index += 1

    # ─── TYPE C: Servicio General (30 pages) ────────────────────────
    print("\n" + "=" * 60)
    print("TYPE C: Servicio General Landing (30 pages)")
    print("=" * 60)

    for svc in SERVICES[:30]:
        filename = f"{svc['slug']}.html"
        filepath = os.path.join(BASE_DIR, filename)

        html = generate_page(
            page_type="C",
            service_slug=svc["slug"],
            service_name=svc["name"],
            service_icon=svc["icon"],
            service_desc=svc["desc"],
            page_index=page_index
        )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)

        generated.append(filename)
        print(f"  [{len(generated):3d}] C: {filename}")
        page_index += 1

    # If we only have 20 services, add 10 more with slight variations
    if len(SERVICES) < 30:
        extra_services = [
            {"slug":"mantencion-a-domicilio","name":"Mantención a Domicilio","icon":"fa-house-chimney-medical","desc":"Mantención preventiva y correctiva de tu vehículo directamente en tu hogar u oficina"},
            {"slug":"taller-mecanico-a-domicilio","name":"Taller Mecánico a Domicilio","icon":"fa-wrench","desc":"El taller mecánico que llega a tu puerta con todas las herramientas y repuestos necesarios"},
            {"slug":"mecanico-de-emergencia","name":"Mecánico de Emergencia","icon":"fa-exclamation-triangle","desc":"Auxilio mecánico urgente las 24 horas para averías en la vía pública"},
            {"slug":"diagnostico-automotriz","name":"Diagnóstico Automotriz","icon":"fa-stethoscope","desc":"Diagnóstico computarizado profesional para detectar la causa exacta de cualquier falla"},
            {"slug":"revision-tecnica-preventiva","name":"Revisión Técnica Preventiva","icon":"fa-clipboard-list","desc":"Inspección completa para que tu vehículo apruebe la revisión técnica sin problemas"},
            {"slug":"cambio-de-filtros","name":"Cambio de Filtros","icon":"fa-filter","desc":"Reemplazo de filtros de aceite, aire, combustible y habitáculo para un motor limpio"},
            {"slug":"reparacion-de-frenos-abs","name":"Reparación de Frenos ABS","icon":"fa-shield-alt","desc":"Diagnóstico y reparación del sistema antibloqueo de frenos ABS"},
            {"slug":"sistema-de-enfriamiento","name":"Sistema de Enfriamiento","icon":"fa-temperature-low","desc":"Reparación de radiador, bomba de agua, termostato y sistema de refrigeración"},
            {"slug":"transmision-automatica","name":"Transmisión Automática","icon":"fa-cogs","desc":"Diagnóstico y reparación de cajas automáticas y transmisiones CVT"},
            {"slug":"mecanico-para-mujeres","name":"Mecánico para Mujeres","icon":"fa-female","desc":"Servicio automotriz con atención transparente, honesta y profesional para todas las conductoras"},
        ]
        for svc in extra_services:
            filename = f"{svc['slug']}.html"
            filepath = os.path.join(BASE_DIR, filename)

            html = generate_page(
                page_type="C",
                service_slug=svc["slug"],
                service_name=svc["name"],
                service_icon=svc["icon"],
                service_desc=svc["desc"],
                page_index=page_index
            )

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)

            generated.append(filename)
            print(f"  [{len(generated):3d}] C: {filename}")
            page_index += 1

    # ─── TYPE D: Servicio + Vehículo + Comuna (30 pages) ────────────
    print("\n" + "=" * 60)
    print("TYPE D: Servicio + Vehículo + Comuna (30 pages)")
    print("=" * 60)

    random.seed(44)
    d_services = SERVICES[:6]  # 6 services
    d_vehicles = VEHICLES[:10]  # first 10 vehicles
    d_comunas = MAIN_COMUNAS + COMUNAS[7:13]  # 12 comunas

    for i in range(30):
        svc = d_services[i % len(d_services)]
        v = d_vehicles[(i // 3) % len(d_vehicles)]
        c = d_comunas[i % len(d_comunas)]
        comuna_display = COMUNA_DISPLAY.get(c, c)

        filename = f"{svc['slug']}-{v[0]}-en-{c}.html"
        filepath = os.path.join(BASE_DIR, filename)

        html = generate_page(
            page_type="D",
            service_slug=svc["slug"],
            service_name=svc["name"],
            service_icon=svc["icon"],
            service_desc=svc["desc"],
            comuna_slug=c,
            comuna_display=comuna_display,
            vehicle_slug=v[0],
            vehicle_display=v[1],
            vehicle_engine=v[2],
            vehicle_type=v[3],
            page_index=page_index
        )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)

        generated.append(filename)
        print(f"  [{len(generated):3d}] D: {filename}")
        page_index += 1

    return generated


# ─── MAIN ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import json
    start_time = time.time()

    print(f"\n{'='*60}")
    print(f"LLANOCAR SEO Landing Page Generator")
    print(f"{'='*60}")
    print(f"Output directory: {BASE_DIR}")
    print(f"Domain: {DOMAIN}")
    print(f"Business: {BUSINESS}")
    print(f"{'='*60}\n")

    pages = generate_pages()

    elapsed = time.time() - start_time

    print(f"\n{'='*60}")
    print(f"GENERATION COMPLETE")
    print(f"{'='*60}")
    print(f"Total pages generated: {len(pages)}")
    print(f"Time elapsed: {elapsed:.1f} seconds")

    # Count by type
    type_a = len([p for p in pages if '-en-' in p and not any(v[0] in p for v in VEHICLES)])
    type_b = len([p for p in pages if any(v[0] in p for v in VEHICLES) and '-en-' not in p])
    type_c = len([p for p in pages if not '-en-' in p and not any(v[0] in p for v in VEHICLES)])
    type_d = len([p for p in pages if '-en-' in p and any(v[0] in p for v in VEHICLES)])

    print(f"\nBreakdown:")
    print(f"  Type A (Servicio + Comuna):   {type_a}")
    print(f"  Type B (Servicio + Vehículo):  {type_b}")
    print(f"  Type C (Servicio General):     {type_c}")
    print(f"  Type D (Serv+Veh+Comuna):      {type_d}")

    # Write list to file
    with open(os.path.join(BASE_DIR, "generated_200_pages_list.txt"), "w") as f:
        f.write(f"LLANOCAR Generated Pages - {len(pages)} total\n")
        f.write(f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"{'='*60}\n\n")
        for p in sorted(pages):
            f.write(f"{p}\n")

    print(f"\nPage list saved to: generated_200_pages_list.txt")
    print(f"{'='*60}")
