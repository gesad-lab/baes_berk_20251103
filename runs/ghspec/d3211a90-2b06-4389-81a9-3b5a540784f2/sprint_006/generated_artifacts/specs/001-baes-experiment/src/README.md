# README.md

# Project Title

## Overview

This project manages courses and teachers, allowing for the assignment of teachers to courses, retrieval of course details, and the management of course and teacher data.

## Features

### Course-Teacher Relationship

This feature allows for a many-to-one relationship between courses and teachers. Here are the key functionalities related to this feature:

1. **Assign a Teacher to a Course**:
   - Users can select a Course and assign a Teacher through the web application.
   - **Expected Outcome**: The application successfully updates the Course record to include the selected Teacher and returns a confirmation message.

2. **Retrieve Course with Teacher Information**:
   - Users can request to view details of a specific Course, including the associated Teacher information.
   - **Expected Outcome**: The application returns the Course details with the Teacher's name included in the response in JSON format.

3. **Validate Course Updates**:
   - Users attempting to assign a Teacher to a Course that does not exist will receive an appropriate error message.
   - **Expected Outcome**: The application responds with an error message stating that the specified Course was not found.

4. **Multiple Courses for a Teacher**:
   - Users can check how many Courses are associated with a specific Teacher.
   - **Expected Outcome**: The application returns a list of Courses linked to that Teacher, confirming the many-to-one relationship.

## Functional Requirements

### Course Modification
- The application allows users to assign a Teacher to an existing Course entity.
- Each Course can only have one Teacher associated with it.

### Retrieve Course Details with Teacher Association
- Users can retrieve detailed Course information, including the associated Teacher.
- The response format is a JSON object containing the Course's details and the Teacher's name.

### Database Schema Update
- The existing Course table has been updated to include a new foreign key field referencing the Teacher entity.
- A database migration has been executed to add the foreign key without disrupting the existing data.

### JSON Response Format
- All API responses concerning Course updates and retrieval are in valid JSON format.

## API Endpoints

- `PUT /courses/<course_id>`: Assign a Teacher to a Course.
- `GET /courses/<course_id>`: Retrieve details of a specific Course, including the associated Teacher.

## Getting Started

1. Clone the repository
2. Install the necessary dependencies (see requirements.txt)
3. Configure your environment variables
4. Run the application

For detailed instructions on each step, refer to the relevant sections in this README.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.