FROM python:3.13-slim

# manually set cache dir to /tmp to prevent permission issues
ENV RUFF_CACHE_DIR=/tmp/ruff_cache

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && pip install --editable .

USER 1000

ENTRYPOINT ["python", "-m", "ili2py.cli"]
