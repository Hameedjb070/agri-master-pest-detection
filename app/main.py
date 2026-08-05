import tempfile
from pathlib import Path

from flask import Flask, jsonify, render_template, request

from inference import predict

app = Flask(__name__)

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict_route():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]
    ext = Path(image.filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        return jsonify({"error": f"Unsupported file type: {ext}"}), 400

    with tempfile.NamedTemporaryFile(suffix=ext, delete=True) as tmp:
        image.save(tmp.name)
        result = predict(tmp.name)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, port=5050)
