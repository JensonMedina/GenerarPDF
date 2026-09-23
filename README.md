# GenerarPDF

Proyecto base en Python para generar archivos PDF de forma rápida y reutilizable.

La idea es mantener preparado un entorno donde puedas pedirle a ChatGPT, Codex u otra IA que genere el código de un documento PDF, pegar ese código dentro del proyecto y ejecutarlo sin tener que volver a configurar Python o las dependencias desde cero.

## Estructura del proyecto

```text
GenerarPDF/
├── assets/
│   ├── images/
│   └── fonts/
├── output/
├── src/
│   ├── __init__.py
│   └── pdf_generator.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

### `src/`

Acá deben ir los archivos Python que contienen la lógica para generar cada tipo de PDF.

Por ejemplo:

```text
src/
├── __init__.py
├── pdf_generator.py
├── factura.py
├── informe.py
├── certificado.py
└── presupuesto.py
```

No es necesario poner todo el código dentro de `main.py`.

Lo recomendable es que cada documento tenga su propio archivo.

Ejemplo:

```text
src/factura.py
```

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def generar_factura(ruta_salida: str):
    pdf = canvas.Canvas(ruta_salida, pagesize=A4)

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(50, 800, "Factura")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 770, "Factura generada con Python y ReportLab.")

    pdf.save()
```

Luego se llama desde `main.py`:

```python
from src.factura import generar_factura


def main():
    generar_factura("output/factura.pdf")
    print("PDF generado correctamente")


if __name__ == "__main__":
    main()
```

## `main.py`

`main.py` es el punto de entrada de la aplicación.

Su función principal es decidir qué generador ejecutar.

Conviene mantenerlo pequeño.

Por ejemplo:

```python
from src.pdf_generator import generar_pdf


def main():
    generar_pdf("output/documento.pdf")


if __name__ == "__main__":
    main()
```

Si en el futuro querés generar otro tipo de documento, podés cambiar el import:

```python
from src.informe import generar_informe
```

y llamar:

```python
generar_informe("output/informe.pdf")
```

## `assets/`

Esta carpeta contiene recursos utilizados por los PDFs.

Por ejemplo:

```text
assets/
├── images/
│   ├── logo.png
│   └── firma.png
└── fonts/
    └── MiFuente.ttf
```

Esto permite usar imágenes, logos o fuentes personalizadas sin mezclarlas con el código.

## `output/`

Todos los PDFs generados deberían guardarse en esta carpeta.

Ejemplo:

```text
output/
├── factura.pdf
├── informe.pdf
└── certificado.pdf
```

De esta manera los archivos generados quedan separados del código fuente.

## Preparar el proyecto

### 1. Crear el entorno virtual

Desde la raíz del repositorio:

```bash
python3 -m venv .venv
```

### 2. Activar el entorno virtual

En Linux:

```bash
source .venv/bin/activate
```

Cuando esté activo debería aparecer algo similar a:

```text
(.venv) usuario@pc:~/Repos/GenerarPDF$
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

Si todavía no existe `requirements.txt`, instalar ReportLab:

```bash
pip install reportlab
```

y luego generarlo con:

```bash
pip freeze > requirements.txt
```

## Ejecutar el proyecto

Con el entorno virtual activo:

```bash
python main.py
```

El archivo generado debería aparecer dentro de:

```text
output/
```

## Agregar un nuevo generador de PDF

Supongamos que querés crear un presupuesto.

Primero creás:

```text
src/presupuesto.py
```

Dentro colocás una función:

```python
def generar_presupuesto(ruta_salida: str):
    # Código de generación del PDF
    pass
```

Luego, en `main.py`:

```python
from src.presupuesto import generar_presupuesto


def main():
    generar_presupuesto("output/presupuesto.pdf")


if __name__ == "__main__":
    main()
```

Finalmente:

```bash
python main.py
```

## Ejemplo de prompt para una IA

Podés copiar y adaptar este prompt cada vez que quieras generar un documento nuevo:

> Tengo un proyecto Python preparado para generar PDFs usando ReportLab.
>
> La estructura es:
>
> ```text
> GenerarPDF/
> ├── assets/
> │   ├── images/
> │   └── fonts/
> ├── output/
> ├── src/
> ├── main.py
> └── requirements.txt
> ```
>
> Quiero crear un nuevo generador de PDF.
>
> Creá un archivo `src/informe.py` que genere un documento A4 usando ReportLab.
>
> El PDF debe guardarse en `output/informe.pdf`.
>
> Necesito que el documento tenga:
>
> - título principal;
> - fecha;
> - varios párrafos;
> - una tabla;
> - encabezado;
> - pie de página con número de página;
> - márgenes adecuados.
>
> Creá una función:
>
> ```python
> generar_informe(ruta_salida: str)
> ```
>
> También indicame exactamente qué código debo poner en `main.py` para ejecutarlo.
>
> Si necesitás instalar alguna dependencia adicional, indicámela y explicá qué debo agregar a `requirements.txt`.
>
> No modifiques innecesariamente la estructura existente del proyecto.

## Ejemplo de prompt más específico

También podés darle a la IA directamente el contenido que querés transformar:

> Usando mi proyecto Python con ReportLab, creá `src/resumen_fisica.py`.
>
> Quiero generar un PDF A4 llamado `output/resumen_fisica.pdf`.
>
> El documento debe contener un resumen de movimiento parabólico.
>
> Usá títulos, subtítulos, fórmulas, cuadros destacados y una tabla de fórmulas.
>
> El código debe quedar encapsulado en:
>
> ```python
> generar_resumen_fisica(ruta_salida: str)
> ```
>
> Dame también el cambio necesario en `main.py`.

## Otro ejemplo de prompt

> Tengo un proyecto Python con ReportLab.
> main.py llama a generar_pdf() y los PDFs se guardan en output/.
> Creame un archivo src/factura.py que genere una factura A4.

## Recomendaciones

- Crear un archivo diferente dentro de `src/` para cada tipo de documento.
- Evitar colocar toda la lógica de generación dentro de `main.py`.
- Guardar siempre los PDFs generados en `output/`.
- Guardar imágenes y logos dentro de `assets/images/`.
- Guardar fuentes personalizadas dentro de `assets/fonts/`.
- Mantener `.venv/` fuera del repositorio.
- Actualizar `requirements.txt` cuando se agreguen nuevas dependencias.

## `.gitignore` recomendado

```gitignore
.venv/
__pycache__/
*.pyc

output/*.pdf
```

## Flujo de trabajo habitual

```text
1. Pedir a una IA el código del nuevo PDF
        ↓
2. Crear el archivo correspondiente dentro de src/
        ↓
3. Pegar el código generado
        ↓
4. Importar la función desde main.py
        ↓
5. Ejecutar python main.py
        ↓
6. Revisar el PDF generado en output/
```

La intención de este repositorio es funcionar como una plantilla reutilizable para experimentar y generar documentos PDF mediante Python sin tener que preparar nuevamente el entorno en cada ocasión.
