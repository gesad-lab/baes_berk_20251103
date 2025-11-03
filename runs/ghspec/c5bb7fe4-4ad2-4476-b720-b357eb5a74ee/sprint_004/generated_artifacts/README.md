# Updated README.md

# Project Documentation

## Overview

This project is designed to manage courses and students through a RESTful API structure. This document serves as a guide to the project setup, API endpoints, and database migration procedures.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Flask-SQLAlchemy
- pytest

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/project-name.git
   ```
2. Change into the project directory:
   ```bash
   cd project-name
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Database Setup

To initialize the database, run the following command:

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

## API Endpoints

### Courses

#### Create a Course

- **Endpoint:** `POST /api/v1/courses`
- **Parameters:**
  - `name` (string): The name of the course.
  - `level` (string): The level of the course (e.g., beginner, intermediate, advanced).
  
- **Request Body Example:**
  ```json
  {
    "name": "Introduction to Programming",
    "level": "beginner"
  }
  ```

- **Response:**
  - **201 Created** on success with the created course details.
  - **400 Bad Request** if the input is invalid.

#### Get All Courses

- **Endpoint:** `GET /api/v1/courses`
- **Response:**
  - **200 OK** with an array of courses.

#### Update Course Level

- **Endpoint:** `PATCH /api/v1/courses/<course_id>`
- **Parameters:**
  - `course_id` (integer): The ID of the course to be updated.
- **Request Body Example:**
  ```json
  {
    "level": "intermediate"
  }
  ```

- **Response:**
  - **200 OK** on success with the updated course details.
  - **404 Not Found** if the course ID does not exist.
  
## Migration Commands

To manage migrations during deployment, use the following commands:

1. **Initialization:**
   ```bash
   flask db init
   ```

2. **Creating a Migration:**
   ```bash
   flask db migrate -m "Your migration message here."
   ```

3. **Applying Migrations:**
   ```bash
   flask db upgrade
   ```

### Note
Ensure all API-related functions and modules have appropriate docstrings explaining their functionality for easier maintenance and understanding in the future.

## Testing

To run the tests, use the following command:
```bash
pytest
```

### Helper Functions
Each function within the service and API modules contains docstrings that detail their purpose and usage. Ensure to check these for guidelines on how to properly interact with each API function.

## Conclusion

This README provides an overview of the setup, endpoint structure, and documentation for the course management system. Ensure that you refer back to this document whenever you engage with the API or contribute to the project.