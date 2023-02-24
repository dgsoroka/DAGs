FROM python:alpine3.10

COPY . /airflow
WORKDIR /airflow

ENV AIRFLOW_HOME=/airflow
RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev

RUN pip3 install --upgrade pip

RUN python3 -m pip install --no-use-pep517 cryptography

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENTRYPOINT airflow standalone

CMD echo cat standalone_admin_password.txt

VOLUME /airflow
