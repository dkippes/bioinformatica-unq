# Desafío VIII: representación Logo de un conjunto de secuencias proteicas
# Requiere: pip install logomaker matplotlib pandas
#
# Cómo ejecutar:
#   python Biomoleculas-DesafioVIII.py
#   Genera el gráfico en pantalla y guarda logo_proteico.png en la misma carpeta

import pandas as pd
import logomaker
import matplotlib.pyplot as plt

secuencias = [
    'MLPGLALLLLAAWTMRALEVPTDGNAPLLVEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRAQCKTHPHFVIPYRCLVGEFVSDALLAPDKCKFLHQERMDVCETHLHWHTV',
    'MLPGLALLLLAAWTARALEVPTDGNAGLLAEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRKQCKTHPHFVIPYRCLVGEFVSDALLVPDKCKFLHQERMDVCETHLHWHTV',
    'MLPGLALLLLAAWTARALEVPTDGNAGLLAEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRKQCKTHPHFVIPYRCLVGEFVSDALLVPDKCKFLHQERMDVCETHLHWHTV',
]

longitud = len(secuencias[0])
aminoacidos = sorted(set(''.join(secuencias)))

# Contar cuántas veces aparece cada aminoácido en cada posición
conteos = pd.DataFrame(0, index=range(longitud), columns=aminoacidos)
for secuencia in secuencias:
    for posicion, aa in enumerate(secuencia):
        conteos.loc[posicion, aa] += 1

# Convertir a matriz de información y graficar
matriz_logo = logomaker.transform_matrix(conteos, from_type='counts', to_type='information')

fig, ax = plt.subplots(figsize=(30, 3))
logomaker.Logo(matriz_logo, ax=ax, color_scheme='chemistry')
ax.set_title('Logo de secuencias proteicas')
ax.set_xlabel('Posición')
ax.set_ylabel('Información (bits)')

plt.tight_layout()
plt.savefig('logo_proteico.png', dpi=150)
plt.show()
