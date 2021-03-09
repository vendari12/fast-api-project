# pull official base image
FROM python:3.8.1-alpine

# set work directory
WORKDIR /usr/project/main

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY ./requirements.txt .requirements.txt

# install dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
    libressl-dev libffi-dev gcc musl-dev python3-dev \
    mongo-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /usr/project/main/requirements.txt \
    && rm -rf /root/.cache/pip

# copy project
COPY . /usr/project/main/
