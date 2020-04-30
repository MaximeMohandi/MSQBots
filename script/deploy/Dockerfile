FROM python

WORKDIR /app
COPY . /app

RUN python -m pip install -r requirements.txt

ENV NAME msqbot
CMD "python" "-m" "msqbot"
