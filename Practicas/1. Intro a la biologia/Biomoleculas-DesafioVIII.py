# DESAFÍO VIII: Representación Logo de un conjunto de secuencias proteicas
#
# Un Logo muestra en cada posición qué aminoácidos aparecen y con qué frecuencia.
# Cuanto más grande la letra, más conservada está esa posición entre las secuencias.
#
# Requiere: pip install logomaker matplotlib pandas

import pandas as pd
import logomaker
import matplotlib.pyplot as plt

secuencias = [
    'MLPGLALLLLAAWTMRALEVPTDGNAPLLVEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRAQCKTHPHFVIPYRCLVGEFVSDALLAPDKCKFLHQERMDVCETHLHWHTV',
    'MLPGLALLLLAAWTARALEVPTDGNAGLLAEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRKQCKTHPHFVIPYRCLVGEFVSDALLVPDKCKFLHQERMDVCETHLHWHTV',
    'MLPGLALLLLAAWTARALEVPTDGNAGLLAEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRKQCKTHPHFVIPYRCLVGEFVSDALLVPDKCKFLHQERMDVCETHLHWHTV',
]

# Paso 1: contar frecuencias de cada aminoácido en cada posición
longitud = len(secuencias[0])
aminoacidos = sorted(set(''.join(secuencias)))

conteos = pd.DataFrame(0, index=range(longitud), columns=aminoacidos)

for secuencia in secuencias:
    for posicion, aa in enumerate(secuencia):
        conteos.loc[posicion, aa] += 1

# Paso 2: convertir conteos a matriz de información (formato que usa logomaker)
matriz_logo = logomaker.transform_matrix(conteos, from_type='counts', to_type='information')

# Paso 3: graficar
fig, ax = plt.subplots(figsize=(30, 3))

logomaker.Logo(matriz_logo, ax=ax, color_scheme='chemistry')

ax.set_title('Logo de secuencias proteicas')
ax.set_xlabel('Posición')
ax.set_ylabel('Información (bits)')

plt.tight_layout()
plt.savefig('logo_proteico.png', dpi=150)
plt.show()

print("Logo guardado como logo_proteico.png")
