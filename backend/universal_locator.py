from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import torch
import os
import requests
from groundingdino.util.inference import load_model, load_image, predict

# === Config ===
MODEL_CONFIG_PATH = "GroundingDINO/groundingdino/config/GroundingDINO_SwinT_OGC.py"
MODEL_WEIGHTS_PATH = "weights/groundingdino_swint_ogc.pth"
BOX_THRESHOLD = 0.4
TEXT_THRESHOLD = 0.3
device = torch.device("cpu")

# === Download model if not present ===
MODEL_GDRIVE_ID = "1gb-8fvuFW_M9GE2EOwj8pNjuNWJiWKUq"
MODEL_URL = f"https://drive.google.com/uc?export=download&id={MODEL_GDRIVE_ID}"

os.makedirs("weights", exist_ok=True)
if not os.path.exists(MODEL_WEIGHTS_PATH):
    print("🔽 Downloading model weights...")
    response = requests.get(MODEL_URL, stream=True)
    with open(MODEL_WEIGHTS_PATH, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    print("✅ Download complete.")

# === Initialize App ===
app = Flask(__name__)
CORS(app)

# === Load Model ===
print("🚀 Loading model...")
model = load_model(MODEL_CONFIG_PATH, MODEL_WEIGHTS_PATH)
print("✅ Model loaded.")

# === API Route ===
@app.route("/locate", methods=["POST"])
def locate():
    object_name = request.form.get("object")
    image_file = request.files.get("image")

    if not object_name or not image_file:
        return jsonify({"error": "Missing object or image"}), 400

    image_path = "temp.jpg"
    image_file.save(image_path)
    image_source, image = load_image(image_path)

    boxes, logits, phrases = predict(
        model=model,
        image=image,
        caption=object_name,
        box_threshold=BOX_THRESHOLD,
        text_threshold=TEXT_THRESHOLD,
        device=device
    )

    if len(boxes) == 0:
        return jsonify({"found": False})

    box = boxes[0].tolist()
    return jsonify({
        "found": True,
        "bbox": {
            "x1": int(box[0]), "y1": int(box[1]),
            "x2": int(box[2]), "y2": int(box[3])
        },
        "label": phrases[0]
    })

# === Run Server ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
