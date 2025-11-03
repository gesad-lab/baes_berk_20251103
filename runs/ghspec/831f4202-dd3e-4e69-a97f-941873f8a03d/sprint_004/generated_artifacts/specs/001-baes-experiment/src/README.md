# Updated README.md

# Student Management Application

Welcome to the Student Management Application! This application allows you to manage students and their associated courses efficiently. Below are the updated instructions for using the new features related to course associations.

## Getting Started

### Installation

Make sure you have Python 3.8+ and SQLite installed. Clone the repository, create a virtual environment, and install the dependencies:

```bash
git clone https://your-repo-url.git
cd your-repo-directory
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Running the Application

To start the application, run:

```bash
uvicorn src.main:app --reload
```

You can access the API documentation at `http://localhost:8000/docs`.

## Course Associations

The latest features allow you to associate students with courses. Here are the user scenarios, along with the expected results:

### Associating a Student with Courses

1. **Select a Student**: Choose a student from the list.
2. **Enroll in Courses**: Select one or more courses you want to associate with the chosen student.
3. **Submit Selection**: Submit your selection to enroll the student.

**Expected Result**: The student's record will update to reflect the newly associated courses, and a success message is displayed.

### Retrieving Student Course Information

1. **Student Detail Request**: Request the details for a specific student.
  
**Expected Result**: The system will return a JSON response, including the student's information and a list of all associated courses.

### Error Handling for Invalid Course Associations

1. **Attempt Invalid Association**: If a user tries to associate a student with a non-existing course, the system will reject the request.
  
**Expected Result**: A "400 Bad Request" error will be returned indicating that the course must exist before being associated with a student.

### Retrieving Courses Associated with Multiple Students

1. **Student Group Request**: Input a request to fetch details for a specific group of students.
  
**Expected Result**: A JSON response with the courses associated with the specified students is returned.

## API Endpoints

### Endpoints for Course Associations

- **POST /students/{student_id}/courses**: Associate courses with a student.
- **GET /students/{student_id}/courses**: Retrieve the courses associated with a student.
- **GET /students/courses**: Retrieve course information for multiple students.

### Error Responses

Ensure that you handle error responses properly. The system will return errors in the following format:

```json
{
  "error": {
    "code": "E001",
    "message": "The specified course must exist before it can be associated.",
    "details": {}
  }
}
```

## Conclusion

The Student Management Application now supports robust course associations, making it easier to manage student enrollments. For further details, please refer to the API documentation linked above.

For any issues or contributions, feel free to open an issue on the GitHub repository or submit a pull request.

Happy coding!