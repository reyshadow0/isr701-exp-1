# EXP-1 — TCP, UDP y WebSockets

Aplicaciones Distribuidas (ISR-701) · Universidad Técnica Estatal de Quevedo · SPA 2026–2027 · Grupo BCM

**Integrantes:** Bueno Troya Erwin Daniel, Castro Coello Mario Sebastián, Macías Vásquez César Abrahan

**Exposición:** lunes 23 de noviembre de 2026

**Video del ensayo completo:** _pendiente: enlace al video (máximo 12 minutos, con el rostro y la voz de los tres)_

## Contenido del repositorio

| Ruta | Descripción |
|---|---|
| `diapositivas.tex` | Archivo principal de las diapositivas (Beamer) |
| `notas.tex` | Archivo principal de las notas de la presentación |
| `contenido/diapositivas/` | Una diapositiva o grupo de diapositivas por parte; cada integrante edita las suyas |
| `contenido/notas/` | El guion de cada parte y las preguntas previstas |
| `partes.tex` | Reparto: orden de las partes, quién expone y cuánto dura cada una |
| `datos.tex` | Título, grupo, repositorio y fecha |
| `beamerthemebcm.sty`, `bcm-comun.sty` | Tema visual del grupo y macros comunes |
| `referencias.bib` | Referencias (BibLaTeX, estilo IEEE) |
| `figuras/` | Figuras exportadas que usan los documentos |
| `diagramas/` | Fuentes editables de draw.io (`.drawio`) |
| `evidencias/` | Foto del esquema inicial y capturas de artículos anotados |
| `ejemplo/` | Código del ejemplo sencillo |
| `BITACORA.md` | Bitácora del grupo |
| `diapositivas.pdf`, `notas.pdf` | Documentos compilados |

## Compilación

- **Compilador:** `pdflatex`
- **Bibliografía:** `biber` (paquete `biblatex` con estilo `ieee`)
- **Archivos principales:** `diapositivas.tex` y `notas.tex`
- **Distribución usada:** MiKTeX en Windows

Orden de comandos, ejecutados desde la raíz del repositorio:

```bash
pdflatex diapositivas.tex
biber diapositivas
pdflatex diapositivas.tex
pdflatex diapositivas.tex
```

```bash
pdflatex notas.tex
biber notas
pdflatex notas.tex
pdflatex notas.tex
```

El resultado es `diapositivas.pdf` y `notas.pdf`.

### Dependencias

Paquetes de LaTeX: `beamer`, `fontenc`, `inputenc`, `babel` (idioma `spanish`), `sourcesanspro`,
`sourcecodepro`, `csquotes`, `booktabs`, `tabularx`, `listings`, `tikz`, `tcolorbox`, `geometry`,
`microtype`, `graphicx`, `float`, `biblatex` con `biblatex-ieee`, y `hyperref`. Además se necesita el
programa `biber`. MiKTeX instala automáticamente los paquetes que falten; en TeX Live vienen incluidos
en el esquema completo (`scheme-full`).

## Cómo se trabaja

- Cada integrante edita solo los archivos de sus partes (`partes.tex` dice quién expone cada una) y hace
  sus propios commits, el mismo día en que avanza.
- Lo que falta aparece en los PDF como un recuadro ámbar «Pendiente». Antes de entregar no debe quedar
  ninguno: `git grep -n "pend"` en `contenido/` tiene que salir vacío.
- Cada diagrama se hace en draw.io: el `.drawio` va en `diagramas/` y su exportación en PDF o PNG en
  `figuras/`.
- Las referencias se obtienen de doi.org con el script de la materia, nunca a mano (ver el comentario
  al inicio de `referencias.bib`).

## Ejemplo sencillo

El ejemplo UDP se encuentra en `ejemplo/udp_demo.py`. Las instrucciones de ejecución están en `ejemplo/README.md`.
