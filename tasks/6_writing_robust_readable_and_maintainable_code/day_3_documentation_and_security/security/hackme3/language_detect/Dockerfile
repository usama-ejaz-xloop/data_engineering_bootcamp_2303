FROM python:3.8-slim-buster

WORKDIR /home/app

COPY ./requirements.txt /home/app/requirements.txt

RUN pip install -r /home/app/requirements.txt

COPY ./ .
