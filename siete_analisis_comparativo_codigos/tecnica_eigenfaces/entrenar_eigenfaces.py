import cv2 as cv
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "DATASET"

PERSONA = "SEBASTIAN"

DATASET_FOLDERS = [
    "SEBASTIAN_NO_LUZ",
    "SEBASTIAN_LUZ",
    "SEBASTIAN_LUZ_NATURAL",
]

MODEL_PATH = Path(__file__).resolve().parent / "SebastianEigenface.xml"

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp"}

# Una sola identidad: las tres condiciones comparten
# la misma etiqueta numerica.
PERSON_LABEL = 0

faces_data = []
labels = []
image_size = None

for folder_name in DATASET_FOLDERS:
    folder_path = DATASET_DIR / folder_name

    if not folder_path.is_dir():
        raise FileNotFoundError(
            f"No se encontro el dataset: {folder_path}"
        )

    folder_count = 0

    for img_path in sorted(folder_path.iterdir()):
        if img_path.suffix.lower() not in IMAGE_EXTENSIONS:
            continue

        img = cv.imread(str(img_path), cv.IMREAD_GRAYSCALE)

        if img is None:
            print(f"Imagen ignorada: {img_path.name}")
            continue

        if image_size is None:
            image_size = img.shape

        if img.shape != image_size:
            raise ValueError(
                f"Tamano diferente en {img_path}.\n"
                f"Esperado: {image_size}; recibido: {img.shape}"
            )

        faces_data.append(img)
        labels.append(PERSON_LABEL)
        folder_count += 1

    print(f"{folder_name}: {folder_count} imagenes validas")

if len(faces_data) < 2:
    raise RuntimeError(
        "Se necesitan al menos dos imagenes para entrenar."
    )

labels_array = np.array(labels, dtype=np.int32)

print(f"\nPersona: {PERSONA}")
print(f"Total de imagenes: {len(faces_data)}")
print(f"Etiquetas unicas: {np.unique(labels_array)}")

face_recognizer = cv.face.EigenFaceRecognizer_create()

face_recognizer.train(faces_data, labels_array)
face_recognizer.write(str(MODEL_PATH))

print(f"\nModelo guardado en: {MODEL_PATH}")
