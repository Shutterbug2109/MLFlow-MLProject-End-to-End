# logging file

import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" # to set the format of the logs

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log") # logs/running_logs.log
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str, #

    handlers=[
        logging.FileHandler(log_filepath),  # save the logs in the file
        logging.StreamHandler(sys.stdout) # print the logs in the console
    ]
)

logger = logging.getLogger("mlProjectLogger") # create a logger object