FROM python:3.8-slim-buster

WORKDIR /home/app/

COPY ./requirements.txt /home/app/requirements.txt
RUN pip3 install -r /home/app/requirements.txt

COPY ./ /home/app/
ENV PYTHONPATH=${PYTHONPATH}:/home/app/
CMD ["python", "main.py"]
