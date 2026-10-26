
import cv2 as cv
from pathlib import Path

# =========================
# CONFIGURACION
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent

# Carpeta donde se guardaran las imagenes.
DATASET_DIR = BASE_DIR / "DATASET"
OUTPUT_DIR = DATASET_DIR / "NOMBRE_DATASET"

# Indice de la camara:
# 0 = camara predeterminada.
# Si no funciona, probar con 1.
CAMERA_INDEX = 0

MAX_IMAGES = 500

# Guardar una imagen cada N fotogramas.
SAMPLE_EVERY = 10

FACE_SIZE = (160, 160)
JPEG_QUALITY = 90

# =========================
# PREPARAR EL CLASIFICADOR
# =========================

cascade_path = (
    cv.data.haarcascades
    + "haarcascade_frontalface_default.xml"
)

detector = cv.CascadeClassifier(cascade_path)

if detector.empty():
    raise RuntimeError(
        "No se pudo cargar el clasificador Haar Cascade."
    )

# =========================
# PREPARAR LA CARPETA
# =========================

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Evitar mezclar resultados de ejecuciones anteriores.
if any(OUTPUT_DIR.iterdir()):
    raise RuntimeError(
        f"La carpeta de salida no esta vacia: {OUTPUT_DIR}\n"
        "Usa otra carpeta o mueve los archivos existentes."
    )

# =========================
# INICIAR LA CAMARA
# =========================

cap = cv.VideoCapture(CAMERA_INDEX)

if not cap.isOpened():
    raise RuntimeError(
        "No se pudo abrir la camara. "
        "Verifica que este conectada y disponible."
    )

# =========================
# CAPTURA EN TIEMPO REAL
# =========================

frame_index = 0
saved_count = 0

print("Camara iniciada correctamente.")
print("Coloca tu rostro frente a la camara.")
print("Presiona ESC para salir.")
print("Presiona S para guardar un rostro manualmente.")

try:
    while saved_count < MAX_IMAGES:
        ret, frame = cap.read()

        if not ret:
            print("No se pudo leer un fotograma de la camara.")
            break

        # Voltear horizontalmente la vista previa,
        # como un espejo. No afecta la imagen guardada.
        preview = cv.flip(frame, 1)

        # Trabajar en escala de grises para detectar rostros.
        gray = cv.cvtColor(preview, cv.COLOR_BGR2GRAY)

        faces = detector.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(60, 60)
        )

        # Dibujar rectangulos alrededor de los rostros.
        for (x, y, w, h) in faces:
            cv.rectangle(
                preview,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

        # Seleccionar automaticamente el rostro mas grande
        # cada SAMPLE_EVERY fotogramas.
        save_automatically = (
            frame_index % SAMPLE_EVERY == 0
            and len(faces) > 0
        )

        # S = captura manual.
        key = cv.waitKey(1) & 0xFF
        save_manually = key == ord("s") and len(faces) > 0

        if save_automatically or save_manually:

            # Elegir el rostro de mayor area.
            x, y, w, h = max(
                faces,
                key=lambda face: face[2] * face[3]
            )

            face = preview[y:y + h, x:x + w]

            if face.size > 0:
                resized = cv.resize(
                    face,
                    FACE_SIZE,
                    interpolation=cv.INTER_AREA
                )

                filename = OUTPUT_DIR / (
                    f"{saved_count + 1:04d}.jpg"
                )

                success = cv.imwrite(
                    str(filename),
                    resized,
                    [cv.IMWRITE_JPEG_QUALITY, JPEG_QUALITY]
                )

                if success:
                    saved_count += 1
                    print(
                        f"Guardadas: {saved_count}/{MAX_IMAGES}"
                    )

        # Mostrar informacion en la vista previa.
        cv.putText(
            preview,
            f"Imagenes: {saved_count}/{MAX_IMAGES}",
            (20, 35),
            cv.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv.putText(
            preview,
            "S: guardar | ESC: salir",
            (20, 70),
            cv.FONT_HERSHEY_SIMPLEX,
            0.65,
            (255, 255, 0),
            2
        )

        cv.imshow("Captura de rostros - Dataset", preview)

        if key == 27:
            print("Captura detenida por el usuario.")
            break

        frame_index += 1

finally:
    cap.release()
    cv.destroyAllWindows()

# =========================
# RESULTADOS
# =========================

print("\nCaptura finalizada.")
print(f"Total de imagenes guardadas: {saved_count}")
print(f"Carpeta de salida: {OUTPUT_DIR.resolve()}")

if saved_count < MAX_IMAGES:
    print(
        f"Atencion: se guardaron {saved_count} de "
        f"{MAX_IMAGES} imagenes solicitadas."
    )
