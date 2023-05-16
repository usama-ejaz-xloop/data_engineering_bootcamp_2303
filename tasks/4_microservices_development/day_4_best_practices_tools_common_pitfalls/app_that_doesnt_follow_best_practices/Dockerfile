FROM python:3.8-slim-buster

WORKDIR /home/app/

COPY ./ /home/app/

ENV PYTHONPATH=${PYTHONPATH}:/home/app/

CMD ["bash", "-c", "pip install -r requirements.txt && gunicorn main:app -b 0.0.0.0:5000"]
