FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py app.py

ENV PYTHONPATH /app

CMD [ "python3", "app.py"]
