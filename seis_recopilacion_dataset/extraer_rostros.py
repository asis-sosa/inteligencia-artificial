import cv2 as cv
from pathlib import Path

# =========================
# CONFIGURACION
# =========================

BASE_DIR = Path(__file__).resolve().parent
VIDEO_PATH = BASE_DIR / "videos" / "video_01.webm"
OUTPUT_DIR = BASE_DIR / "DATASETS" / "DATASET_persona_01"

MAX_IMAGES = 1000
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
# PREPARAR EL VIDEO
# =========================

if not VIDEO_PATH.is_file():
    raise FileNotFoundError(
        f"No se encontro el video: {VIDEO_PATH}"
    )

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Evitar mezclar resultados de ejecuciones anteriores.
if any(OUTPUT_DIR.iterdir()):
    raise RuntimeError(
        f"La carpeta de salida no esta vacia: {OUTPUT_DIR}\n"
        "Usa otra carpeta o mueve los archivos existentes."
    )

cap = cv.VideoCapture(str(VIDEO_PATH))

if not cap.isOpened():
    raise RuntimeError("No se pudo abrir el video.")

# =========================
# EXTRACCION
# =========================

frame_index = 0
saved_count = 0

try:
    while saved_count < MAX_IMAGES:
        ret, frame = cap.read()

        if not ret:
            print("El video termino o no se pudo leer.")
            break

        # Convertir el fotograma a escala de grises.
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Detectar rostros frontales.
        faces = detector.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(60, 60)
        )

        # Dibujar las detecciones para inspeccion visual.
        for (x, y, w, h) in faces:
            cv.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

        # Guardar solo en los fotogramas seleccionados.
        if frame_index % SAMPLE_EVERY == 0 and len(faces) > 0:

            # Elegir el rostro de mayor area.
            x, y, w, h = max(
                faces,
                key=lambda face: face[2] * face[3]
            )

            face = frame[y:y + h, x:x + w]

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

        cv.putText(
            frame,
            f"Imagenes: {saved_count}/{MAX_IMAGES}",
            (20, 35),
            cv.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv.imshow("Deteccion de rostros", frame)

        if cv.waitKey(1) & 0xFF == 27:
            print("Extraccion detenida por el usuario.")
            break

        frame_index += 1

finally:
    cap.release()
    cv.destroyAllWindows()

print(f"Total de imagenes guardadas: {saved_count}")
print(f"Carpeta de salida: {OUTPUT_DIR.resolve()}")

if saved_count < MAX_IMAGES:
    print(
        "Atencion: el dataset no alcanzo las "
        f"{MAX_IMAGES} imagenes solicitadas."
    )
