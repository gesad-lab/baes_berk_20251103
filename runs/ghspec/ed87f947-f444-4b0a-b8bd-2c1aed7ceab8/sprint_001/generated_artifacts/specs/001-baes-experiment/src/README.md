# Project Title

## Overview

This project provides a RESTful API built with FastAPI, allowing users to interact with the application easily. It is designed for environments that support Python 3.11 or higher and incorporates SQLite for data management.

## Requirements

- Python 3.11+
- FastAPI
- SQLAlchemy
- Logging
- Pytest for testing

## Environment Variables

To run this application, you will need to configure the following environment variables. These variables are essential for the application to function properly in different deployment environments.

| Environment Variable | Description                            | Default Value  |
|----------------------|----------------------------------------|-----------------|
| `DATABASE_URL`       | The URL for connecting to the SQLite database. Typically, it’ll be like `sqlite:///./database.db`. | `sqlite:///./database.db` |
| `LOG_LEVEL`          | The logging level for the application. Options are `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`. | `INFO`          |
| `API_PREFIX`         | A prefix for all API routes. E.g., `/api/v1`. This helps with versioning and organization. | `/api`          |

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://your-repo-url.git
   cd your-repo-name
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file to specify the required environment variables, or set them in your environment manually according to the table above.

5. **Run the application:**
   ```bash
   uvicorn src.main:app --reload
   ```

6. **Access the API documentation:**
   Open your browser and go to `http://127.0.0.1:8000/docs` to see the automatically generated API documentation.

## Testing

Run tests using the following command:
```bash
pytest
```

Ensure all tests pass before deploying to production.