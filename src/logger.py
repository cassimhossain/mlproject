import logging
import os
from datetime import datetime

# Clear any existing handlers (important in interactive environments)
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Logs folder
logs_dir = os.path.join(os.getcwd(), "Logs")
os.makedirs(logs_dir, exist_ok=True)

# Log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

