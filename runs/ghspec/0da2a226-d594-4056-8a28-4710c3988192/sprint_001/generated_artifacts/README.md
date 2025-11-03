# README.md

# Student Management API

This project is a simple Student Management API that allows you to create, retrieve, update, and delete student records. It is built using Python, SQLAlchemy for ORM, and Pydantic for input validation and request handling.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [API Endpoints](#api-endpoints)
- [Run the Application](#run-the-application)
- [Running Tests](#running-tests)
- [License](#license)

## Features

- Create new student records
- Retrieve a student by ID
- Update an existing student’s name
- Delete a student record
- Input validation using Pydantic

## Requirements

- Python 3.7+
- SQLite
- Flask
- SQLAlchemy
- Pydantic
- pytest

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://your-repo-url.git
   cd student-management-api
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   The application will automatically create the necessary SQLite database and tables on startup.

## API Endpoints

### Create a Student

- **Endpoint:** `POST /students`
- **Request Body:**
  ```json
  {
    "name": "John Doe"
  }
  ```
- **Response:**
  - **201 Created**
  - **Body:**
  ```json
  {
    "id": 1,
    "name": "John Doe"
  }
  ```

### Retrieve a Student

- **Endpoint:** `GET /students/{id}`
- **Response:**
  - **200 OK**
  - **Body:**
  ```json
  {
    "id": 1,
    "name": "John Doe"
  }
  ```

### Update a Student

- **Endpoint:** `PUT /students/{id}`
- **Request Body:**
  ```json
  {
    "name": "Jane Doe"
  }
  ```
- **Response:**
  - **200 OK**
  - **Body:**
  ```json
  {
    "id": 1,
    "name": "Jane Doe"
  }
  ```

### Delete a Student

- **Endpoint:** `DELETE /students/{id}`
- **Response:**
  - **204 No Content**

## Run the Application

To start the application, run the following command:

```bash
flask run
```

Make sure to have the `FLASK_APP` environment variable set to the main application file.

## Running Tests

To run the tests, execute the following command:

```bash
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.