FROM python:slim-jessie
ADD requirements.txt /app/requirements.txt
ADD . /app/
WORKDIR /app/
RUN pip install -r requirements.txt