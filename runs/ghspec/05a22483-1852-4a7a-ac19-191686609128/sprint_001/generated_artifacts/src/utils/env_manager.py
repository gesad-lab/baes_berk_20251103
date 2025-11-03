import os
from dotenv import load_dotenv

class EnvManager:
    """Handles environment variable management for the application."""
    
    def __init__(self):
        """Load environment variables from a .env file."""
        self.load_env_variables()

    def load_env_variables(self):
        """Load environment variables from a .env file."""
        load_dotenv()
        # Validate required environment variables
        self.validate_env_variable("DATABASE_URL")
        self.validate_env_variable("FLASK_ENV")

    def validate_env_variable(self, var_name: str):
        """Validate that the specified environment variable is set.

        Args:
            var_name (str): The name of the environment variable to validate.

        Raises:
            ValueError: If the environment variable is not set.
        """
        if not os.getenv(var_name):
            raise ValueError(f"{var_name} must be set in the environment.")

    def get_database_url(self) -> str:
        """Get the database URL from the environment.

        Returns:
            str: The database URL.
        """
        return os.getenv("DATABASE_URL")

    def get_flask_env(self) -> str:
        """Get the Flask environment from the environment.

        Returns:
            str: The value of the Flask environment variable.
        """
        return os.getenv("FLASK_ENV")

# Example usage:
# env_manager = EnvManager()
# database_url = env_manager.get_database_url()
# flask_env = env_manager.get_flask_env()