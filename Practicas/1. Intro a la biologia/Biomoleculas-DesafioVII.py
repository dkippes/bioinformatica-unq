# DESAFÍO VII: Buscar el motivo de N-glicosilación en proteínas de UniProt
#
# Motivo de N-glicosilación: N{P}[ST]{P}
#   N      -> asparagina
#   {P}    -> cualquier aminoácido excepto prolina
#   [ST]   -> serina o treonina
#   {P}    -> cualquier aminoácido excepto prolina
#
# En regex: N[^P][ST][^P]
#
# Input:  hasta 15 identificadores de UniProt (uno por línea, línea vacía para terminar)
# Output: para cada proteína con el motivo, su ID y las posiciones donde aparece

import urllib.request
import re

MOTIVO = re.compile(r'(?=(N[^P][ST][^P]))')  # lookahead para encontrar solapados

def obtener_secuencia(uniprot_id):
    url = f"https://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    try:
        with urllib.request.urlopen(url) as respuesta:
            contenido = respuesta.read().decode('utf-8')
        # El formato FASTA tiene una línea de encabezado y luego la secuencia
        lineas = contenido.strip().split('\n')
        secuencia = ''.join(lineas[1:])  # junta todo menos el encabezado
        return secuencia
    except Exception:
        print(f"  No se pudo obtener la secuencia para {uniprot_id}")
        return None

def buscar_motivo(secuencia):
    # Las posiciones en biología arrancan en 1, no en 0
    posiciones = [m.start() + 1 for m in MOTIVO.finditer(secuencia)]
    return posiciones


# --- Programa principal ---
print("Ingresá los identificadores de UniProt (uno por línea, Enter vacío para terminar):")

ids = []
while len(ids) < 15:
    id_ingresado = input("> ").strip()
    if id_ingresado == '':
        break
    ids.append(id_ingresado)

print()
for uniprot_id in ids:
    secuencia = obtener_secuencia(uniprot_id)
    if secuencia is None:
        continue

    posiciones = buscar_motivo(secuencia)
    if posiciones:
        print(uniprot_id)
        print(' '.join(str(p) for p in posiciones))
