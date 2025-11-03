# README.md

# Student Management System

A simple application for managing student records using FastAPI and a SQLite database.

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd student_management
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the FastAPI application, execute:

```bash
uvicorn src.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## API Documentation

Auto-generated API documentation is available at `http://127.0.0.1:8000/docs`.

## Testing

To run the tests, use:

```bash
pytest
```

## Environment Variables

Create a `.env` file based on the `.env.example`.

## Additional Notes

- Ensure that you have Python 3.7 or higher installed.
- For any issues or feature requests, please open an issue on this repository.