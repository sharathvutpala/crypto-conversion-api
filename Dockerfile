# pull official base image
FROM python:3.9.10-alpine3.14

# set work directory
WORKDIR /code

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# install dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
        libressl-dev libffi-dev gcc musl-dev python3-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /code/requirements.txt
# copy project
COPY api/ /code/api
COPY tests/ /code/tests

EXPOSE 8000

#CMD ["sleep", "3600"]
CMD  /usr/local/bin/uvicorn api.currency:app --reload --port 8000 --host 0.0.0.0 --log-level debug --workers 1
