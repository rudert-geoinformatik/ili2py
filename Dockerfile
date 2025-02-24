FROM python:3.13-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && pip install .

ENTRYPOINT ["python", "-m", "ili2py.cli"]

# Default command to run when starting the container (example from README.md)
CMD ["ili2py-python-classes", "-i", "data/OeREBKRMtrsfr_V2_0.imd", "-f", "generated"]
