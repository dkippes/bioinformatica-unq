# ¿En qué se parecen una gallina y una mosca?

**Tabla:**

| Secuencia	|Nombre taxonómico | Nombre común | 
|-------------	|----------	|-------------	|
| NP_061820.1 | Homo sapiens | Humano | 
| NP_001072946.1 | Gallus gallus | Gallina |
| NP_001065289.1 | Pan troglodytes | Chimpancé |
| NP_001157486.1 | Equus caballus | Caballo |
| NP_001183974.1 | Canis lupus familiaris | Perro |
| AEP27192.1 | Gorilla gorilla | Gorila |
| XP_024245566.1 | Oncorhynchus tshawytscha | Salmón |
| NP_001086101.1 | Xenopus laevis | Rana africana |
| NP_477164.1 | Drosophila melanogaster | Mosca de la fruta |

**PARA PENSAR:** ¿Cuán sencillo será alinear dos o más secuencias a mano? ¿Cuánto influirán el número de secuencias a alinear, su longitud, y la similitud entre ellas?

Respuesta: Alinear secuencias a mano es muy difícil incluso con pocas secuencias cortas. A medida que aumenta el número de secuencias, su longitud o su divergencia, la tarea se vuelve exponencialmente más compleja: hay que evaluar todas las combinaciones posibles de insertar gaps para maximizar las coincidencias.

**PARA PENSAR:**¿Son parecidos los citocromos c de humano y gallo? 

Respuesta: Sí, son muy parecidos. Ambas secuencias tienen 104 aminoácidos y difieren en apenas unos pocos residuos, lo que representa una identidad bastante cercana. Esto indica que el citocromo c es una proteína muy conservada a lo largo de la evolución.

**PARA PENSAR:**¿Qué teorías subyacen a este análisis?

Respuesta: Subyace la teoría de la evolución por selección natural (Darwin) y el concepto de ancestro común. Si organismos distintos comparten secuencias similares, es porque descienden de un ancestro común que ya poseía esa proteína. Cuanto más parecidas sean las secuencias, más cercano es el parentesco evolutivo.

**PARA PENSAR:**¿Cómo nos ayuda la evolución a explicar sus similitudes y diferencias?

Respuesta:** Las similitudes se explican por el origen común: todas estas especies comparten un ancestro que ya tenía citocromo c, y como la proteína cumple una función vital en la respiración aeróbica, las mutaciones que la alteran suelen ser letales y son eliminadas por selección natural. Las diferencias, en cambio, son mutaciones neutras o ligeramente beneficiosas que se fueron fijando a lo largo del tiempo de forma independiente en cada linaje. Cuanto más tiempo lleven separadas dos especies, más diferencias acumulan.

**PARA PENSAR:**¿Qué indican los colores?

Respuesta: Los colores en Clustal Omega agrupan los aminoácidos según sus propiedades fisicoquímicas. Por ejemplo, los residuos hidrofóbicos aparecen en rojo/naranja; los residuos polares o cargados positivamente en azul; los cargados negativamente en magenta, etc. Esto permite ver de un vistazo si en una posición se conserva la identidad exacta del aminoácido o al menos su tipo funcional.

**PARA PENSAR:**¿Qué indican el guión (-), los dos puntos (:) y el asterisco (*)?

Respuesta:
- `-`: indica un gap, es decir que en esa posición una secuencia no tiene aminoácido respecto a las otras. Se inserta para mantener el alineamiento cuando hay una inserción o deleción.
- `:`: los aminoácidos en esa posición son distintos pero con propiedades fisicoquímicas muy similares.
- `*`: todos los organismos tienen el mismo aminoácido en esa posición.

**PARA PENSAR:** A simple vista, ¿se conserva la secuencia del citocromo c en los organismos?

Respuesta: Sí, se conserva notablemente. La gran mayoría de las posiciones del alineamiento muestran asteriscos o dos puntos, lo que indica que el citocromo c es una proteína altamente conservada.

**PARA PENSAR:** ¿Creeríamos que todos los organismos se asemejan por igual al resto, o se pueden identificar grupos de mayor similitud? Si es así, ¿tienen sentido?

Respuesta: Se pueden identificar grupos de mayor similitud. Los mamíferos (humano, chimpancé, gorila, perro, caballo) son muy similares entre sí y difieren más del pollo, la rana, el salmón y especialmente de la mosca. Esto tiene sentido evolutivo: los organismos más emparentados llevan menos tiempo divergiendo desde su último ancestro común y, por lo tanto, acumularon menos diferencias.

**PARA PENSAR:** ¿Qué evidencias nos aportaría este análisis, a la luz de la evolución?

Respuesta: Este análisis aporta evidencia molecular a favor de la evolución por descendencia con modificación. El grado de similitud entre las secuencias refleja el grado de parentesco entre los organismos: cuanto más parecido es el citocromo c de dos especies, más reciente es su ancestro común. Además, como el citocromo c está bajo fuerte presión de selección purificadora, las diferencias observadas representan la acumulación de mutaciones neutras a lo largo del tiempo, lo que lo convierte en un buen "reloj molecular" para estimar tiempos de divergencia.

**PREGUNTA:** A juzgar por los organismos participantes, ¿cuáles creería que deberían estar más agrupados en el árbol filogenético?

Respuesta: Esperaría que los primates (humano, chimpancé y gorila) formen un grupo muy cercano, seguidos por los demás mamíferos (perro y caballo). El pollo debería agruparse con los vertebrados no mamíferos (rana, salmón), y la mosca quedar más alejada de todos por ser el único invertebrado del grupo.

**PREGUNTA:** Observemos el árbol filogenético. ¿Concuerda con lo esperado? ¿De qué organismos son los citocromos c más parecidos? ¿Cómo se explica?

Respuesta: Sí, el árbol concuerda en gran medida con lo esperado. Los citocromos c más parecidos son los de humano, chimpancé y gorila, que forman un clado compacto. Esto se explica porque comparten el ancestro común más reciente y llevan el menor tiempo divergiendo. La mosca aparece como el organismo más distante, lo que refleja la gran separación evolutiva entre artrópodos y vertebrados.
