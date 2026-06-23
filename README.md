# Reto: detección de rostros

Te damos una "caja negra" que recibe una imagen y te regresa las coordenadas de los rostros que encontró y un score de confianza. Lo que hagas después con esas coordenadas es tu reto.

## Requisito previo: Python 3

Verifica que tienes Python 3 instalado:

```bash
python3 --version
```

Si no lo tienes, instálalo desde la página oficial:

https://www.python.org/downloads/

Después abre una nueva terminal y vuelve a verificar con el comando anterior.

## Setup (una vez)

```bash
python3 -m pip install -r requirements.txt
```

## Probarlo

```bash
python3 detector.py image-example.jpg
```

Vas a ver algo así:

```
Rostros detectados: 3
  Rostro 1: x=593, y=1177, w=441, h=580, confianza=0.88
  Rostro 2: x=2877, y=1699, w=374, h=534, confianza=0.86
  Rostro 3: x=1864, y=1909, w=482, h=570, confianza=0.77
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
