# Guía para encarar el práctico — El juego de la vida

## Contexto teórico (lo que tenés que tener claro antes de codear)

**Dogma central de la biología molecular:**
```
ADN → (transcripción) → ARNm → (traducción) → Proteína
```

- La transcripción ocurre en el **núcleo**: una hebra de ADN sirve de molde para sintetizar ARNm.
- La traducción ocurre en el **citoplasma**: el ARNm es leído en tripletes (codones) para ensamblar aminoácidos.
- El **código genético** tiene 64 codones: 61 codifican aminoácidos, 3 son codones de STOP.
- En eucariotas el ADN tiene **intrones** (no codificantes) y **exones** (codificantes).
- La **caja TATA** (`TATAAA`) es una secuencia promotora que señala dónde empieza la transcripción.

---

## Desafíos del práctico

### Desafío I — Diferencias procariota vs eucariota (conceptual, sin código)
Enumerar las diferencias estructurales y genéticas entre ambos tipos celulares.

**Lo esencial:**
| | Procariota | Eucariota |
|---|---|---|
| Núcleo | No (ADN libre en citoplasma) | Sí (membrana nuclear) |
| Organelas | No | Sí (mitocondria, RE, etc.) |
| Intrones | No | Sí |
| Tamaño | ~1–10 µm | ~10–100 µm |
| Ejemplo | Bacteria, Archaea | Plantas, animales, hongos |

---

### Desafío II — Script: secuencia proteica → ARN codificante

**Qué hace:** dada una secuencia de aminoácidos, devolver una posible cadena de ARNm que la codifique.

**Clave:** el código genético es **degenerado** (un aminoácido puede tener varios codones). Podés elegir uno cualquiera por aminoácido.

**Esquema del script:**
```python
# Diccionario aminoácido → codón (elegir uno representativo)
codon_table = {
    'A': 'GCU', 'T': 'ACU', 'V': 'GUU', 'E': 'GAA',
    'K': 'AAA', 'G': 'GGU', 'H': 'CAU', 'F': 'UUU',
    'I': 'AUU', 'Q': 'CAA', 'C': 'UGU', 'S': 'UCU',
    'L': 'CUU', 'M': 'AUG', 'N': 'AAU', 'P': 'CCU',
    'R': 'CGU', 'W': 'UGG', 'Y': 'UAU', 'D': 'GAU',
    # completar todos los aminoácidos
}

# Input: secuencia proteica (argparse o sys.argv)
# Output: concatenar codones y agregar codón de inicio (AUG) y STOP (UAA)
```

**Peptido de ejemplo:** `ATVEKGGKHKTGPNEKGKKIFVQKCSQCHTVLHGLFGRKTGQA`

**Cómo ejecutar:** `python solucion.py ATVEKGG...`

---

### Desafío III — Script: identificar regiones promotoras en ADN

**Qué hace:** dado un archivo con una secuencia de ADN, encontrar todas las regiones que empiezan y terminan con `TATAAA`.

**Esquema del script:**
```python
import re, argparse

# Leer el archivo de ADN
# Buscar con regex todas las ocurrencias de TATAAA...TATAAA
patron = r'TATAAA.*?TATAAA'
# re.findall(patron, secuencia, re.DOTALL) o re.IGNORECASE si hace falta
# Imprimir posición y secuencia encontrada
```

**Consideraciones:**
- La secuencia puede venir en varias líneas → limpiar saltos de línea antes de buscar.
- Usar `re.DOTALL` si la región promotora puede abarcar múltiples líneas.
- Reportar posición de inicio y fin de cada región encontrada.

---

### Desafío IV — Juego RPG interactivo sobre expresión génica (CLI)

**Qué hace:** un juego por consola donde el jugador "atraviesa" el proceso de expresión génica (transcripción y traducción) tomando decisiones o respondiendo preguntas.

**Ideas para la narrativa:**
- El jugador es una molécula de ARN Polimerasa que debe transcribir un gen.
- Hay "enemigos" (intrones, mutaciones) que hay que evitar o cortar.
- La traducción es la segunda fase: el jugador guía el ribosoma codón a codón.

**Estructura mínima sugerida:**
```
main.py
├── argparse: --nombre_jugador, --dificultad
├── fase_transcripcion(): muestra ADN, pide al jugador identificar la caja TATA
├── fase_traduccion(): va mostrando codones y pide el aminoácido correspondiente
└── puntaje final
```

**Tecnología:** solo stdlib de Python (no hace falta nada externo). Usar `input()`, `print()` con colores via `\033[...m` si querés darle estética.

---

## Orden de ataque sugerido

1. **Desafío I** → solo texto/markdown, 10 min.
2. **Desafío III** → el más mecánico, regex sobre string. Empezar por acá para calentar.
3. **Desafío II** → armar el diccionario de codones y la lógica de mapeo.
4. **Desafío IV** → el más creativo, dejar para el final con más tiempo.

---

## Estructura de archivos sugerida

```
Juego_de_la_Vida_kippes/
├── GUIA.md              ← este archivo
├── desafio1.md          ← respuesta conceptual
├── desafio2.py          ← proteína → ARN
├── desafio3.py          ← buscar promotores
├── desafio4/
│   ├── main.py          ← juego RPG
│   └── game_logic.py
└── data/
    └── secuencia.fasta  ← archivo de ADN de prueba para desafío 3
```
