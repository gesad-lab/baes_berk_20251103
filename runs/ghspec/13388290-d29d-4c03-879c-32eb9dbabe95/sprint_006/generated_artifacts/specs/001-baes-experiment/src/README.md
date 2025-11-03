# README.md

# Project Title

## Overview
This application manages a learning platform that includes Courses and Teachers. 

## Database Migration
To establish a relationship between the Course entity and the Teacher entity, the following changes will be made to the database schema:

- **Updated Database Schema**:
  - **Table**: `courses`
    - **Columns**:
      - Existing attributes (retained)
      - `teacher_id`: INTEGER (nullable, foreign key referencing the `teachers` table)

The migration ensures that the existing Student and Course data remains intact.

## Features

### Assign Teacher to Course
- **API Endpoint**: `POST /courses/{course_id}/assign-teacher/{teacher_id}`
  - Assigns a Teacher to an existing Course.
  - Requires both `course_id` and `teacher_id` to be valid.
  - Returns confirmation of the assignment.

### Retrieve Course Details
- **API Endpoint**: `GET /courses/{course_id}`
  - Retrieves all details of a specific Course, including the assigned Teacher’s details.

## Setup Instructions
1. **Initial Setup**: Follow instructions in the setup section to configure your local environment.
2. **Database Migration**: Run the migration script to update the database schema before starting the application.
3. **Feature Usage**:
   - To assign a teacher to a course, make a POST request to the `/assign-teacher` endpoint with valid IDs.
   - To retrieve a course's details, make a GET request to the `/courses/{course_id}` endpoint.

## Success Criteria
- The database schema will include a `teacher_id` foreign key in the `courses` table post-migration without affecting existing Student and Course data.
- Users will be able to successfully assign a Teacher to a Course and retrieve Course details with the Teacher's information accurately represented.
- Attempts to assign a Teacher with an invalid Course or Teacher ID will result in appropriate validation error messages.

## Conclusion
This update enhances the course management capabilities by integrating a relationship with teachers. Follow the setup instructions for a smooth migration and implementation of new features.