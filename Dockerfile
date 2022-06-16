FROM python:3.9.4-slim

COPY .env.example .env
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
