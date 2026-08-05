const imageInput = document.getElementById("imageInput");
const uploadBox = document.getElementById("uploadBox");
const uploadLabel = document.getElementById("uploadLabel");
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const statusEl = document.getElementById("status");
const resultsEl = document.getElementById("results");

const BOX_COLOR = "#e53935";

imageInput.addEventListener("change", async () => {
    const file = imageInput.files[0];
    if (!file) return;

    uploadLabel.textContent = file.name;
    resultsEl.innerHTML = "";
    statusEl.textContent = "Detecting pests...";

    const img = new Image();
    img.onload = () => drawImage(img);
    img.src = URL.createObjectURL(file);

    const formData = new FormData();
    formData.append("image", file);

    try {
        const response = await fetch("/predict", { method: "POST", body: formData });
        const data = await response.json();

        if (data.error) {
            statusEl.textContent = `Error: ${data.error}`;
            return;
        }

        img.onload = () => {
            drawImage(img);
            data.detections.forEach((det) => drawBox(det));
        };
        if (img.complete) {
            drawImage(img);
            data.detections.forEach((det) => drawBox(det));
        }

        renderResults(data);
    } catch (err) {
        statusEl.textContent = `Request failed: ${err}`;
    }
});

function drawImage(img) {
    canvas.width = img.width;
    canvas.height = img.height;
    canvas.style.display = "block";
    ctx.drawImage(img, 0, 0);
}

function drawBox(det) {
    const [x1, y1, x2, y2] = det.box;
    ctx.strokeStyle = BOX_COLOR;
    ctx.lineWidth = Math.max(2, canvas.width / 250);
    ctx.strokeRect(x1, y1, x2 - x1, y2 - y1);

    const label = `${det.class} ${det.confidence}%`;
    ctx.font = `${Math.max(14, canvas.width / 40)}px sans-serif`;
    const textWidth = ctx.measureText(label).width;
    ctx.fillStyle = BOX_COLOR;
    ctx.fillRect(x1, y1 - 20, textWidth + 8, 20);
    ctx.fillStyle = "white";
    ctx.fillText(label, x1 + 4, y1 - 5);
}

function renderResults(data) {
    const modelNote = data.using_fallback_model
        ? " (using placeholder model - not yet trained on pests)"
        : "";
    statusEl.textContent = `${data.detections.length} detection(s) in ${data.inference_ms}ms${modelNote}`;

    resultsEl.innerHTML = "";
    data.detections.forEach((det) => {
        const card = document.createElement("div");
        card.className = "detection-card";

        const header = document.createElement("div");
        header.className = "detection-header";
        const displayName = det.info ? det.info.common_name : det.class;
        header.innerHTML = `<span>${displayName}</span><span class="conf">${det.confidence}%</span>`;
        card.appendChild(header);

        if (det.info) {
            const info = det.info;
            const body = document.createElement("div");
            body.className = "detection-body";
            body.innerHTML = `
                <p><strong>Damage:</strong> ${info.damage}</p>
                <p><strong>How to avoid it:</strong> ${info.prevention}</p>
                <p><strong>Treatment:</strong> ${info.treatment}</p>
                <p class="disclaimer">${info.disclaimer}</p>
            `;
            card.appendChild(body);
        }

        resultsEl.appendChild(card);
    });
}
