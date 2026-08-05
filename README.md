# Agri-Master — AI-Powered Crop Pest Detection

A real-time crop pest detection system: a fine-tuned **YOLOv9** model (with a
**Faster R-CNN** comparison model) served through a **Flask** API, with a
mobile-responsive web UI for uploading a photo and getting back detected pests,
bounding boxes, and practical guidance (damage caused, prevention, treatment).

## Results

Evaluated on a held-out test set of 562 images, across 15 real pest categories:

| Metric | YOLOv9 (production model) | Faster R-CNN (comparison) |
|---|---|---|
| mAP50 | **81.8%** | 78.2% |
| mAP50-95 | **48.1%** | 44.3% |
| Recall | 72.7% | 59.1% |

Full breakdown, per-class numbers, and discussion of the YOLOv9 vs Faster R-CNN
tradeoff: [docs/evaluation_results.md](docs/evaluation_results.md).

## How it works

1. **Dataset**: [Roboflow-hosted pest detection dataset](https://universe.roboflow.com/pest-2bk0e/detection-d0qov)
   (sourced from [IP102](https://github.com/xpwu95/IP102), CC BY 4.0), filtered
   down from 97 sparse classes to the **15 best-represented classes**
   (5,499 labeled images) — see [src/prepare_dataset.py](src/prepare_dataset.py).
2. **Training**: YOLOv9c fine-tuned for 50 epochs (with early stopping) and
   Faster R-CNN (ResNet50-FPN backbone) fine-tuned for 10 epochs, both on a free
   Google Colab GPU — see [notebooks/](notebooks/).
3. **Serving**: a Flask API (`/predict`) loads the trained YOLOv9 weights and
   runs inference on uploaded images, returning bounding boxes, confidence
   scores, and pest-specific guidance from a small reference database
   ([app/pest_info.py](app/pest_info.py)).
4. **Frontend**: a single-page upload UI draws detection boxes on a `<canvas>`
   over the uploaded photo and lists what was found.

## Project structure

```
agri-master/
├── app/
│   ├── main.py           # Flask app + /predict route
│   ├── inference.py       # Loads YOLO model, runs detection
│   ├── pest_info.py       # Pest reference database (damage/prevention/treatment)
│   ├── templates/         # HTML
│   └── static/            # CSS/JS
├── src/
│   ├── download_dataset.py   # Pulls raw dataset from Roboflow
│   └── prepare_dataset.py    # Filters to the 15 target classes
├── notebooks/
│   ├── train_yolov9.ipynb       # Colab: fine-tune YOLOv9
│   └── train_fasterrcnn.ipynb   # Colab: fine-tune Faster R-CNN
├── docs/
│   └── evaluation_results.md  # Full metrics + per-class breakdown
├── data/                  # Local only (gitignored) — datasets
└── models/                # Local only (gitignored) — trained weights
```

## Running it locally

Requires Python 3.12+.

```bash
git clone https://github.com/Hameedjb070/agri-master-pest-detection.git
cd agri-master-pest-detection
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

You'll need the trained YOLOv9 weights at `models/pest_yolov9_best.pt` (not
included in the repo — see "Reproducing the training" below). Without it, the
app automatically falls back to a generic pretrained model so the API/UI still
work end-to-end for testing.

```bash
python app/main.py
```

Then open `http://127.0.0.1:5050`.

## Reproducing the training

1. Get a free [Roboflow](https://roboflow.com) account and API key.
2. Open `notebooks/train_yolov9.ipynb` in [Google Colab](https://colab.research.google.com)
   (`Runtime → Change runtime type → T4 GPU`), add your API key as a Colab
   Secret named `ROBOFLOW_API_KEY`, and run all cells.
3. Download the resulting `pest_yolov9_best.pt` and place it in `models/`.
4. (Optional) Repeat with `notebooks/train_fasterrcnn.ipynb` for the comparison model.

## Tech stack

Python, Flask, PyTorch, Ultralytics (YOLOv9), torchvision (Faster R-CNN),
Roboflow (dataset hosting), vanilla JS/CSS (frontend, no framework).

## Dataset attribution

Pest images and annotations sourced from the
[IP102](https://github.com/xpwu95/IP102) benchmark dataset via
[Roboflow Universe](https://universe.roboflow.com/pest-2bk0e/detection-d0qov),
licensed CC BY 4.0.
