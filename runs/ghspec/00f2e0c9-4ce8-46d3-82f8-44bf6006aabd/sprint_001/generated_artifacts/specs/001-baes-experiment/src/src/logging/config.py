```python
import os

# Load environment variables from .env file
from dotenv import load_dotenv

load_dotenv()

# Required Environment Variables
# DATABASE_URL: The SQLite database URL for storing student records.
# This should point to a valid file path (e.g., sqlite:///path/to/database.db).
DATABASE_URL = os.getenv('DATABASE_URL')

# Ensure that required environment variables are set
if DATABASE_URL is None:
    raise ValueError("Missing required environment variable: DATABASE_URL")
```