FROM apache/airflow:slim-2.10.4-python3.12
USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
      libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
USER airflow
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt