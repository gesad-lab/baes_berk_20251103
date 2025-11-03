# README.md

# Student Management API

This project provides a simple API for managing students, allowing for the creation and retrieval of student records. It uses Flask and SQLAlchemy for web service and database interaction.

## 1. Setup & Configuration

### Prerequisites

- Python 3.6 or later
- Flask
- Flask SQLAlchemy
- A local database (SQLite is used by default)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables:
   Create a `.env` file based on the provided `.env.example` file, filling in your specific database connection settings and any other necessary configurations.

### Running the Application

To run the Flask application, use the following command:
```bash
flask run
```

## 2. API Documentation

### Create Student
**Endpoint:** `POST /students`  
**Request Body:**
```json
{
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```
**Response:**
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```

### Retrieve Student
**Endpoint:** `GET /students/{id}`  
**Response:**
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```
*or*
```json
{
    "error": {
        "code": "E404",
        "message": "Student not found."
    }
}
```

## 3. Database Migration

To update the existing Student table to include the `email` field, you should create and execute a migration script. 

### Migration Instructions

1. Use Flask-Migrate to manage database migrations. If you haven’t installed Flask-Migrate, include it in your `requirements.txt` and run:
   ```bash
   pip install Flask-Migrate
   ```

2. Initialize the migration repository:
   ```bash
   flask db init
   ```

3. Create a migration script:
   ```bash
   flask db migrate -m "Add email field to Student table"
   ```

4. Apply the migration to the database:
   ```bash
   flask db upgrade
   ```

This migration will add the `email` column to the Student table while preserving existing data.

## 4. Testing

Ensure to run the test suite to validate the implementation. Use the following command:
```bash
pytest
```

## Contribution

For contributions, submit a pull request with a clear description of your changes and any relevant documentation updates. 

## License

This project is licensed under the MIT License - see the LICENSE file for details.