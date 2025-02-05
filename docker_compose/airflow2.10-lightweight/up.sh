#!/bin/bash

# Start base services first
docker compose up -d --build postgres

# If --init flag is passed, run initialization and then start airflow
if [ "$1" == "--init" ]; then
    echo -e "AIRFLOW_UID=$(id -u)" > .env
    echo "Running Airflow initialization..."
    docker compose up --build --force-recreate airflow-init
    docker compose up --build --wait -d airflow-standalone
else
    # Otherwise just start airflow-standalone
    docker compose up --wait -d airflow-standalone
fi