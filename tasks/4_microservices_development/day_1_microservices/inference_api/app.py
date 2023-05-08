from PIL import Image
import numpy as np
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog


def main():
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

    image = np.array(Image.open("example.jpg"))

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
    detected_image.save("out.jpg", format="JPEG")


if __name__ == "__main__":
    main()
