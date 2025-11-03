import logging
import sys
import json

# Configure structured logging
class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_obj = {
            'level': record.levelname,
            'message': record.getMessage(),
            'timestamp': self.formatTime(record, self.datefmt),
            'filename': record.filename,
            'line_number': record.lineno,
            'method_name': record.funcName,
        }
        # If there's an exception, include that as well
        if record.exc_info:
            log_obj['exception'] = self.formatException(record.exc_info)
        return json.dumps(log_obj)


# Set up logger
def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Set global logging level

    # Create console handler and set formatter
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(JSONFormatter())
    
    # Add the handler to the logger
    logger.addHandler(console_handler)

    return logger


# Example usage of the logger
logger = setup_logger(__name__)


def log_api_request(request_method: str, pathname: str, params: dict):
    logger.info(f"API request received", extra={
        'method': request_method,
        'path': pathname,
        'params': params
    })

    
def log_api_error(error_code: str, error_message: str):
    logger.error(f"API error occurred", extra={
        'code': error_code,
        'message': error_message
    })  


def log_general_info(message: str):
    logger.info(message)


def log_warning(message: str):
    logger.warning(message)


def log_debug(message: str):
    logger.debug(message)