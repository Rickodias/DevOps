#Dockerfile, Image, Container
FROM python:3.9.18

ADD main.py .

RUN pip install requests

CMD [ "python", "./main.py" ]

