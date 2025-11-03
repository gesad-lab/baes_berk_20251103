import logging
import json
import sys


class StructuredLogger:
    """A logger that formats log entries in JSON for structured logging."""
    
    def __init__(self, name: str):
        # Configure the logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # Create console handler and set level
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)

        # Create formatter for JSON logging
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        ch.setFormatter(formatter)
        
        # Add the handler to the logger
        self.logger.addHandler(ch)

    def log_error(self, message: str, **kwargs):
        """Logs an error message with structured context."""
        log_entry = {
            "level": "ERROR",
            "message": message,
            **kwargs
        }
        self.logger.error(json.dumps(log_entry))

    def log_info(self, message: str, **kwargs):
        """Logs an info message with structured context."""
        log_entry = {
            "level": "INFO",
            "message": message,
            **kwargs
        }
        self.logger.info(json.dumps(log_entry))

    def log_debug(self, message: str, **kwargs):
        """Logs a debug message with structured context."""
        log_entry = {
            "level": "DEBUG",
            "message": message,
            **kwargs
        }
        self.logger.debug(json.dumps(log_entry))


# Example usage:
if __name__ == "__main__":
    logger = StructuredLogger("student_management")
    
    # Log an info message
    logger.log_info("Application started")
    
    # Log an error with details
    logger.log_error("Failed to connect to the database", details={"error": "Connection timeout", "db": "sqlite:///students.db"})