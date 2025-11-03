# Student Management Web Application

## Overview

The Student Management Web Application allows Admin Users to efficiently create and retrieve student records. The application validates user inputs and handles errors gracefully, ensuring a robust user experience.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Error Handling](#error-handling)
- [Testing](#testing)
- [License](#license)

## Features

1. **Student Entity Creation**: Admin Users can create new student records with a required name field.
2. **Retrieval of Student Records**: Admin Users can fetch all student records in a JSON format.
3. **Error Handling**: The application provides meaningful error messages for invalid inputs.
4. **Automatic Database Schema Creation**: The SQLite database schema is automatically created upon application startup.

## Project Structure

```
student_management/
├── src/
│   ├── app.py               # Main application file
│   ├── models.py            # ORM/Entity definitions
│   ├── routes.py            # API endpoint definitions
│   ├── services.py          # Business logic
│   └── db.py                # Database management
├── tests/
│   ├── test_routes.py       # API tests
│   └── test_services.py     # Business logic tests
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.11+
- Virtual environment (recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd student_management
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To start the application, run:

```bash
python src/app.py
```

The application will automatically create the database schema on startup.

## API Endpoints

### Create a Student Record

- **POST** `/student`
    - Body: 
      ```json
      {
          "name": "John Doe"
      }
      ```
    - Returns: 
      ```json
      {
          "message": "Student record created successfully."
      }
      ```

### Retrieve Student Records

- **GET** `/students`
    - Returns: 
      ```json
      [
          {
              "id": 1,
              "name": "John Doe"
          },
          ...
      ]
      ```

## Error Handling

The application provides structured error messages in JSON format. For example, submitting an empty name will return:

```json
{
    "error": {
        "code": "E001",
        "message": "Name field cannot be empty."
    }
}
```

## Testing

Automated tests are included to verify functionality. To run the tests, execute:

```bash
pytest
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.