import json
import pendulum
import requests

from airflow import Dataset
from airflow.decorators import dag, task

SRC = Dataset(
    "https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/ytd/12/1880-2022.json"
)
now = pendulum.now()


@dag(start_date=now, schedule="@once", catchup=False)
def etl():
    @task()
    def retrieve(src: Dataset) -> dict:
        resp = requests.get(url=src.uri)
        data = resp.json()
        return data["data"]

    @task()
    def to_fahrenheit(temps: dict[int, float]) -> dict[int, float]:
        ret: dict[int, float] = {}
        for year, celsius in temps.items():
            ret[year] = float(celsius) * 1.8 + 32

        return ret

    @task()
    def load(fahrenheit: dict[int, float]) -> Dataset:
        filename = "/tmp/fahrenheit.json"
        s = json.dumps(fahrenheit)
        f = open(filename, "w")
        f.write(s)
        f.close()

        return Dataset(f"file:///{filename}")

    data = retrieve(SRC)
    fahrenheit = to_fahrenheit(data)
    load(fahrenheit)


etl()
