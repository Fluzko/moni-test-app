from python:3-alpine

MAINTAINER Facu

RUN apk add gcc
RUN apk add libc-dev
RUN apk add libffi-dev

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3", "run.py"]