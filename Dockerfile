FROM python:3.7.3-alpine3.9

MAINTANER Volodymyr Moskov "boba.mockob@gmail.com"

RUN mkdir -p /home/algorithmsAPI/

WORKDIR /home/algorithmsAPI/

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY  . .

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app/algorithms_api.py" ]
