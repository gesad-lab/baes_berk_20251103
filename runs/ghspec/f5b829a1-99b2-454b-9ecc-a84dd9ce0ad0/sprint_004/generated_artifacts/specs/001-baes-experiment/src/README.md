# README.md
```
# Project Title

## Setup Development Environment

To set up the development environment for this project, follow these instructions:

### Prerequisites

Ensure you have `Poetry` installed. You can follow the installation instructions from the official [Poetry documentation](https://python-poetry.org/docs/#installation).

### Install Dependencies

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the project dependencies using Poetry:
   ```bash
   poetry install
   ```

### Configure Environment Variables

1. Create a `.env` file in the root of the project if it does not exist. You can start with the template provided:
   ```
   # .env.example
   DATABASE_URL=sqlite:///./test.db  # Example SQLite URL (change as needed)
   ```

2. Update the `.env` file with your specific configuration details.

### Run Migrations

Ensure that the application runs without errors and executes the migration scripts to set up the database. Run the following command to apply any pending migrations:
```bash
poetry run alembic upgrade head
```

### Start the Development Server

You can start the FastAPI development server with the following command:
```bash
poetry run uvicorn src.main:app --reload
```

Your development environment setup is now complete! You can begin working on the application and testing the new API endpoints for enrolling students and retrieving student courses.

### Additional Notes

- The application uses FastAPI as the web framework.
- Ensure your database schema is up to date by running any necessary migrations before testing new features.
- For running tests, use the following command:
  ```bash
  poetry run pytest
  ```
  
This will execute the tests present in the `tests/` directory to ensure everything is functioning as expected.

```
