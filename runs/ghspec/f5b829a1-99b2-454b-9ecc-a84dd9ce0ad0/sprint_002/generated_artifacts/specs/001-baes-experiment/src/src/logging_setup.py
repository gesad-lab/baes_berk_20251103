```python
import logging
import sys
import json

# Configure structured logging settings
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    stream=sys.stdout
)

class StructuredLogger:
    """A structured logger implementation for logging in JSON format."""

    @staticmethod
    def log_info(message: str, **kwargs) -> None:
        """Log an info message with additional context.

        Args:
            message (str): The message to log.
            **kwargs: Optional additional context to include in the log.
        """
        log_entry = {
            'level': 'INFO',
            'message': message,
            **kwargs
        }
        print(json.dumps(log_entry))

    @staticmethod
    def log_error(message: str, **kwargs) -> None:
        """Log an error message with additional context.

        Args:
            message (str): The message to log.
            **kwargs: Optional additional context to include in the log.
        """
        log_entry = {
            'level': 'ERROR',
            'message': message,
            **kwargs
        }
        print(json.dumps(log_entry))

    @staticmethod
    def log_warning(message: str, **kwargs) -> None:
        """Log a warning message with additional context.

        Args:
            message (str): The message to log.
            **kwargs: Optional additional context to include in the log.
        """
        log_entry = {
            'level': 'WARNING',
            'message': message,
            **kwargs
        }
        print(json.dumps(log_entry))

# Example usage within an application context
if __name__ == "__main__":
    logger = StructuredLogger()
    logger.log_info("Application starting...", context={"module": "main"})
    # Add more logging as needed through the application lifecycle
```