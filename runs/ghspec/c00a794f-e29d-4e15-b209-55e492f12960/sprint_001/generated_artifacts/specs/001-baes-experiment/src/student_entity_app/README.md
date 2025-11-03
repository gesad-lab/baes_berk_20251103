# Project documentation

# Student Entity Application

This repository is a simple application to manage student entities with a RESTful API interface. It allows for the creation and retrieval of student information.

## Table of Contents
- [Installation Instructions](#installation-instructions)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Examples](#examples)

## Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student_entity_app.git
   cd student_entity_app
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file based on the `.env.example` provided to configure environment variables.

## Usage

To run the application, execute the following command:
```bash
python src/main.py
```

The API will be available at `http://localhost:8000`.

## API Endpoints

### `GET /students`
- **Description**: Retrieves a list of all students.
- **Response**: Returns a JSON array of student objects and a status code of 200.

### `POST /students`
- **Description**: Creates a new student record.
- **Request Body**:
    - `name`: The name of the student.
    - `age`: The age of the student.
    - `email`: The email address of the student.
- **Response**: Returns the created student object and a status code of 201.

## Examples

### Retrieve Students

To retrieve the list of students, you can make a `GET` request to the `/students` endpoint:

```bash
curl -X GET http://localhost:8000/students
```

This will return a non-empty list of students if students have been created.

### Creating a Student

To create a new student, you can make a `POST` request:

```bash
curl -X POST http://localhost:8000/students -H "Content-Type: application/json" -d '{"name": "John Doe", "age": 20, "email": "john.doe@example.com"}'
```

This will create a new student and return the created student object.

## Testing

The application has a suite of tests to ensure the API works as expected. You can find the tests in the `tests` directory.

Run the tests using:

```bash
pytest tests/
```

---

## Success Criteria Check
1. **Student Creation**: Ensure at least one student can be created and verified through API response.
2. **Students Retrieval**: Confirm that querying for students returns a non-empty list when available.
3. **Error Handling**: Validate that errors are returned for improper inputs.
4. **Database Initialization**: Verify automatic creation of database and schema upon application startup.
5. **Python Compatibility**: Confirm that the application runs on Python 3.11+ with no errors.