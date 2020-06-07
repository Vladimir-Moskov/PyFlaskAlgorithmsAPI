FROM python:3.7.3-alpine3.9

USER algorithmsAPI

WORKDIR /home/algorithmsAPI/

COPY --chown=algorithmsAPI:algorithmsAPI  . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "algorithms_api.py" ]
