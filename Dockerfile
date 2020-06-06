FROM python:3.7.3-alpine3.9 as base

FROM node:12-stretch

USER python

RUN mkdir -p /home/python/PyFlaskAlgorithmsAPI

WORKDIR /home/node/code

COPY --chown=node:node package-lock.json package.json ./

RUN npm ci

COPY --chown=node:node . .

EXPOSE 3000

CMD ["node", "index.js"]

RUN mkdir -p /PyFlaskAlgorithmsAPI/
RUN mkdir -p /app/PyFlaskAlgorithmsAPI/app/
RUN mkdir -p /app/PyFlaskAlgorithmsAPI/batch/
RUN mkdir -p /app/PyFlaskAlgorithmsAPI/resource/

WORKDIR /app/SmartSteelPyFlaskCSV/app/

COPY ./requirements_flask.txt /app/SmartSteelPyFlaskCSV/app/requirements_flask.txt
RUN pip install --upgrade pip
RUN pip install -r requirements_flask.txt
COPY ./app/ /app/SmartSteelPyFlaskCSV/app/
COPY ./batch/ /app/SmartSteelPyFlaskCSV/batch/
COPY ./resource/ /app/SmartSteelPyFlaskCSV/resource/

ENV FLASK_APP=smart_steel_app.py

CMD flask run -h 0.0.0.0 -p 5000