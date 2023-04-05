FROM python:latest

COPY requirements.txt /

RUN pip install -r requirements.txt

COPY . /home/app

WORKDIR /home/app

CMD ["bash", "-c", "python manage.py migrate && gunicorn src.wsgi -b 0.0.0.0:8000"]
