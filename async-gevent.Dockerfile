# run application with gunicorn server (asynchronous version) - for real life usage (prod)
# Light weight Linux version - not much software needs to run the application
FROM python:3.7.7-alpine3.12

RUN mkdir -p /home/algorithmsAPI/webAPI

WORKDIR /home/algorithmsAPI/webAPI

# workaround to install numpy for alpine
# Install native libraries, required for numpy
RUN apk --no-cache add musl-dev linux-headers g++

#  workaround to install gevent for alpine
RUN apk add --no-cache python3-dev libffi-dev gcc musl-dev make

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# add web server gunicorn to run application
# add gevent as async layer
RUN pip install gunicorn gevent

COPY  ./webAPI .

ENV FLASK_APP=algorithms_api.py

EXPOSE 5000

# start application
CMD gunicorn --worker-class gevent \
  --workers 4 \
  --bind 0.0.0.0:5000 \
  algorithms_api:app
