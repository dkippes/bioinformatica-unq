# Desafío VII: buscar el motivo de N-glicosilación en proteínas de UniProt
#
# El motivo es: N{P}[ST]{P}
# En regex: N[^P][ST][^P]
# Significa: N, cualquier aa excepto P, S o T, cualquier aa excepto P
#
# Cómo ejecutar:
#   python Biomoleculas-DesafioVII.py
#   Luego ingresá los IDs de UniProt de a uno, ej: B5ZC00
#   Enter vacío para terminar

import urllib.request
import re

def obtener_secuencia(uniprot_id):
    url = f"https://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    with urllib.request.urlopen(url) as respuesta:
        contenido = respuesta.read().decode('utf-8')
    lineas = contenido.strip().split('\n')
    return ''.join(lineas[1:])  # saco el encabezado FASTA

def buscar_motivo(secuencia):
    motivo = re.compile(r'(?=(N[^P][ST][^P]))')
    return [m.start() + 1 for m in motivo.finditer(secuencia)]  # posiciones base 1


print("Ingresá los IDs de UniProt (Enter vacío para terminar):")

ids = []
while len(ids) < 15:
    id_ingresado = input("> ").strip()
    if id_ingresado == '':
        break
    ids.append(id_ingresado)

for uniprot_id in ids:
    secuencia = obtener_secuencia(uniprot_id)
    posiciones = buscar_motivo(secuencia)
    if posiciones:
        print(uniprot_id)
        print(' '.join(str(p) for p in posiciones))
