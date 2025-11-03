import logging
import sys

def setup_logging(log_level=logging.INFO):
    """Set up the logging configuration for the application.

    Args:
        log_level (int): The logging level (default is logging.INFO).
                         It can be set to logging.DEBUG, logging.INFO,
                         logging.WARNING, logging.ERROR, or logging.CRITICAL.
    """
    logging.basicConfig(
        level=log_level,  # Set the logging level
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log message format
        handlers=[
            logging.StreamHandler(sys.stdout),  # Log to standard output
            logging.FileHandler('app.log')  # Log to a file
        ]
    )
    
    # Log the startup message
    logging.info("Logging is set up successfully.")