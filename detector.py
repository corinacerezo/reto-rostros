import cv2
import os
import sys

MODELO = "models/face_detection.onnx"


def detectar_rostros(ruta_imagen):
    """
    Recibe la ruta de una imagen y regresa una lista de tuplas
    (x, y, w, h, confianza) por cada rostro encontrado.
    """
    imagen = cv2.imread(ruta_imagen)
    if imagen is None:
        raise FileNotFoundError(f"No se pudo abrir la imagen: {ruta_imagen}")

    alto, ancho = imagen.shape[:2]
    detector = cv2.FaceDetectorYN.create(MODELO, "", (ancho, alto), score_threshold=0.5)
    _, rostros = detector.detect(imagen)

    if rostros is None:
        return []

    return [
        (int(r[0]), int(r[1]), int(r[2]), int(r[3]), float(r[-1]))
        for r in rostros
    ]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python detector.py <ruta_imagen>")
        sys.exit(1)

    rostros = detectar_rostros(sys.argv[1])
    print(f"Rostros detectados: {len(rostros)}")
    for i, (x, y, w, h, confianza) in enumerate(rostros, 1):
        print(f"  Rostro {i}: x={x}, y={y}, w={w}, h={h}, confianza={confianza:.2f}")
