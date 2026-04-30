import random

comunas = [
    "providencia", "las-condes", "nunoa", "maipu", "la-florida", "puente-alto",
    "san-bernardo", "santiago-centro", "estacion-central", "la-cisterna",
    "quilicura", "recoleta", "independencia", "san-miguel", "cerrillos",
    "pedro-aguirre-cerda", "lo-prado", "cerro-navia", "renca", "conchali",
    "vitacura", "huechuraba", "penalolen", "la-granja", "la-pintana",
    "macul", "san-joaquin", "el-bosque", "pudahuel", "melipilla",
    "buin", "san-ramon", "colina", "lampa", "curacavi", "el-monte",
    "isla-de-maipo", "calera-de-tango", "maria-pinto", "padre-hurtado",
    "paine", "penaflor", "san-jose-de-maipo", "pirque", "tiltil",
    "quinta-normal", "lo-espejo", "talagante", "alhue"
]

servicios = [
    "mecanico-a-domicilio", "revision-tecnica", "cambio-de-aceite",
    "cambio-de-frenos", "cambio-de-pastillas", "reparacion-de-embrague",
    "scanner-automotriz", "diagnostico-electronico", "suspension-y-direccion",
    "alineacion-y-balanceo", "cambio-de-bujias", "aire-acondicionado-automotriz",
    "reparacion-de-motor", "electricidad-automotriz", "mantencion-preventiva",
    "cambio-de-amortiguadores", "cambio-de-correa-de-distribucion",
    "reparacion-de-caja-de-cambio", "cambio-de-bateria", "servicio-de-emergencia",
    "inspeccion-pre-compra", "reparacion-de-frenos-abs", "cambio-de-filtros",
    "limpieza-de-inyectores", "reparacion-de-alternador", "cambio-de-discos-de-freno"
]

vehiculos = [
    "toyota-corolla", "nissan-kicks", "hyundai-accent", "kia-rio",
    "chevrolet-sail", "renault-duster", "ford-ecosport", "mazda-3",
    "honda-civic", "suzuki-swift", "subaru-forester", "chevrolet-spark",
    "peugeot-208", "hyundai-tucson", "mg-zs", "renault-logan",
    "suzuki-celerio", "honda-city", "ford-fiesta", "toyota-yaris",
    "volkswagen-gol", "kia-morning", "hyundai-grand-i10", "subaru-xv",
    "peugeot-3008", "chevrolet-sonic", "mg-3", "fiat-bravo-tjet"
]

# Generate unique combinations
names = set()

# Pattern 1: servicio + comuna (80 names)
while len([n for n in names if n.startswith(tuple(servicios[:5]))]) < 80:
    s = random.choice(servicios)
    c = random.choice(comunas)
    names.add(f"{s}-{c}.jpg")

# Pattern 2: servicio + vehiculo (40 names)
while len([n for n in names if any(v in n for v in vehiculos)]) < 40:
    s = random.choice(servicios)
    v = random.choice(vehiculos)
    names.add(f"{s}-{v}.jpg")

# Pattern 3: vehiculo + comuna (40 names)
while len([n for n in names if any(v in n for v in vehiculos) and any(c in n for c in comunas) and not any(s.split('-')[0] in n for s in servicios)]) < 40:
    v = random.choice(vehiculos)
    c = random.choice(comunas)
    names.add(f"{v}-{c}.jpg")

# Pattern 4: taller-mecanico + comuna (20 names)
while len([n for n in names if 'taller-mecanico' in n]) < 20:
    c = random.choice(comunas)
    names.add(f"taller-mecanico-{c}.jpg")

# Pattern 5: mecanico-emergencia + comuna (20 names)
while len([n for n in names if 'mecanico-de-emergencia' in n or 'auxilio-mecanico' in n]) < 20:
    s = random.choice(["mecanico-de-emergencia", "auxilio-mecanico", "mecanico-24-horas"])
    c = random.choice(comunas)
    names.add(f"{s}-{c}.jpg")

# Fill up to exactly 200
all_patterns = []
for s in servicios:
    for c in comunas:
        all_patterns.append(f"{s}-{c}.jpg")
for s in servicios:
    for v in vehiculos:
        all_patterns.append(f"{s}-{v}.jpg")
for v in vehiculos:
    for c in comunas:
        all_patterns.append(f"{v}-{c}.jpg")
for c in comunas:
    all_patterns.append(f"taller-mecanico-{c}.jpg")
    all_patterns.append(f"mecanico-de-emergencia-{c}.jpg")
    all_patterns.append(f"auxilio-mecanico-{c}.jpg")

random.shuffle(all_patterns)
for name in all_patterns:
    if len(names) >= 200:
        break
    names.add(name)

names_list = sorted(list(names))[:200]

# Write to txt
with open('/home/z/my-project/nombres-imagenes-seo.txt', 'w') as f:
    f.write("# NOMBRES DE IMAGENES SEO - LLANOCAR\n")
    f.write("# Total: 200 imagenes\n")
    f.write("# Formato: palabras-clave-separadas-por-guiones.jpg\n\n")
    for i, name in enumerate(names_list, 1):
        f.write(f"{i}. {name}\n")

# Also output the first 25 for image replacements
print("=== FIRST 25 NAMES FOR REPLACEMENT ===")
for i, name in enumerate(names_list[:25]):
    print(f"{i+1}. {name}")

print(f"\nTotal generated: {len(names_list)}")
print(f"\nAll names saved to: /home/z/my-project/nombres-imagenes-seo.txt")
