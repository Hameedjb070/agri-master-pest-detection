"""
Loads a YOLO model and runs pest detection on uploaded images.

Looks for a trained model at models/pest_yolov9_best.pt. Falls back to the
generic pretrained yolov8n.pt (everyday objects, not pests) so the API can be
built and tested before training finishes -- swap in the real weights when
ready and no other code needs to change.
"""
import time
from pathlib import Path

from ultralytics import YOLO

from pest_info import get_pest_info

TRAINED_WEIGHTS = Path(__file__).resolve().parent.parent / "models" / "pest_yolov9_best.pt"
FALLBACK_WEIGHTS = "yolov8n.pt"

_model = None
_using_fallback = False


def get_model():
    global _model, _using_fallback
    if _model is None:
        if TRAINED_WEIGHTS.exists():
            _model = YOLO(str(TRAINED_WEIGHTS))
            _using_fallback = False
        else:
            _model = YOLO(FALLBACK_WEIGHTS)
            _using_fallback = True
    return _model


def is_using_fallback():
    get_model()
    return _using_fallback


def predict(image_path, confidence=0.25):
    model = get_model()
    start = time.time()
    results = model.predict(image_path, conf=confidence, verbose=False)
    elapsed_ms = round((time.time() - start) * 1000)

    detections = []
    result = results[0]
    for box in result.boxes:
        cls_id = int(box.cls[0])
        class_name = result.names[cls_id]
        detections.append({
            "class": class_name,
            "confidence": round(float(box.conf[0]) * 100, 1),
            "box": [round(v, 1) for v in box.xyxy[0].tolist()],
            "info": get_pest_info(class_name),
        })

    return {
        "detections": detections,
        "inference_ms": elapsed_ms,
        "using_fallback_model": _using_fallback,
    }
