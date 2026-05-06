# Guía: Cómo se expresa un gen (de ADN a proteína)

---

## Paso 1 — El ADN es el plano

El ADN es como un manual de instrucciones guardado en el núcleo de la célula.
Nunca sale del núcleo. Para usarlo, la célula hace una **copia** de la parte que necesita.

---

## Paso 2 — El promotor: la señal de "empezá acá"

Antes de cada gen hay una zona llamada **promotor**.
Es como el encabezado de una receta: le dice a la célula *dónde empieza ese gen*.

Dentro del promotor está la **caja TATA** (`TATAAA`).
Es una secuencia de 6 bases que funciona como marca de inicio.
Está ubicada unos 25-30 pasos antes del gen real.

> Si la caja TATA está mutada (cambiada), la célula no puede encontrar el inicio → el gen no se expresa.

---

## Paso 3 — TBP se engancha a la caja TATA

**TBP** = *TATA-Binding Protein* = proteína que reconoce y se pega a la caja TATA.

Pensala como una llave que encaja exactamente en esa cerradura (`TATAAA`).
Cuando TBP se pega, dobla el ADN unos 80°. Eso es la señal de que algo va a pasar acá.

---

## Paso 4 — Se arma el complejo de preiniciación

TBP no actúa solo. Llama a otros factores de transcripción (se llaman TFIID, TFIIB, TFIIH, etc.).
Juntos arman una plataforma encima del promotor.

> Pensalos como el equipo que prepara el set antes de que llegue el actor principal.

El actor principal es la **ARN Polimerasa II** (ARN Pol II).

---

## Paso 5 — ARN Polimerasa II empieza a transcribir

La ARN Pol II se sube a esa plataforma y empieza a recorrer el ADN.
A medida que avanza, va copiando la secuencia de ADN en una nueva molécula: el **ARN**.

Esta copia se llama **ARN pre-mensajero (pre-mRNA)**.
Es una copia en borrador, todavía no está lista para usarse.

---

## Paso 6 — Splicing: se sacan los intrones

El gen tiene dos tipos de fragmentos mezclados:

- **Exones** → partes que SÍ codifican proteína (las que importan)
- **Intrones** → partes que NO codifican nada (basura evolutiva, básicamente)

Una maquinaria llamada **spliceosoma** corta los intrones y pega los exones.
El resultado es el **mRNA maduro**: la copia limpia y lista.

> En el juego, las `i` debajo de ciertas bases indican intrones — posiciones que no forman parte del gen funcional.

---

## Paso 7 — El mRNA sale del núcleo

El mRNA maduro recibe dos "gorros" protectores (cap 5' y cola poli-A) y cruza la membrana nuclear.
Ahora está en el citoplasma, listo para ser leído.

---

## Paso 8 — Traducción: del mRNA a proteína

Los **ribosomas** leen el mRNA de a 3 bases por vez (cada grupo de 3 = **codón**).
Cada codón corresponde a un aminoácido.
Los aminoácidos se van encadenando hasta formar una **proteína funcional**.

---

## Resumen visual

```
ADN
 └─ promotor (TATAAA) ← TBP se pega acá
     └─ ARN Pol II transcribe
         └─ pre-mRNA (con intrones)
             └─ splicing → mRNA maduro
                 └─ traducción → PROTEÍNA
```

---

## Por qué el juego se enfoca en la caja TATA

La caja TATA es el **primer paso obligatorio**. Si TBP no la reconoce, todo lo demás no arranca.
Es el cuello de botella del proceso: mutada o bloqueada por un intrón → gen apagado.
Por eso el juego simula exactamente esa decisión.
