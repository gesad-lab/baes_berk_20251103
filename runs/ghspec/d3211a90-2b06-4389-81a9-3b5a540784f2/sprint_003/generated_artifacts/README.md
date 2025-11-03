# README.md

# Project Title

## Overview

This project is a web application that allows users to create and manage courses, including features for creating and retrieving course details.

## Required Packages

To run this application, you will need the following packages:

- **Flask**: A lightweight WSGI web application framework.
- **Flask-SQLAlchemy**: An extension for Flask that adds support for SQLAlchemy, an ORM for managing databases.
- **Flask-Migrate**: An extension that handles SQLAlchemy database migrations for Flask applications.
- **pytest**: A testing framework for Python.

## Installation

To install the required packages, you can use pip. It is recommended to create a virtual environment before installation.

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install the required packages
pip install Flask Flask-SQLAlchemy Flask-Migrate pytest
```

## Usage

After installing the required packages, you can run the application using:

```bash
flask run
```

Make sure to set the `FLASK_APP` environment variable to the main application file.

## API Endpoints

### Create Course

- **Endpoint**: `POST /courses`
- **Request Body**: 
```json
{
  "name": "Introduction to Programming",
  "level": "Beginner"
}
```
- **Responses**:
  - Success (201 Created):
    ```json
    {
      "id": 1,
      "name": "Introduction to Programming",
      "level": "Beginner"
    }
    ```
  - Error (400 Bad Request for missing fields):
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Both name and level fields are required."
      }
    }
    ```

### Retrieve Course

- **Endpoint**: `GET /courses/<id>`
- **Responses**:
  - Success (200 OK):
    ```json
    {
      "name": "Introduction to Programming",
      "level": "Beginner"
    }
    ```

## Running Tests

To run the tests, you can use pytest:

```bash
pytest
```

This will execute all the test cases in the `tests/` directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.