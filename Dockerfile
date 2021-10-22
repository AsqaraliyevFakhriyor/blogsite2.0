FROM python:stretch

LABEL maintainer="Asqaliyev Faxriyor"
LABEL description="testing to deploy django app on heroku with docker + aws s3 bucket"
LABEL date="2021-10-20"


COPY requirements.txt /project/requirements.txt
RUN set -ex \
    && pip install --upgrade pip \
    && pip install -r /project/requirements.txt

WORKDIR /project
COPY . /project/


CMD gunicorn main.wsgi:application --bind 0.0.0.0:$PORT 