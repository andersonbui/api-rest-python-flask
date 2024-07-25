FROM python:3.10-alpine

RUN mkdir /application
WORKDIR /application

# dependencias
COPY ./requirements.txt /application
RUN pip install --no-cache-dir -r ./requirements.txt

# script de inicio
COPY start.sh /start.sh

CMD "./start.sh"