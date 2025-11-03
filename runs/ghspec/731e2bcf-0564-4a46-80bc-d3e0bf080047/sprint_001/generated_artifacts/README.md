# README.md

# Student Records Management API

## Version: 1.0.0  
**Purpose**: To create a web application for managing student records through an API.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [API Endpoints](#api-endpoints)
5. [Testing](#testing)
6. [License](#license)

---

## Introduction
This project provides a RESTful API for managing student records. Admin users can create new student entries and retrieve a list of stored students. All interactions with the API are via JSON.

## Installation
To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/student-records-api.git
   cd student-records-api
   ```

2. **Set up Docker:**
   Ensure that you have [Docker](https://www.docker.com/get-started) installed on your machine.

3. **Build and run the application using Docker Compose:**
   ```bash
   docker-compose up --build
   ```

4. The API will be accessible at `http://localhost:8000`.

## Usage
The API allows you to manage student records with two main endpoints:

### Creating a Student
To add a new student, send a `POST` request to `/students` with a JSON body containing the student's name.

**Request:**
```http
POST /students
Content-Type: application/json

{
  "name": "John Doe"
}
```

**Response:**
- **201 Created**
- Returns the created student record in JSON format:
```json
{
  "id": 1,
  "name": "John Doe"
}
```

### Retrieving Student Records
To retrieve all student records, send a `GET` request to `/students`.

**Request:**
```http
GET /students
```

**Response:**
- **200 OK**
- Returns an array of student records in JSON format:
```json
[
  {
    "id": 1,
    "name": "John Doe"
  },
  {
    "id": 2,
    "name": "Jane Smith"
  }
]
```
- If no students exist, returns an empty array `[]`.

## API Endpoints
The API supports the following endpoints:

- `POST /students`: Create a new student.
- `GET /students`: Retrieve all student records.

## Testing
Ensure the functionality of creating and retrieving students by running the included tests. These tests validate the core functionalities:
1. Valid name input should create the student successfully.
2. Empty name input returns an error message indicating the field is required.
3. When there are students in the database, a list of students should be returned.
4. If no students exist, an empty list should be returned.

Run the tests with:
```bash
pytest
```

## License
This project is open source and available under the [MIT License](LICENSE).