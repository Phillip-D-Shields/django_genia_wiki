# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY wait-for-it.sh /code/
RUN chmod +x /code/wait-for-it.sh
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

