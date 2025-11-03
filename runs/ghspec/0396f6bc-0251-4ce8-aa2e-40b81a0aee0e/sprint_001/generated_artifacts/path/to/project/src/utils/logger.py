import logging
import sys

# Configure the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set the threshold for the logger

# Create console handler and set level to debug
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add formatter to the console handler
ch.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(ch)

def log_info(message: str) -> None:
    """
    Log an informational message.
    
    Args:
        message (str): The message to log as informational.
    """
    logger.info(message)

def log_warning(message: str) -> None:
    """
    Log a warning message.
    
    Args:
        message (str): The message to log as a warning.
    """
    logger.warning(message)

def log_error(message: str) -> None:
    """
    Log an error message.
    
    Args:
        message (str): The message to log as an error.
    """
    logger.error(message)

def log_critical(message: str) -> None:
    """
    Log a critical error message.
    
    Args:
        message (str): The message to log as critical.
    """
    logger.critical(message)

# Example usage of logging functions:
if __name__ == "__main__":
    log_info("Logger is configured and ready to use.")
    log_warning("This is a warning message.")
    log_error("This is an error message.")
    log_critical("This is a critical error message.")