from flask import Flask, request, jsonify, abort
from PIL import Image, ImageFilter
import pytesseract, base64, io

app = Flask(__name__)

@app.route("/ocr", methods=["POST"])
def ocr():
    data = request.get_json()
    img_bytes = base64.b64decode(data["image"])
    img = Image.open(io.BytesIO(img_bytes)).convert("L")
    img = img.filter(ImageFilter.SHARPEN)
    text = pytesseract.image_to_string(img, config="--psm 6")
    return jsonify({"text": text.strip()})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
