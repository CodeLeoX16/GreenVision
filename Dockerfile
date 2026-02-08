FROM python:3.8.5-slim-buster

WORKDIR /app
COPY . /app

RUN python -m pip install --upgrade pip && \
    pip install "urllib3<2" && \
    pip install -r requrements.txt

CMD ["python3", "app.py"]
