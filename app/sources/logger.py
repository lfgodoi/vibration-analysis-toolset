# Importing packages
import logging.handlers as handlers
import logging
import os
import datetime
import pytz

# Dictionary to store the log instances globally
loggers = {}

# Class to overwrite 'logging.Formatter'
class Formatter(logging.Formatter):

    # Converter
    def converter(self, timestamp):
        dt = datetime.datetime.fromtimestamp(timestamp, tz=pytz.UTC)
        return dt.astimezone(pytz.timezone("America/Sao_Paulo"))
    
    # Time formatter
    def formatTime(self, record, datefmt=None):
        dt = self.converter(record.created)
        if datefmt:
            s = dt.strftime(datefmt)
        else:
            try:
                s = dt.isoformat(timespec="milliseconds")
            except TypeError:
                s = dt.isoformat()
        return s
    
# Function to create a logger object
def set_logger(ref):

    # Creating the log folder if it does not exist
    path = "../logs"
    if not os.path.exists(path):
        os.makedirs(path)
    
    # Checking whether a logger instance already exists
    global loggers
    if loggers.get(ref):
        return loggers.get(ref)
    
    # Instantiating the logger if it does not exists
    else:

        # Creating the logger object
        logger = logging.getLogger(ref)
        logger.setLevel(logging.INFO)

        # Formatting the log file
        formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")
        log_handler = handlers.RotatingFileHandler(f"{path}/logs.log", maxBytes=500000, backupCount=0)
        log_handler.setFormatter(formatter)
        logger.addHandler(log_handler)
        loggers[ref] = logger

    return logger