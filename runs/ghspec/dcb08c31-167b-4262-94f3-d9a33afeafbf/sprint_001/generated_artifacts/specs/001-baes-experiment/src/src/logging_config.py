import logging
import sys

def setup_logging() -> None:
    """Set up structured logging configuration for the application."""
    # Create a logger instance
    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.DEBUG)  # Set the log level to DEBUG for detailed logging

    # Create a console handler that outputs logs to stdout
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)

    # Define a formatter for structured logging in JSON format
    formatter = logging.Formatter(
        '{"timestamp": "%(asctime)s", '
        '"level": "%(levelname)s", '
        '"name": "%(name)s", '
        '"message": "%(message)s"}'
    )

    # Set the formatter for the console handler
    console_handler.setFormatter(formatter)

    # Add the console handler to the logger
    logger.addHandler(console_handler)

    # Log application start message
    logger.info("Logging configured successfully.")

# Call the logging setup function when this module is imported
setup_logging()