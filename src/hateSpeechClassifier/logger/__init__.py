import logging
import os
from datetime import datetime

LOG_FILENAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_directory = os.path.join(os.getcwd(), "logs")

os.makedirs(logs_directory, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_directory, LOG_FILENAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
