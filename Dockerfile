FROM python:3.9.7

MAINTAINER Ken Mwaura "kemwaura@gmail.com"

ENV PYTHON_PATH /usr/local/python3.9/bin/python3.9
ENV PORT 8001

WORKDIR app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

# RUN apt-get update && apt-get install -y python3.9 python3.9-dev

COPY . /app

RUN cp .env.example .env

RUN chmod a+x ./run.sh

RUN ./run.sh





