import logging
import json
import os

class CustomJsonFormatter(logging.Formatter):
    """Custom JSON Formatter for structured logging."""
    
    def format(self, record):
        # Create a dictionary to hold log details
        log_entry = {
            "level": record.levelname,
            "message": record.getMessage(),
            "timestamp": self.formatTime(record, self.datefmt),
            "name": record.name,
            "pathname": record.pathname,
            "lineno": record.lineno,
        }
        # If there's an exception, add it to the log entry
        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_entry)

def setup_logging():
    """Setup logging configuration with structured JSON logging."""
    
    logging_level = os.getenv("LOGGING_LEVEL", "DEBUG").upper()

    # Create a logger
    logger = logging.getLogger("api_logger")
    logger.setLevel(logging_level)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging_level)

    # Set formatter for the handler
    formatter = CustomJsonFormatter()
    console_handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(console_handler)

    # Log the startup event
    logger.info("Logging initialized with level: %s", logging_level)

# Call setup_logging() when the application starts
setup_logging()