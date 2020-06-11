# run application as stand alon server - for development needs only
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

COPY  ./webAPI .

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "algorithms_api.py" ]



