FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
ADD requirements-dev.txt /code/
ADD gulpfile.js /code/
ADD package.json /code/

RUN apt-get update -y && \
    apt-get install gettext -y &&\
    apt-get install -y nodejs && \
    apt-get install npm -y && \
    apt-get install nodejs-legacy

RUN pip install -r requirements.txt

ADD . /code/

RUN npm install
