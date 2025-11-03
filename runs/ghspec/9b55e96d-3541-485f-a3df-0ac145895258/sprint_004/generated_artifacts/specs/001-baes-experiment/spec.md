# Feature: Add Course Relationship to Student Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the existing Student entity and the newly created Course entity within the educational management system. This relationship will enable Students to enroll in and associate multiple Courses, thereby facilitating better tracking and management of their education. The enhancement aims to provide greater value to students and educators by allowing comprehensive visibility into students' course enrollments, which is critical for academic planning and assessment.

## User Scenarios & Testing
1. **Enrolling a Student in a Course**:
   - A user provides a Student ID and Course ID to enroll the student in a course.
   - The system should successfully associate the Student with the specified Course and return a confirmation response.

2. **Retrieving a Student's Courses**:
   - A user requests to view all Courses associated with a specific Student.
   - The application should return a list of Course details (e.g., name, level) for the specified Student.

3. **Removing a Student from a Course**:
   - A user provides a Student ID and Course ID to remove the student from the course.
   - The system should successfully disassociate the Student from the specified Course and return a confirmation response.

4. **Enrolling a Student Without Existing Records**:
   - A user attempts to enroll a Student in a Course when either the Student ID or Course ID does not exist.
   - The system should return an error indicating that the Student or Course was not found.

5. **Retrieving Courses for a Non-existent Student**:
   - A user tries to retrieve Courses for a Student that does not exist.
   - The system should return an error indicating that the Student was not found.

## Functional Requirements
1. **Student Enrollment in Course**:
   - Endpoint: POST `/students/{student_id}/enroll`
   - Input: Student ID (integer, required) and Course ID (integer, required).
   - Output: JSON response confirming enrollment (200 OK) or error (404 Not Found if Student or Course does not exist).

2. **Retrieve Student Courses**:
   - Endpoint: GET `/students/{student_id}/courses`
   - Input: Student ID (integer, required).
   - Output: JSON array containing details of Courses the Student is enrolled in or error (404 Not Found if Student does not exist).

3. **Remove Student from Course**:
   - Endpoint: DELETE `/students/{student_id}/courses/{course_id}`
   - Input: Student ID (integer, required) and Course ID (integer, required).
   - Output: JSON response confirming removal (200 OK) or error (404 Not Found if Student or Course does not exist).

4. **Database Management**:
   - Update the database schema to introduce a new associative entity (e.g., `Enrollment`) that connects `Student` and `Course`, ensuring existing data remains intact.

## Success Criteria
- **Functionality**: The application must allow successful enrollment and removal of Students in/from Courses, as well as retrieval of all Courses for a Student.
- **Response Format**: All responses must be in valid JSON format detailing the status of the operations performed.
- **Persistence**: All associations between Students and Courses must retain integrity and persist across application restarts.
- **Error Handling**: Clear and actionable error messages must be returned for invalid Student or Course IDs during enrollment and retrieval operations.
- **Data Integrity**: The existing Student and Course records must remain unchanged and unaffected by this new enrollment relationship.

## Key Entities
- **Enrollment**:
  - **Attributes**:
    - `id` (integer, auto-generated primary key)
    - `student_id` (integer, references Student entity, required)
    - `course_id` (integer, references Course entity, required)
  
- **Student (existing)**:
  - Attributes relevant for relationship mapping.
  
- **Course (existing)**:
  - Attributes relevant for relationship mapping.

## Assumptions
- Users have sufficient knowledge of the system to identify and input valid Student and Course IDs.
- The existing architecture supports the introduction of associative entities without major refactoring.
- There are no special cases regarding enrollment limits or prerequisites at this stage.

## Out of Scope
- Advanced features such as handling prerequisites or configurable enrollment policies.
- User interfaces for course enrollment management.
- Integration with third-party systems for educational resources or external course offerings.
- Any modifications to the existing Course management features introduced in the previous sprint.