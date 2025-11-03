```bash
#!/bin/bash

# Verify Environment Setup for FastAPI and SQLAlchemy with Alembic

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check for FastAPI installation
if ! command_exists pip; then
    echo "Error: pip is not installed. Please install pip to proceed."
    exit 1
fi

if ! python -c "import fastapi" >/dev/null 2>&1; then
    echo "Error: FastAPI is not installed. Please install FastAPI using 'pip install fastapi'."
    exit 1
fi

# Check for SQLAlchemy installation
if ! python -c "import sqlalchemy" >/dev/null 2>&1; then
    echo "Error: SQLAlchemy is not installed. Please install SQLAlchemy using 'pip install sqlalchemy'."
    exit 1
fi

# Check for Alembic installation
if ! python -c "import alembic" >/dev/null 2>&1; then
    echo "Error: Alembic is not installed. Please install Alembic using 'pip install alembic'."
    exit 1
fi

echo "Environment Setup verified: FastAPI, SQLAlchemy, and Alembic are installed."

# Run database migrations to ensure the latest schema is applied
echo "Applying database migrations..."
alembic upgrade head
if [ $? -ne 0 ]; then
    echo "Error: Failed to run database migrations. Please check your Alembic configuration."
    exit 1
fi

echo "Database migrations applied successfully."
```