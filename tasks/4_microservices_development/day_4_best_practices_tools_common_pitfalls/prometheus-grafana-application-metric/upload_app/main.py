import binascii
import os
import string

from flask import abort, Flask, render_template, request, send_from_directory

app = Flask(__name__)


ALLOWED_EXTENSIONS = [".jpg", ".png"]
UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "uploads")


def validate_name_characters(image_name: str):
    # We whitelist only letters, digits and dots to prevent directory traversal attacks (e.g. trying to read/upload
    # ../../../../etc/passwd or whatever the path separator is on a given system).

    for c in image_name:
        if c not in ". " and c not in string.ascii_letters and c not in string.digits:
            abort(400, f"{c} not allowed in file name")


def has_allowed_extension(name: str) -> bool:
    _, ext = os.path.splitext(name)
    return ext in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST" and request.files["image"]:
        image = request.files["image"]
        image_name = image.filename
        image_bytes = image.stream.read()

        validate_name_characters(image_name)

        if not has_allowed_extension(image_name):
            abort(
                400,
                f"Extension {ext} not allowed. Allowed extensions: {' '.join(ALLOWED_EXTENSIONS)}",
            )

        # We prepend a random token to the name to solve the problem of multiple people submitting a file with the same name.
        with open(
            os.path.join(
                UPLOAD_DIR,
                binascii.hexlify(os.urandom(10)).decode("ascii") + image_name,
            ),
            "wb",
        ) as f:
            f.write(image_bytes)

    return render_template(
        "index.html",
        images=[
            image for image in os.listdir(UPLOAD_DIR) if has_allowed_extension(image)
        ],
    )


@app.route("/uploads/<string:path>")
def static_file(path):
    validate_name_characters(path)
    return send_from_directory(UPLOAD_DIR, path)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
