FROM python:3.13-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && pip install --editable .

USER 1000

ENTRYPOINT ["python", "-m", "ili2py.cli"]
