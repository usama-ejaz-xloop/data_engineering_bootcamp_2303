FROM python:3.8-slim-buster

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y python3-opencv
WORKDIR /home/appuser
ENV PATH="/home/appuser/.local/bin:${PATH}"
RUN python -m pip install detectron2 -f \
  https://dl.fbaipublicfiles.com/detectron2/wheels/cpu/torch1.10/index.html
COPY ./requirements.txt /home/appuser/requirements.txt
RUN pip install -r /home/appuser/requirements.txt
COPY ./ .
CMD ["uvicorn", "segmentation_api:app", "--host", "0.0.0.0", "--port", "8686", "--reload"]