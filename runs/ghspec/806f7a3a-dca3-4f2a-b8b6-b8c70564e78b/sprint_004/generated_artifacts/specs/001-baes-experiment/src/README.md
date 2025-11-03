# README.md

# Project Title

## Overview

This project is an educational management system designed to manage students, courses, and enrollments. It provides an API for various operations related to these entities, ensuring seamless management capabilities.

## Table of Contents

- [API Documentation](#api-documentation)
- [Enrollment API](#enrollment-api)
- [Database Migrations](#database-migrations)
- [Installation](#installation)
- [Usage](#usage)
- [Contribution](#contribution)

## API Documentation

The API offers endpoints for managing students, courses, and enrollments. Please refer to `/docs/api.md` for detailed documentation on all available endpoints and their respective functional requirements.

### Enrollment API

The enrollment-related API allows users to manage student enrollments in courses efficiently. Below are the key endpoints:

- `POST /api/enrollments`
  - **Description**: Enroll a student in a course.
  - **Request Body**:
    - `student_id`: The ID of the student.
    - `course_id`: The ID of the course.
  - **Response**: Confirmation of enrollment along with the enrollment details.

- `DELETE /api/enrollments`
  - **Description**: Remove a student's enrollment from a course.
  - **Request Body**:
    - `student_id`: The ID of the student.
    - `course_id`: The ID of the course.
  - **Response**: Confirmation of the removal of enrollment.

Make sure to check the response status codes for each endpoint to handle success and error responses appropriately.

## Database Migrations

To manage database schema changes, use Flask-Migrate. Follow these commands to create and apply migration scripts, which include adding a `student_courses` mapping table:

```bash
flask db migrate -m "Added StudentCourses mapping table"
flask db upgrade
```

This ensures existing data remains intact while adding the necessary relationships between students and courses.

## Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set up a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the application, ensure the environment is set up correctly and run:

```bash
flask run
```

## Contribution

Contributions are welcome! Please adhere to the coding standards and ensure any changes are well documented and tested. 

--- 

This `README.md` provides an overview, installation and usage instructions, and specifics about the enrollment API and database migration, paralleling the detailed guidelines indicated in the task requirements.