# Example object detection script
This is a script that performs object detection on an image. Your task will be to expose an
API to the inference and Dockerize the resulting microservice.

To start the inference, use:

```
python3 -m venv venv
. venv/bin/activate
# Install requirements
pip install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html
# Install the object detection toolkit we will use
pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cpu/torch1.10/index.html
python3 app.py
```
