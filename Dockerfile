# Light weight Linux version - not much software needs to run the application
FROM python:3.7.7-alpine3.12

RUN mkdir -p /home/algorithmsAPI/webAPI

WORKDIR /home/algorithmsAPI/webAPI

# workaround to install numpy for alpine
# Install native libraries, required for numpy
RUN apk --no-cache add musl-dev linux-headers g++

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN pip install gunicorn

COPY  ./webAPI .

RUN chmod -R 777 .

ENV FLASK_APP=algorithms_api.py

EXPOSE 5000

CMD gunicorn \
  --workers 4 \
  --threads 16 \
  --bind 0.0.0.0:5000 \
  algorithms_api:app

