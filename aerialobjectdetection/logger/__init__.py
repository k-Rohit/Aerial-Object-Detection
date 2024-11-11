import logging
import os
from datetime import datetime
from from_root import from_root

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

try:
    log_path = os.path.join(from_root(), 'log', LOG_FILE)
except FileNotFoundError:
    # Fallback to current working directory if root detection fails
    log_path = os.path.join(os.getcwd(), 'log', LOG_FILE)

os.makedirs(os.path.dirname(log_path), exist_ok=True)

logging.basicConfig(
    filename=log_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
