# Light weight Linux version - not much software needs to run the application
FROM python:3.7.7-alpine3.12

RUN mkdir -p /home/algorithmsAPI/

WORKDIR /home/algorithmsAPI/

# workaround
RUN apk add py-numpy
# In the next step install it with pip.
# RUN python -m pip install numpy

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY  . .

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app/algorithms_api.py" ]
