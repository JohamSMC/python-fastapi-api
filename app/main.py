import time
import logging
from datetime import datetime
from fastapi import FastAPI
from app.config.logs import configure_logs

app = FastAPI()

configure_logs()

logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    logger.info("Inicio root path")
    return "Hello World JohamSMC"


@app.get("/time")
def get_time():
    logger.info("Inicio path /time")
    return f"Hello World {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"


@app.get("/sleep/{time_sleep}")
def get_endpoint_sleep(time_sleep: int):
    logger.info("Inicio path /sleep/{time_sleep}")
    start_time = datetime.now()
    logger.info(f"Start time: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    time.sleep(time_sleep)
    end_time = datetime.now()
    logger.info(f"End time  : {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    time_difference = end_time - start_time
    logger.info(f"Duración endPoint : {time_difference.total_seconds()}")
    return f"Duración endPoint : {time_difference.total_seconds()}"
