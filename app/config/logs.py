import logging


def configure_logs():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    if logger.hasHandlers():
        logger.handlers.clear()

    # Formato de logs
    formatter = logging.Formatter(
        "[%(levelname)s] [%(asctime)s] : %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    # Handler para consola
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Configuración de logs de Uvicorn
    uvicorn_logger = logging.getLogger("uvicorn")
    uvicorn_logger.setLevel(logging.DEBUG)
    uvicorn_logger.propagate = False
    uvicorn_logger.handlers.clear()
    uvicorn_logger.addHandler(console_handler)
