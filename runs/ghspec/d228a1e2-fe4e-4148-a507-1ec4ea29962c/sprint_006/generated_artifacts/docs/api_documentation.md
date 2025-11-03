```markdown
# API Documentation for Course-Teacher Management

## User Scenarios:
1. **Assign Teacher to Course**: As an admin, I want to assign a teacher to a course so that it reflects the teacher responsible for that course.
2. **View Course Details with Teacher Information**: As an admin, I want to view course details, including the assigned teacher, to easily understand the course structure.
3. **List Courses by Teacher**: As a teacher, I want to see a list of courses I am assigned to, so that I can manage them efficiently.

## Testing Scenarios:
- Test that an admin can successfully assign a teacher to a course and that the assignment is reflected accurately in the database.
- Test that the system retrieves the correct course details, including the assigned teacher information.
- Test that the system can list all courses associated with a specific teacher.
- **Test Scenarios for No Assigned Courses**:
  - Test that when a teacher has no courses assigned, the response indicates an empty list and the correct HTTP status code.
  - Test that retrieving courses for a non-existing teacher returns a 404 error with an appropriate message.

## 3. Functional Requirements
1. **Assign Teacher to Course API Endpoint**:
   - Method: POST
   - URL: `/courses/{course_id}/assign-teacher`
   - Request Body: JSON object containing the required field `teacher_id` (Integer).
   - Response: JSON object indicating the success or failure of the assignment with appropriate HTTP status codes.

2. **Get Course Details API Endpoint**:
   - Method: GET
   - URL: `/courses/{course_id}`
   - Response: JSON object containing details of the requested course, including its assigned teacher's ID, name, and email.

3. **List Courses by Teacher API Endpoint**:
   - Method: GET
   - URL: `/teachers/{teacher_id}/courses`
   - Response: JSON array containing objects for each course assigned to the specified teacher, including course ID and title.

4. **Database Migration**:
   - Update the existing `Course` schema to include a new field:
     - `teacher_id`: Integer (foreign key referencing `Teacher.id`)
   - Ensure that the migration script preserves all existing `Student`, `Course`, and `Teacher` data during the structural change.

## Unit Test Scenarios for Teacher-Course Relationships
```python
def test_list_courses_by_teacher_with_no_courses(client):
    """
    Test that when a teacher has no courses assigned, the response indicates an empty list.
    """
    # Assuming teacher_id 1 has no courses assigned
    response = client.get('/teachers/1/courses')
    assert response.status_code == 200
    assert response.json == []  # Expecting an empty list

def test_list_courses_for_non_existing_teacher(client):
    """
    Test that retrieving courses for a non-existing teacher 
    returns a 404 error with an appropriate message.
    """
    response = client.get('/teachers/999/courses')  # Assuming 999 does not exist
    assert response.status_code == 404
    assert response.json == {"error": {"code": "E404", "message": "Teacher not found."}}
```
```