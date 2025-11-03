# README.md

# Student Management System

## Overview

The Student Management System is a simple web application designed for managing Student entities. Each Student has a required name field, allowing users to store, retrieve, and manage student data efficiently while ensuring data integrity through automatic database schema creation.

## Purpose

The main purpose of this application is to provide a user-friendly interface for managing student records. It embraces simplicity and lightweight design, which is ideal for educational purposes or small-scale applications.

## Features

- **Add Students**: Easily add new student records via a RESTful API.
- **Retrieve Students**: Fetch existing student records for viewing and management.
- **Data Validation**: Ensure that only valid data is accepted, preventing common input errors.
- **Automatic Database Setup**: The application automatically creates and manages the SQLite database schema upon startup.

## Assumptions

1. Users have valid access to the web application to manage student data.
2. The application will be deployed in an environment where Python 3.11+ is available, along with necessary libraries for running a FastAPI application and SQLite.
3. Data persistence through SQLite is sufficient for the application's intended usage.

## Installation

1. Clone the repository:
   ```bash
   git clone https://your-repo-url/student_management.git
   cd student_management
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment variables by creating a `.env` file based on the `.env.example` provided.

## Running the Application

Run the application using the following command:
```bash
uvicorn src.main:app --reload
```
This command starts the FastAPI application, and it will be accessible at `http://127.0.0.1:8000`.

## API Endpoints

- **POST /students**: Add a new student.
  - Request Body: `{"name": "Student Name"}`
- **GET /students**: Retrieve a list of all students.

## Testing

To run the tests, ensure all dependencies are installed and execute:
```bash
pytest
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.