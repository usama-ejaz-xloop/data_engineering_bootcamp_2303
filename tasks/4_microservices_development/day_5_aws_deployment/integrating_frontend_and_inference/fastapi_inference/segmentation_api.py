import base64
import io

import pydantic
from detectron2.utils.logger import setup_logger
import cv2
from PIL import Image
import numpy as np
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
from fastapi import FastAPI

setup_logger()

app = FastAPI()


def decode_image_base64(img_base64: str) -> Image.Image:
    buff = io.BytesIO(base64.b64decode(img_base64))
    img = Image.open(buff).convert("RGB")
    return img


class InferenceRequestResponse(pydantic.BaseModel):
    base64_image: str


@app.post("/inference")
def inference(inference_request: InferenceRequestResponse) -> InferenceRequestResponse:
    im_bytes = base64.b64decode(inference_request.base64_image)
    im_arr = np.frombuffer(im_bytes, dtype=np.uint8)  # im_arr is one-dim Numpy array
    image = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
    return _predict(image)


def _predict(image: np.ndarray) -> InferenceRequestResponse:
    """
    :param (np.ndarray): image of shape (H, W, C) (in BGR order):
    :return: InferenceRequestResponse
    """
    # Set configurations
    cfg = get_cfg()
    cfg.MODEL.DEVICE = "cpu"
    cfg.merge_from_file(
        model_zoo.get_config_file(
            "COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"
        )
    )
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(
        "COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"
    )

    # Create a simple end-to-end predictor with the given config that runs on single device for a single input image.
    predictor = DefaultPredictor(cfg)
    outputs = predictor(image)  # (dict) – the output of the model for one image only

    # Draw the predictions on the image
    v = Visualizer(
        image[:, :, ::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.2
    )
    out = v.draw_instance_predictions(outputs["instances"].to("cpu"))

    # Get an image with draw predictions and transfer it to base64
    detected_image = Image.fromarray(out.get_image())
    buffered = io.BytesIO()
    detected_image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    return InferenceRequestResponse(**{"base64_image": img_str})
