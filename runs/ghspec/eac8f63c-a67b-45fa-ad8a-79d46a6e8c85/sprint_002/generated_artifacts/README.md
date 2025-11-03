# README.md

# Student Management System

## Overview

This project is designed to manage student records efficiently. The system allows for the addition, retrieval, update, and deletion of student information seamlessly, ensuring data integrity and smooth interaction via a RESTful API.

## Features

- Add new students with details such as name, age, and email.
- Retrieve student details.
- Update existing student information.
- Delete student records.
- Email validation for student records.

## Requirements

To install the necessary dependencies, use the following command:

```bash
pip install -r requirements.txt
```

## Database Setup

This application uses SQLite for development and testing. Ensure you have a database set up as per the configuration in the `config.py` file. For migrations, we use Alembic to manage the database schema changes.

### Running Migrations

To add the new `email` field to the Student model, run:

```bash
alembic upgrade head
```

## API Endpoints

### Create Student

- **POST /students**
  
  To create a new student, send a JSON body with the following attributes:

  ```json
  {
      "name": "John Doe",
      "age": 20,
      "email": "john.doe@example.com"
  }
  ```

  - **Success Response**: Returns the created student with a 201 status code.
  - **Error Response**: A 400 status code if the email is missing or in an invalid format.

### Get Student

- **GET /students/{id}**

  Retrieve the details of a specific student by their ID.

### Update Student

- **PUT /students/{id}**
  
  To update an existing student's details.

### Delete Student

- **DELETE /students/{id}**

  To remove a student from the records.

## Testing

To ensure the functionality and integrity of the code, the project includes unit tests housed under the `tests/` directory. 

Run the tests using:

```bash
pytest
```

This will execute all tests including those for handling the new email feature.

### Test Cases for Email

The test suite has been extended to include cases testing the addition of students with email and the validation logic to ensure proper error responses are returned when email is missing or improperly formatted.

## Contribution

To contribute to this project, please fork the repository and create a pull request. Ensure to adhere to the coding standards and include unit tests for any new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Ensure that any further modifications to the project or its structure are documented clearly to maintain an efficient workflow and collaborative development.