import logging

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,  # Log everything at INFO level and above
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('api_requests.log'),  # Log to a file
        logging.StreamHandler()  # Also log to console
    ]
)

def log_request(endpoint: str, method: str, payload: dict, status_code: int):
    """
    Log details of an API request.

    Parameters:
        endpoint (str): The API endpoint being accessed.
        method (str): The HTTP method used (GET, POST, etc.).
        payload (dict): The payload of the request.
        status_code (int): The HTTP status code returned by the request.
    """
    # Log the request details
    logging.info("Request to %s with method %s returned status %d. Payload: %s", 
                 endpoint, method, status_code, payload)

# Example usage in an API endpoint (adjust according to your framework)
# def create_student(request):
#     # Extract necessary data from the request
#     payload = request.json()  # Assume FAST API or similar
#     # Process the request...
#     response_status = 201  # or whatever is appropriate
#     log_request('/students', 'POST', payload, response_status)