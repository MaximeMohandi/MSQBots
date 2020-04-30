FROM python:3.7.4-slim

WORKDIR /app
COPY . /app

RUN python -m pip install -r requirements.txt

ENV NAME msqbot
CMD "python" "-m" "msqbot"
