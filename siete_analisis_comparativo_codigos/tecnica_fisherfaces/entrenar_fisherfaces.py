import cv2 as cv
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "DATASET"

DATASETS_POR_PERSONA = {
    "SEBASTIAN": [
        "SEBASTIAN_NO_LUZ",
        "SEBASTIAN_LUZ",
        "SEBASTIAN_LUZ_NATURAL",
    ],
    "PERSONA_01": [
        "DATASET_persona_01",
    ],
}

MODEL_PATH = (
    Path(__file__).resolve().parent
    / "SebastianFisherFace.xml"
)

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp"}

faces_data = []
labels = []
image_size = None

for label, (person, folders) in enumerate(
    DATASETS_POR_PERSONA.items()
):
    person_count = 0

    for folder_name in folders:
        folder_path = DATASET_DIR / folder_name

        if not folder_path.is_dir():
            raise FileNotFoundError(
                f"No se encontro el dataset: {folder_path}"
            )

        folder_count = 0

        for img_path in sorted(folder_path.iterdir()):
            if img_path.suffix.lower() not in IMAGE_EXTENSIONS:
                continue

            img = cv.imread(
                str(img_path),
                cv.IMREAD_GRAYSCALE
            )

            if img is None:
                print(f"Imagen ignorada: {img_path.name}")
                continue

            # Fisherfaces necesita imagenes del mismo tamano.
            if image_size is None:
                image_size = img.shape

            if img.shape != image_size:
                raise ValueError(
                    f"Tamano diferente en {img_path}.\n"
                    f"Esperado: {image_size}; "
                    f"recibido: {img.shape}"
                )

            faces_data.append(img)
            labels.append(label)

            folder_count += 1
            person_count += 1

        print(
            f"{folder_name}: "
            f"{folder_count} imagenes validas"
        )

    print(
        f"Total de {person}: "
        f"{person_count} imagenes"
    )

if not faces_data:
    raise RuntimeError(
        "No se encontraron imagenes validas para entrenar."
    )

labels_array = np.array(labels, dtype=np.int32)
unique_labels = np.unique(labels_array)

print("\nResumen del entrenamiento")
print(f"Total de imagenes: {len(faces_data)}")
print(f"Identidades encontradas: {len(unique_labels)}")
print(f"Etiquetas: {unique_labels.tolist()}")

if len(unique_labels) < 2:
    raise RuntimeError(
        "Fisherfaces requiere al menos dos identidades distintas."
    )

face_recognizer = cv.face.FisherFaceRecognizer_create()

face_recognizer.train(
    faces_data,
    labels_array
)

face_recognizer.write(str(MODEL_PATH))

print(f"\nModelo guardado en: {MODEL_PATH}")
