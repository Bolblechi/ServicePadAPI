FROM python:alpine3.18

WORKDIR /app

COPY ./app /app

RUN pip3 install -r requirements.txt --no-cache-dir

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8080"]
