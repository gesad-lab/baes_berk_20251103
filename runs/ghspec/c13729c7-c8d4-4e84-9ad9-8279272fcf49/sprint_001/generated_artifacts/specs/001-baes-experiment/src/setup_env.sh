```bash
#!/bin/bash

# .env.example template for environment variables
# Copy this file to .env and fill in the required values.

# Database configuration
# DATABASE_URL: The URL for connecting to the SQLite database
# Format: sqlite:///./database.db
DATABASE_URL=""

# API configuration
# API_HOST: The host for the FastAPI application
# Format: "localhost" for local development
API_HOST=""

# API_PORT: The port for the FastAPI application
# Default: 8000
API_PORT="8000"

# Logging configuration
# LOG_LEVEL: The logging level for the application (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_LEVEL="INFO"

# Additional environment variables can be added below as needed
```