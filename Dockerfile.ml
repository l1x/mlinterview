FROM python:3.6
MAINTAINER XenonStack

RUN mkdir -p /ml/src

WORKDIR /ml/src

COPY requirements.txt /ml/src
RUN pip install --no-cache-dir -r requirements.txt

COPY serve.py /ml/src/app
COPY Dataset_N.csv /ml/src/app

ENV APP_ENV production

EXPOSE 5000

VOLUME ["/app-data"]

CMD ["python", "serve.py"]
