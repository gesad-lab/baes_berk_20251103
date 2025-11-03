```python
import os
from dotenv import load_dotenv

# Load environment variables from a .env file if it exists
load_dotenv()

# Define a function to get required environment variables with validation
def get_env_variable(var_name: str) -> str:
    """Fetches the environment variable value and validates its presence.

    Args:
        var_name (str): The name of the environment variable to fetch.

    Raises:
        EnvironmentError: If the variable is not set or is empty.

    Returns:
        str: The value of the environment variable.
    """
    value = os.getenv(var_name)
    if value is None or value.strip() == '':
        raise EnvironmentError(f"Environment variable '{var_name}' must be set and not empty.")
    return value

# Fetching required configuration variables
DATABASE_URL = get_env_variable("DATABASE_URL")
SECRET_KEY = get_env_variable("SECRET_KEY")

# Here you can define additional environment variables required for your application
# if needed, following the same pattern of getting and validating the variable.

# Configuration for SQLAlchemy or other relevant setup can follow
# ...

# Example usage (to be implemented in the application where needed):
# print(f"Connecting to database at: {DATABASE_URL}")
# print(f"Using secret key: {SECRET_KEY}")

```