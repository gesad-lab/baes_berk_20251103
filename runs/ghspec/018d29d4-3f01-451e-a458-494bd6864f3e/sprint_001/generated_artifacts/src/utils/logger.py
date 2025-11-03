import logging
import sys
from fastapi import Request

# Configuring the structured logger
class StructLogger:
    def __init__(self):
        self.logger = logging.getLogger("StructuredLogger")
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s", '
            '"request_id": "%(request_id)s"}'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_request(self, request: Request):
        """Logs incoming request details."""
        self.logger.info(
            "Incoming request",
            extra={"request_id": request.headers.get("X-Request-ID", "N/A")}
        )

    def log_response(self, response: dict):
        """Logs response details."""
        self.logger.info(
            "Outgoing response",
            extra={"request_id": response.get("request_id", "N/A")}
        )

    def log_error(self, message: str, error: Exception):
        """Logs error details."""
        self.logger.error(
            message,
            extra={"request_id": getattr(error, 'request_id', 'N/A')}
        )

logger = StructLogger()