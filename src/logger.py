import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y%m%d%H%M%S')}.log"
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(os.path.dirname(log_path), exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(filename=log_path, level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")


if __name__ == "__main__":
    logging.info("Login Started!!!")
    