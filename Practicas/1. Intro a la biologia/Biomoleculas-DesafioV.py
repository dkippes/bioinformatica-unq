# DESAFÍO V: Predicción de estructura secundaria por residuo
#
# Input:  una secuencia de aminoácidos en código de una letra (string)
#         Ej: "ACDEFGHIKLMNPQRSTVWY"
#
# Output: una cadena del mismo largo donde cada posición indica la
#         estructura predicha para ese residuo:
#           H = alfa-hélice
#           B = hoja beta plegada
#           L = bucle (loop)
#
# Método: tabla de propensidades de Chou-Fasman.
#         Cada aminoácido tiene una "preferencia" conocida por cada
#         estructura. Se elige la de mayor valor para cada residuo.

# Tabla de propensidades (valores de Chou-Fasman)
# Fuente: Chou & Fasman, 1978
# Formato: aminoácido -> (P_helix, P_sheet, P_loop)
PROPENSIDADES = {
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

def predecir_estructura(secuencia):
    secuencia = secuencia.upper().strip()
    resultado = []

    for aminoacido in secuencia:
        if aminoacido not in PROPENSIDADES:
            resultado.append('?')  # aminoácido desconocido
            continue

        p_helice, p_hoja, p_bucle = PROPENSIDADES[aminoacido]

        if p_helice >= p_hoja and p_helice >= p_bucle:
            resultado.append('H')
        elif p_hoja >= p_helice and p_hoja >= p_bucle:
            resultado.append('B')
        else:
            resultado.append('L')

    return ''.join(resultado)


# --- Programa principal ---
secuencia = input("Ingresá la secuencia de aminoácidos (código de 1 letra): ")

prediccion = predecir_estructura(secuencia)

print("\nSecuencia: ", secuencia.upper())
print("Predicción:", prediccion)
print()
print("Referencia: H = hélice | B = hoja beta | L = loop")
