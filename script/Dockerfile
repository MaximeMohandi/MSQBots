FROM python:3.7.4-slim
WORKDIR /app
COPY . /app
RUN pip install -r /requirements.txt
EXPOSE 80
ENV NAME msqbitsreporter
CMD "python" "-m" "msqbitsReporter"