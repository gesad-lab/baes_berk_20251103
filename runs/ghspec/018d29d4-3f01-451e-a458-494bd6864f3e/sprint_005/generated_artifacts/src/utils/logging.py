```python
import logging
import sys
from fastapi import Request

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s", "request_id": "%(request_id)s"}',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("api_logging")

def log_api_request(request: Request):
    """Logs API request details for structured logging.

    Args:
        request (Request): The FastAPI request object.
    """
    request_data = {
        "method": request.method,
        "url": request.url.path,
        "headers": dict(request.headers),
        "query_params": dict(request.query_params),
    }
    logger.info("API Request received", extra={"request_id": request.headers.get("X-Request-ID", "N/A"), **request_data})

def log_api_error(error_message: str, error_code: str, request_id: str):
    """Logs API errors for structured logging.

    Args:
        error_message (str): A message describing the error.
        error_code (str): A code related to the error.
        request_id (str): The unique request identifier.
    """
    logger.error("API Error occurred", extra={"request_id": request_id, "error_message": error_message, "error_code": error_code})

# Note: The `log_api_request` should be called at the beginning of processing each API endpoint
#       The `log_api_error` should be called within the exception handling portion of the API endpoints
```