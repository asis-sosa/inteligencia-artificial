import cv2 as cv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "SebastianEigenface.xml"

CASCADE_PATH = (
    Path(cv.data.haarcascades) / "haarcascade_frontalface_alt2.xml"
)

FACE_SIZE = (160, 160)

NOMBRES = {
    0: "Sebastián",
}

THRESHOLD = 2800

if not MODEL_PATH.is_file():
    raise FileNotFoundError(f"No se encontró el modelo: {MODEL_PATH}")

if not CASCADE_PATH.is_file():
    raise FileNotFoundError(f"No se encontró el clasificador: {CASCADE_PATH}")

face_recognizer = cv.face.EigenFaceRecognizer_create()
face_recognizer.read(str(MODEL_PATH))

cascade = cv.CascadeClassifier(str(CASCADE_PATH))

if cascade.empty():
    raise RuntimeError("No se pudo cargar el clasificador Haar Cascade.")

cap = cv.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("No se pudo abrir la cámara.")

try:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("No se pudo leer la imagen de la cámara.")
            break

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        rostros = cascade.detectMultiScale(gray, 1.3, 3)

        for (x, y, w, h) in rostros:
            roi = gray[y:y + h, x:x + w]
            roi = cv.resize(roi, FACE_SIZE, interpolation=cv.INTER_CUBIC)

            label_id, confidence = face_recognizer.predict(roi)

            if label_id in NOMBRES and confidence < THRESHOLD:
                name = NOMBRES[label_id]
                color = (0, 255, 0)
                texto = f"{name} ({confidence:.0f})"
            else:
                color = (0, 0, 255)
                texto = f"Desconocido ({confidence:.0f})"

            cv.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv.putText(
                frame, texto, (x, max(y - 12, 20)),
                cv.FONT_HERSHEY_SIMPLEX, 0.7, color, 1, cv.LINE_AA
            )

        cv.imshow("Reconocimiento en vivo - Eigenfaces", frame)

        if cv.waitKey(1) == 27:
            break
finally:
    cap.release()
    cv.destroyAllWindows()
