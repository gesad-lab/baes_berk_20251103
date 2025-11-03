# Feature: Add Course Relationship to Student Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Student and Course entities, allowing each Student to enroll in multiple Courses. This enhancement will improve the educational data model by enabling better tracking of student enrollments, supporting educational insights such as course load and participation. The feature will also facilitate course management processes including enrollment tracking and reporting.

## User Scenarios & Testing
1. **Scenario 1: Enroll a Student in a Course**
   - **Given** a Student exists with a known ID,
   - **When** the user submits a request to enroll the Student in a Course,
   - **Then** the Student's record should be updated to reflect the enrollment in the specified Course.

2. **Scenario 2: Retrieve Courses for a Student**
   - **Given** a Student exists with a known ID,
   - **When** the user requests the courses the Student is enrolled in,
   - **Then** the response should contain a list of Courses associated with the Student.

3. **Scenario 3: Enroll a Student in a Course that does not exist**
   - **Given** a Student exists with a known ID,
   - **When** the user submits a request to enroll the Student in a non-existing Course,
   - **Then** the response should indicate that the specified Course is not found.

4. **Scenario 4: Enroll a Student without specifying a Course**
   - **Given** a Student exists with a known ID,
   - **When** the user submits a request to enroll the Student without providing a Course ID,
   - **Then** the response should indicate that the Course ID is required.

## Functional Requirements
1. The application must include an API endpoint to enroll a Student in a Course with the following:
   - Method: POST
   - Endpoint: `/students/{studentId}/enroll`
   - Request Body: JSON object containing "courseId" (string, required).
   - Response: JSON object indicating success and the updated Student's course list.

2. The application must include an API endpoint to retrieve all Courses for a specific Student with the following:
   - Method: GET
   - Endpoint: `/students/{studentId}/courses`
   - Response: JSON object containing a list of Courses the Student is enrolled in.

3. The application must update the database schema to establish a many-to-many relationship between the Student and Course entities, including any necessary migration steps to preserve existing data.

4. The application must validate that the courseId field is present during the enrollment process.

5. The API must always respond with valid JSON, including error responses.

## Success Criteria
1. The application should successfully enroll a Student in a Course when provided with a valid Course ID.
2. The application should return a JSON response that includes the updated list of Courses for the Student.
3. An error response must be returned when attempting to enroll a Student in a non-existing Course.
4. An error response must be returned during enrollment if the Course ID is missing.
5. The database schema update should occur without losing any existing Student and Course data.

## Key Entities
- **Student**
    - Existing fields remain unchanged.
- **Course**
    - Existing fields remain unchanged.
- **Enrollment**
    - **student_id** (foreign key to Student)
    - **course_id** (foreign key to Course)

## Assumptions
1. The existing system is structured to allow for the addition of relationships without disruption to current functionality.
2. Users will employ API tools like Postman or cURL to facilitate testing and interaction with the new endpoints.
3. Input validation will be in place to ensure the integrity of enrollment data.
4. The tech stack used in the prior sprint remains functional and consistent with this feature addition.

## Out of Scope
1. User interface changes or visual representations for enrollment tracking.
2. Advanced features like withdrawal from Courses or bulk enrollment capabilities.
3. Enrollment metrics or reporting functionalities outside of simple course associations.
4. Deployment to production; focus is solely on local development setup and testing.

---
