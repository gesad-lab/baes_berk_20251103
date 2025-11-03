# README.md

# Feature: Add Course Relationship to Student Entity

## Overview & Purpose
The purpose of this feature is to establish a relationship between the Student entity and the Course entity, enabling students to enroll in multiple courses. This relationship will enhance the educational offerings and facilitate better management of student course enrollments. By integrating this feature, we aim to provide students with flexibility in course selection while preserving the integrity of existing student data.

## User Scenarios & Testing
1. **As a user, I want to enroll a student in a course** so that I can track which courses each student is currently taking.
   - Test: Send a POST request to enroll a student in a specific course and verify that the relationship record is created in the database.

2. **As a user, I want to retrieve a list of courses a student is enrolled in** so that I can view their current academic commitments.
   - Test: Send a GET request for a particular student and confirm that the response includes all courses they are enrolled in.

3. **As a user, I want to remove a student from a course** so that I can manage course enrollments effectively.
   - Test: Send a DELETE request to unlink a student from a course and verify that the relationship no longer exists in the database.

4. **As a user, I want to ensure that existing student data is unaffected during the schema migration** that adds the course relationship.
   - Test: Retrieve all student records post-migration to ensure their integrity and retention of existing data.

5. **As a user, I want to confirm that students can enroll in multiple courses** without any disruption in the system functionality.
   - Test: Enroll the same student in multiple courses and check that the relationships are maintained correctly in the database.

---

## VII. Logging and Monitoring

- Implement structured logging to track API requests, responses, and errors during the student-course relationship operations.
- The following logging will be implemented:
  - Logging for course retrievals to track when a student’s course list is fetched.
  - Logging for removals to track when a student is removed from a course.

### Example Logging Implementation

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    logger.info("Retrieving courses for student %s.", student_id)
    # Logic to retrieve courses...

@app.route('/students/<int:student_id>/courses/<int:course_id>', methods=['DELETE'])
def remove_student_from_course(student_id, course_id):
    logger.info("Removing student %s from course %s.", student_id, course_id)
    # Logic to remove the student from the course...
```

## # Implementation Plan: Add Course Relationship to Student Entity