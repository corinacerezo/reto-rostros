# Reto: detección de rostros

Te damos una "caja negra" que recibe una imagen y te regresa las coordenadas de los rostros que encontró. Lo que hagas después con esas coordenadas es tu reto.

## Setup (una vez)

```bash
pip install -r requirements.txt
```

## Probarlo

```bash
python3 detector.py imagen-ejemplo.png
```

Vas a ver algo así:

```
Rostros detectados: 4
  Rostrosss 1: x=661, y=237, w=64, h=74, confianza=0.91
  Rostrosss 2: x=590, y=345, w=66, h=97, confianza=0.91
  Rostrosss 3: x=526, y=93, w=49, h=73, confianza=0.90
  Rostrosss 4: x=201, y=289, w=99, h=161, confianza=0.86
```

Formatos soportados: JPG, PNG, WebP, BMP.

## Usarlo en tu código

```python
from detector import detectar_rostros

rostros = detectar_rostros("mi_foto.jpg")
for x, y, w, h, confianza in rostros:
    # haz algo con cada rostro
    ...
```

`x, y` es la esquina superior izquierda del rostro. `w, h` es su ancho y alto.

## ¿En otro lenguaje?

Si prefieres usar otro lenguaje, el modelo es un detector de rostros open source. Cualquier runtime que soporte ONNX puede cargarlo.
