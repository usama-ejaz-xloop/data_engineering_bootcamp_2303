FROM python:3.8-slim-buster

WORKDIR /home/app/

RUN apt-get update && apt-get -yy install wget && apt-get clean

RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -O /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY ./ /home/app/

ENV PYTHONPATH=${PYTHONPATH}:/home/app/
