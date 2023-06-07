FROM python:3.11-slim-buster
ENV DOCKER_RUNNING=true
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt 

COPY ./app .