# Desafío V: predecir la estructura secundaria de una proteína
# Para cada aminoácido dice si forma hélice (H), hoja beta (B) o loop (L)

# Tabla de Chou-Fasman: cada aminoácido tiene preferencia por una estructura
# (hélice, hoja_beta, loop)
propensidades = {
    'A': (1.45, 0.97, 0.57),
    'R': (0.79, 0.90, 1.00),
    'N': (0.73, 0.65, 1.68),
    'D': (0.98, 0.80, 1.36),
    'C': (0.77, 1.30, 1.17),
    'E': (1.53, 0.26, 0.77),
    'Q': (1.17, 1.23, 0.80),
    'G': (0.53, 0.81, 1.68),
    'H': (1.00, 0.87, 0.95),
    'I': (1.00, 1.60, 0.58),
    'L': (1.34, 1.22, 0.57),
    'K': (1.07, 0.74, 1.01),
    'M': (1.20, 1.67, 0.67),
    'F': (1.12, 1.28, 0.71),
    'P': (0.59, 0.62, 1.79),
    'S': (0.79, 0.72, 1.56),
    'T': (0.82, 1.20, 1.06),
    'W': (1.14, 1.19, 0.96),
    'Y': (0.61, 1.29, 1.11),
    'V': (1.14, 1.65, 0.61),
}

secuencia = input("Ingresá la secuencia de aminoácidos: ").upper().strip()

prediccion = ""
for aa in secuencia:
    helice, hoja, loop = propensidades[aa]
    if helice >= hoja and helice >= loop:
        prediccion += "H"
    elif hoja >= helice and hoja >= loop:
        prediccion += "B"
    else:
        prediccion += "L"

print("Secuencia: ", secuencia)
print("Predicción:", prediccion)
print("H = hélice | B = hoja beta | L = loop")
