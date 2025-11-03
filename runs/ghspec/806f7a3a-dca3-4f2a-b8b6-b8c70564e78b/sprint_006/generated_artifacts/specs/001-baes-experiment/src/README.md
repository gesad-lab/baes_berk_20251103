# README.md

# Project Title

## Overview

This project implements a course management system that allows administrators to manage courses, students, and teachers. It includes functionality to assign teachers to courses, view course details, and ensure the preservation of existing data during updates.

## User Scenarios & Testing

1. **Assigning a Teacher to a Course**: An administrator selects a teacher and associates them with a specific course. The system successfully updates the course to link the teacher.
   - *Test*: Assign a teacher to a course and verify that the course record shows the correct teacher ID.

2. **Viewing Course Details with Teacher Assignment**: A user requests to see the details of a course, including the assigned teacher's name and email.
   - *Test*: Query a Course by ID and ensure that the returned data includes the teacher's name and email alongside course details.

3. **Preservation of Existing Data**: Upon adding the teacher relationship, the system must ensure that existing data for courses and students remains unaltered.
   - *Test*: Verify that data for all existing courses and students remains intact after the implementation of this relationship.

4. **Removing Teacher Assignment**: An administrator decides to disassociate a teacher from a course. The system should update the course record to remove the teacher link.
   - *Test*: Remove a teacher from a course and check that the course record no longer displays the teacher's ID.

## Functional Requirements

1. **Add Teacher to Course**:
   - An API endpoint must accept a request that allows an administrator to link a Teacher to a Course by updating the Course entity to include a teacher ID.
   - The request must validate that the provided teacher ID corresponds to an existing Teacher record.

2. **Get Course Details**:
   - An API endpoint must retrieve details for a specific Course that includes the related Teacher’s name and email.

3. **Database Migration**:
   - Update the existing Course table to include a new column for the Teacher relationship:
     - Teacher_ID (Integer, Foreign Key referencing Teacher(ID))
   - Ensure that this migration preserves existing Student, Course, and Teacher data during the schema update.

## Success Criteria
- Successful API response codes for all operations related to teacher assignments and course management.

## API Endpoints

### Assign Teacher to Course
- **POST** `/api/v1/courses/<course_id>/assign_teacher`
  - Request Body: `{ "teacher_id": <integer> }`
  - Description: Assign a teacher to a course.

### Get Course Details
- **GET** `/api/v1/courses/<course_id>`
  - Description: Retrieve details of a specific course, including the assigned teacher's information.

### Remove Teacher from Course
- **DELETE** `/api/v1/courses/<course_id>/remove_teacher`
  - Description: Remove the assignment of a teacher from a course.

# Running the Application

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set up the database and run migrations:
   ```
   flask db upgrade
   ```

3. Start the server:
   ```
   flask run
   ```

# Contributing

Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing to this project.

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.