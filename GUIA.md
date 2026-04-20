# Guia Bioinformatica - UNQ

## Archivos descargados

### Apuntes teóricos (todos descargados ✓)

| Archivo | Tema |
|---------|------|
| `Apuntes/Teorias/BIOINFORMÁTICA_clase_introductoria.pdf` | Introducción a la Bioinformática |
| `Apuntes/Teorias/Introducción_Biología.pdf` | Intro a la biología |
| `Apuntes/Teorias/Biomoleculas.pdf` | Biomoléculas |
| `Apuntes/Teorias/Celulas_y_genetica.pdf` | Células y genética |
| `Apuntes/Teorias/Proteinas.pdf` | Proteínas |
| `Apuntes/Teorias/Algoritmos_de_Comparación_Secuencias.pdf` | Algoritmos de comparación de secuencias |
| `Apuntes/Teorias/Análisis Filogenéticos.pdf` | Análisis filogenéticos |
| `Apuntes/Teorias/Teoria_Estructura-proteinas_Gustavo_Parisi.pdf` | Estructura de proteínas (Parisi) |

### Teórico-Prácticos (todos descargados ✓)

| Carpeta | Contenido |
|---------|-----------|
| `Apuntes/1. Intro_a_la_Biologia/` | El juego de la vida, Biomoléculas (md + imágenes) |
| `Apuntes/2. Linux_Bash/` | Intro al CLI/Unix/Bash (md + archivos complementarios) |
| `Apuntes/3. Intro_Python/` | Programación orientada a la biología, intro CLI (md + pdf) |
| `Apuntes/4. Bioinformatica_Primeros_pasos/` | Alineamientos secuenciales, En qué se parece una mosca y una gallina (md + imágenes) |
| `Apuntes/5. Biopython/` | Alineamientos de a pares con Biopython (md + complementarios) |
| `Apuntes/6. Inferencias_evolutivas/` | Inferencias evolutivas, árboles filogenéticos (md + fasta) |
| `Apuntes/7. Bioinformatica_Estructural/` | La vida en tres dimensiones, Acoplamiento molecular (md + PyMol.pdf) |
| `Apuntes/8. Estadistica_con_pandas/` | Análisis de IRAs con Pandas, comparación de estructuras (ipynb + md) |

### Prácticas (todas descargadas ✓)

| Carpeta | Contenido |
|---------|-----------|
| `Practicas/1. Intro a la biologia/` | Desafíos V, VII, VIII de Biomoléculas en Python (.py) |
| `Practicas/Clase_de_Imagenes/` | 8 notebooks de actividades con imágenes (arrays, filtros, bordes, morfología, etc.) |
| `Practicas/Corrida_Inferencias/` | Archivos de una corrida IQ-TREE (fasta, treefile, logs) |

---

## Recorrido por unidad temática

### Unidad 1 — Introducción a la Biología y Biomoléculas

**Leer:**
1. `Apuntes/Teorias/Introducción_Biología.pdf`
2. `Apuntes/Teorias/Biomoleculas.pdf`
3. `Apuntes/Teorias/Celulas_y_genetica.pdf`
4. `Apuntes/1. Intro_a_la_Biologia/El_juego_de_la_vida.md` — células, ADN, transcripción, traducción
5. `Apuntes/1. Intro_a_la_Biologia/Biomoléculas.md` — aminoácidos, proteínas, código genético

**Conceptos clave:**
- Célula procariota vs eucariota
- Dogma central de la biología molecular (ADN → ARN → Proteína)
- Código genético, codones, aminoácidos
- Transcripción y traducción

**Práctica:**
- `Practicas/1. Intro a la biologia/` — scripts Python con desafíos de Biomoléculas

---

### Unidad 2 — Introducción a Python y Linux/Bash

**Leer:**
1. `Apuntes/2. Linux_Bash/Intro_Unix_bash.md` — CLI, comandos básicos, GREP, bash
2. `Apuntes/3. Intro_Python/Porgramacion_orientada_a_la_biologia.md`
3. `Apuntes/3. Intro_Python/Interfaz_por_liena_de_comando.md`
4. `Apuntes/3. Intro_Python/Guia_Taller_Programacion_Biologia_2019.pdf`
5. `Apuntes/Guia_Instalacion_Python.pdf`

**Conceptos clave:**
- Estructura general de comandos UNIX
- Navegación de archivos, permisos, GREP
- Programación orientada a la biología en Python

---

### Unidad 3 — Alineamientos y Búsqueda de Similitud Secuencial

**Leer:**
1. `Apuntes/Teorias/Algoritmos_de_Comparación_Secuencias.pdf`
2. `Apuntes/4. Bioinformatica_Primeros_pasos/En_que_se_parece_una_mosca_y_una_gallina.md` — homología, bases de datos (NCBI)
3. `Apuntes/4. Bioinformatica_Primeros_pasos/Alineamientos_secuenciales.md` — Needleman-Wunsch, Smith-Waterman, BLAST, matrices de sustitución

**Conceptos clave:**
- Secuencias homólogas, ortólogos y parálogos
- Alineamiento global (Needleman-Wunsch) vs local (Smith-Waterman)
- Matrices de sustitución (Dayhoff/PAM, BLOSUM)
- BLAST y búsqueda de similitud en bases de datos
- NCBI, UniProt, ClustalOmega

---

### Unidad 4 — Biopython

**Leer:**
1. `Apuntes/5. Biopython/alineamientos_de_a_Pares.md`
2. `Apuntes/5. Biopython/complementarios/Notas_alineamiento_de_a_pares.md`
3. `Apuntes/5. Biopython/complementarios/Práctico_Biopython_PDBs.md`

**Conceptos clave:**
- Instalación y uso de Biopython
- Alineamientos de a pares programáticos
- Lectura de estructuras PDB con Biopython

