# README.md

# Student Management System

This project is a Student Management System designed to handle student information, including personal details and academic records. The application uses a RESTful API architecture.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Development Steps](#development-steps)
4. [API Endpoints](#api-endpoints)

## Installation

To set up the project, clone the repository and install the required packages.

```bash
git clone https://github.com/yourusername/student_management.git
cd student_management
pip install -r requirements.txt
```

## Usage

To start the application, run:

```bash
python src/app.py
```

### Student Creation

You can create a new student by making a POST request to the `/students` endpoint with the following required fields:

- `name`: The name of the student (string).
- `email`: The email address of the student (string, must be a valid format).

**Example Request:**

```bash
curl -X POST http://localhost:5000/students \
-H "Content-Type: application/json" \
-d '{"name": "John Doe", "email": "john.doe@example.com"}'
```

### Student Retrieval

To retrieve a student's information, send a GET request to the `/students/{id}` endpoint, where `{id}` is the unique identifier of the student.

**Example Request:**

```bash
curl -X GET http://localhost:5000/students/1
```

## Development Steps

1. **Database Migration**: Update the database schema using SQLAlchemy migration to add the `email` column.
2. **Update Models**: Modify `models.py` to include the `email` field in the `Student` model.
3. **Updating Routes**: Modify `routes.py` to include validation for the new email field during the creation of a student.
4. **Service Logic**: Update corresponding functionalities in `services.py` to handle the email during student creation and retrieval.
5. **Data Validation**: Update validation schemas in `schemas.py` to ensure that email is a required field with a valid format.
6. **Testing**: Add unit tests and integration tests for the new functionality in `test_routes.py` and `test_services.py` to ensure proper error handling.
7. **Documentation**: Update this `README.md` to include usage examples for the new fields in student creation and retrieval.

## API Endpoints

- **POST /students**: Create a new student.
- **GET /students/{id}**: Retrieve a student by ID.
- **PUT /students/{id}**: Update a student's information.
- **DELETE /students/{id}**: Remove a student from the system.

## License

MIT License. See LICENSE for details.