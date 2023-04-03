FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./app .

EXPOSE 8000

CMD [ "python", "main.py"]