---

### Unidad 5 — Inferencias Evolutivas (Filogenética)

**Leer:**
1. `Apuntes/Teorias/Análisis Filogenéticos.pdf`
2. `Apuntes/6. Inferencias_evolutivas/inferencias_evolutivas.md` — distancias evolutivas, árboles filogenéticos, clustering, IQ-TREE

**Conceptos clave:**
- Distancias evolutivas entre especies
- Árboles filogenéticos: nodos internos, hojas, clados
- Algoritmos de clustering (NJ, ML)
- IQ-TREE para inferencia filogenética

**Práctica:**
- `Practicas/Corrida_Inferencias/` — corrida IQ-TREE con secuencias de Citocromo C

---

### Unidad 6 — Bioinformática Estructural

**Leer:**
1. `Apuntes/Teorias/Proteinas.pdf`
2. `Apuntes/Teorias/Teoria_Estructura-proteinas_Gustavo_Parisi.pdf`
3. `Apuntes/7. Bioinformatica_Estructural/La_vida_en_tres_dimensiones.md` — PDB, estructuras 3D, PyMol
4. `Apuntes/7. Bioinformatica_Estructural/Acoplamiento_molecular.md` — docking molecular
5. `Apuntes/7. Bioinformatica_Estructural/PyMol.pdf`

**Conceptos clave:**
- Estructura primaria, secundaria, terciaria y cuaternaria de proteínas
- Banco de Datos de Proteínas (PDB): formato, búsqueda, descarga
- Visualización 3D con PyMol
- Acoplamiento molecular (docking ligando-proteína)

---

### Unidad 7 — Estadística con Pandas

**Leer:**
1. `Apuntes/8. Estadistica_con_pandas/libro_estadistica.pdf`
2. `Apuntes/8. Estadistica_con_pandas/Análisis_de_IRAS_con_PANDAS/IRAS_analisis_de_datos_biomédicos.md`

**Notebooks:**
- `Apuntes/8. Estadistica_con_pandas/Análisis_de_IRAS_con_PANDAS/Bioinfo_Estadistica_IRAS.ipynb` — análisis de datos de infecciones respiratorias
- `Apuntes/8. Estadistica_con_pandas/Comparación_de_estructuras_con_Pandas/PANDAS_usos_y_desusos_UNQ.ipynb` — comparación de estructuras proteicas

**Conceptos clave:**
- DataFrames, filtrado, agrupación con Pandas
- Estadística descriptiva aplicada a datos biomédicos
- RMSD para comparación de estructuras

---

### Unidad 8 — Procesamiento de Imágenes Biológicas

**Notebooks (en orden):**
1. `Practicas/Clase_de_Imagenes/Imagenes1_arrays_2021.ipynb` — imágenes como arrays NumPy
2. `Practicas/Clase_de_Imagenes/Imagenes2_bibliotecas.ipynb` — bibliotecas (PIL, skimage, matplotlib)
3. `Practicas/Clase_de_Imagenes/Imagenes3_Resolución.ipynb` — resolución, escalado
4. `Practicas/Clase_de_Imagenes/Imagenes4_Operaciones.ipynb` — operaciones sobre imágenes
5. `Practicas/Clase_de_Imagenes/Imagenes5_Filtros.ipynb` — filtros (gaussiano, mediana, etc.)
6. `Practicas/Clase_de_Imagenes/Imagenes6_Bordes.ipynb` — detección de bordes
7. `Practicas/Clase_de_Imagenes/Imagenes7_Binarizacion.ipynb` — umbralización y binarización
8. `Practicas/Clase_de_Imagenes/Imagenes8_Morfologia.ipynb` — morfología matemática
9. `Practicas/Clase_de_Imagenes/Actividad.ipynb` — actividad integradora

---

## Recursos permanentes

| Recurso | URL |
|---------|-----|
| NCBI (bases de datos biológicas) | https://www.ncbi.nlm.nih.gov/ |
| Protein Data Bank (PDB) | https://www.rcsb.org/ |
| UniProt (base de datos de proteínas) | https://www.uniprot.org/ |
| ClustalOmega (alineamientos múltiples) | https://www.ebi.ac.uk/Tools/msa/clustalo/ |
| Biopython docs | https://biopython.org/wiki/Documentation |
| IQ-TREE (inferencia filogenética) | http://www.iqtree.org/ |

---

## Estructura de carpetas

```
bioinformatica-unq/
├── Apuntes/
│   ├── Teorias/                              ← PDFs de slides teóricos
│   ├── 1. Intro_a_la_Biologia/               ← notas md (células, biomoléculas, código genético)
│   ├── 2. Linux_Bash/                        ← notas md + archivos complementarios
│   ├── 3. Intro_Python/                      ← notas md + pdf de programación en biología
│   ├── 4. Bioinformatica_Primeros_pasos/     ← notas md (homología, BLAST, NCBI, alineamientos)
│   ├── 5. Biopython/                         ← notas md + scripts Python
│   ├── 6. Inferencias_evolutivas/            ← notas md + fasta de Citocromo C
│   ├── 7. Bioinformatica_Estructural/        ← notas md (PDB, PyMol, docking)
│   ├── 8. Estadistica_con_pandas/            ← ipynb + md + datos (IRAs, estructuras)
│   └── Guia_Instalacion_Python.pdf
├── Practicas/
│   ├── 1. Intro a la biologia/         ← scripts .py desafíos de Biomoléculas
│   ├── Clase_de_Imagenes/              ← 8 notebooks de procesamiento de imágenes
│   └── Corrida_Inferencias/            ← output de IQ-TREE (fasta, treefile, logs)
└── Introduccion_a_la_Bioinformatica/   ← repo original del curso (NO MODIFICAR)
```
