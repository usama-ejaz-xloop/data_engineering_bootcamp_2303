import base64
import os

import requests
from flask import Flask, render_template, request

app = Flask(__name__)


def inference(request_data):
    predictions_url = f"http://{os.environ['SERVICE_DISCOVERY']}:8686/inference"
    return requests.post(predictions_url, json=request_data)


@app.route("/", methods=["GET", "POST"])
def main(image_data=None, image_name=None):
    if request.method == "POST" and request.files["image"]:
        image = request.files["image"]
        image_name = image.filename
        image_bytes = image.stream.read()
        payload = {"base64_image": base64.b64encode(image_bytes).decode("utf8")}
        inference_response = inference(payload)
        image_data = inference_response.json()["base64_image"]
    return render_template(
        "inference/inference.html", image_data=image_data, image_name=image_name
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
