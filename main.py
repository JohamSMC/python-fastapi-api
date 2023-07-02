import time
from typing import Union
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return f"Hello World {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

@app.get("/sleep/{time_sleep}")
def endpoint_sleep(time_sleep: int):
    start_time = datetime.now()
    print(f"start time: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    time.sleep(time_sleep)
    end_time = datetime.now()
    print(f"end time  : {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    time_difference = end_time-start_time
    print(f"Duracion endPoint : {time_difference.total_seconds()}")
    return f"Duracion endPoint : {time_difference.total_seconds()}"
