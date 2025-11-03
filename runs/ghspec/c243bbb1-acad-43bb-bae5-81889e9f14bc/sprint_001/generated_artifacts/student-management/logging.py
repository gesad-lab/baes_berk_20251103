import logging

# Configure the logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format='%(asctime)s - %(levelname)s - %(message)s',  # Define the log message format
)

def log_api_call(api_endpoint: str):
    """Log the API call for a given endpoint."""
    logging.info(f"API call made to {api_endpoint}")

def log_error(message: str):
    """Log an error message."""
    logging.error(message)

def log_successful_response(api_endpoint: str, duration: float):
    """Log a successful API response with duration."""
    logging.info(f"API call to {api_endpoint} succeeded, response time: {duration:.2f} ms")

def log_invalid_input(api_endpoint: str, details: str):
    """Log details of invalid input received at an API endpoint."""
    logging.warning(f"Invalid input at {api_endpoint}: {details}")