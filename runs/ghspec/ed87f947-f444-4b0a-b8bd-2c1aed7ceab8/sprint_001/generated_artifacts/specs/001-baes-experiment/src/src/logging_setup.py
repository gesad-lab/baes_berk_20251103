import logging
import sys

def setup_logging(log_level=logging.ERROR):
    """
    Configures the logging for the application.

    Parameters:
    - log_level: The level of logging that is captured (default: logging.ERROR)
    """
    # Set up a basic configuration for the logging system
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),  # Log to standard output
            logging.FileHandler('app_errors.log')  # Log to a file
        ]
    )

    logging.info("Logging is set up. Level: %s", logging.getLevelName(log_level))

# Call the setup_logging function during application startup
setup_logging()