FROM python:3.7.3-alpine3.9

RUN mkdir -p /home/algorithmsAPI/

WORKDIR /home/algorithmsAPI/

COPY  . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app/algorithms_api.py" ]
