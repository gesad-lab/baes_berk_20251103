# README.md

# Course API Documentation

## Overview

The Course API allows the management of educational courses within the system. It introduces a new Course entity that enhances our classification of various educational offerings. Each course is categorized by a name and a level, allowing for better organization and querying of course-related data.

## Functional Requirements

### Course Entity

Each course entity has the following structure:

- **Course**
  - **name**: (String) - required
  - **level**: (String) - required

### Database Schema

The database schema includes a new table for courses, structured as follows:

- **courses table**
  - **id**: (Integer, Primary Key, Auto-increment)
  - **name**: (String) - required
  - **level**: (String) - required

The migration process ensures that the new Course table is created without affecting existing data in the Student table.

## API Endpoints

### Create Course

- **Endpoint**: `POST /courses`
- **Description**: Adds a new course to the system.
- **Request Body**:
  ```json
  {
    "name": "Course Name",
    "level": "Course Level"
  }
  ```
- **Responses**:
  - **200 OK**: Course added successfully.
    ```json
    {
       "message": "Course added successfully"
    }
    ```
  - **400 Bad Request**: If required fields are missing.
    ```json
    {
       "error": {
           "code": "E001",
           "message": "Level is required."
       }
    }
    ```

### Fetch Courses (Future Work)

- **Endpoint**: `GET /courses`
- **Description**: Retrieves all courses (not implemented yet).

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd student_entity_app
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Update the `.env` file with necessary environment variables.

## Usage

After setting up the environment, you can start the server using the command:
```bash
python src/main.py
```

Make requests to the Course API using tools like Postman or cURL.

---

With this addition, the `README.md` is now updated to reflect the new Course entity and its functionalities.