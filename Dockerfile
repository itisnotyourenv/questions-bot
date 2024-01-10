FROM python:3.11-slim
# get BOT_NAME from .env !
ENV BOT_NAME=mybotname

WORKDIR /usr/src/app/${BOT_NAME}

COPY requirements.txt /usr/src/app/${BOT_NAME}
RUN pip install -r /usr/src/app/${BOT_NAME}/requirements.txt

RUN apt-get update -y
RUN apt-get install -y libraqm-dev

COPY . /usr/src/app/${BOT_NAME}
