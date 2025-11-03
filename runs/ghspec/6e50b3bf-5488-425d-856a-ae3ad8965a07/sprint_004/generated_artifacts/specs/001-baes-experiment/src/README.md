# README.md

# Student Management API

## Overview

This project provides API endpoints for managing student enrollments in various courses, including functionality for enrolling students and retrieving their enrolled courses. 

## Migration Steps

### Database Migration

To support the many-to-many relationship between students and courses, a new table `Student_Course` will be introduced in the database schema. This involves the following steps:

1. **Create Migration Script**: 
   - Write a database migration script to create the `Student_Course` table.
   - The table should include the following columns:
     - `student_id`: integer, foreign key referencing `Student`.
     - `course_id`: integer, foreign key referencing `Course`.

2. **Run Migration**:
   - Execute the migration script to alter the existing database schema without affecting the current `Student` and `Course` data.
   - Use a migration tool (like Flask-Migrate) to manage the migration process and ensure that changes are applied correctly.

3. **Verify Migration**:
   - After the migration, verify that the `Student_Course` table is created successfully and that existing data in the `Student` and `Course` tables is preserved.

### Updating Codebase

After performing the migration steps, the following code updates will take place:

1. **Update Models**:
   - Create a model for `StudentCourse` in `models.py` to encapsulate the behavior of the relationship.

2. **Creating API Endpoints**:
   - Implement the following API endpoints in `routes.py`:
     - Enroll a student in a course via `POST /students/{student_id}/courses`.
     - Retrieve a student's enrolled courses via `GET /students/{student_id}/courses`.

3. **Service Logic**:
   - In `services.py`, implement the business logic for enrolling students in courses and fetching their enrolled courses, ensuring proper error handling for non-existent students or courses.

4. **Data Validation**:
   - Add input validation schemas in `schemas.py` for the API requests related to course enrollment.

5. **Testing**:
   - Create unit tests and integration tests in `test_routes.py` and `test_services.py` to thoroughly verify the new functionality and maintain existing tests.

## Running the Application

Follow the instructions in the subsequent sections to set up and run the application locally.

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Up the Environment**:
   - Create a `.env` file based on the `.env.example` and provide necessary configurations.

3. **Run Migrations**:
   - Execute the migration script to ensure the database schema is up to date.

4. **Start the Application**:
   ```bash
   python src/app.py
   ```

## Conclusion

By following these migration steps, we ensure that the application is ready for the extended functionality of managing course enrollments for students. This enhancement allows for greater flexibility in handling student data, paving the way for increased usage of the application.