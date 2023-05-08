import base64

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main(image_data=None, image_name=None):
    if request.method == "POST" and request.files["image"]:
        image = request.files["image"]
        image_name = image.filename
        image_bytes = image.stream.read()
        payload = {"base64_image": base64.b64encode(image_bytes).decode("utf8")}
        image_data = (
            None  # later, it will be replaced with a call to an inference function
        )
    return render_template(
        "inference/inference.html", image_data=image_data, image_name=image_name
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
