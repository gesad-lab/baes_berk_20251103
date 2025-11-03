# README.md

# Course Management API

This repository contains the code for managing courses and their relationships with teachers. The API allows users to create, read, update, and delete courses, as well as associate and dissociate teachers with those courses.

## Table of Contents

- [API Endpoints](#api-endpoints)
- [Course Entity Management](#course-entity-management)
- [Usage](#usage)
- [Testing](#testing)

## API Endpoints

The following endpoints have been implemented to manage courses and teacher relationships:

- **GET /api/v1/courses**
  - Retrieves a list of all courses.
  
- **GET /api/v1/courses/{id}**
  - Retrieves a specific course by ID.
  
- **POST /api/v1/courses**
  - Creates a new course. Expects a JSON body with course details.
  
- **PUT /api/v1/courses/{id}**
  - Updates an existing course. Expects a JSON body with updated course details.

- **DELETE /api/v1/courses/{id}**
  - Deletes a specific course by ID.

- **POST /api/v1/courses/{id}/assign_teacher**
  - Assigns a teacher to a course. Expects a JSON body with `teacher_id`.

- **DELETE /api/v1/courses/{id}/remove_teacher**
  - Removes a teacher from a course.

These endpoints allow applications to effectively manage the relationship between courses and teachers.

## Course Entity Management

### Course Model Updates

The `Course` model has been updated to include a new attribute `teacher_id`. This attribute establishes a relationship back-reference to the `Teacher`, allowing easy access to which teacher is assigned to which course.

### Database Migration

A new migration script has been created to add the `teacher_id` column to the existing `courses` table and enforce a foreign key relationship with the `teachers` table.

## Usage

To set up the project, ensure you have the necessary environment variables configured. You can use the provided `.env.example` as a reference. Then, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your_repo.git
   cd your_repo
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the database migrations:
   ```bash
   alembic upgrade head
   ```

4. Start the server:
   ```bash
   python app.py
   ```

## Testing

To run the tests, make sure that you have all the dependencies installed, and simply execute:

```bash
pytest tests/
```

This will run all the tests included in the `tests` directory.

Make sure to add tests specific to the new endpoints and the updated `Course` model to ensure everything is functioning correctly.

--- 

This README has been updated to reflect the changes made in managing the `Course` entity and the new capabilities for assigning and removing teachers from courses.