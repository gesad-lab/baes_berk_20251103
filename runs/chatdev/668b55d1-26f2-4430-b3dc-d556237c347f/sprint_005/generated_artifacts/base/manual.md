```markdown
# Student Course Management System

A simple application for managing students and their associated courses.

## Overview

This application allows you to create and manage students and courses, establishing a many-to-many relationship between them. Students can enroll in multiple courses, and each course can have multiple students.

## Main Functions

- **Create Student**: Add a new student to the system with their name, email, and associated courses.
- **Create Course**: Add a new course to the system with its name and level.
- **View Students**: Retrieve a list of all students along with their enrolled courses.
- **View Courses**: Retrieve a list of all courses along with their enrolled students.

## Installation

To run this application, you need to set up your environment and install the required dependencies. Follow the steps below:

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-repo/student-course-management.git
cd student-course-management
```

### Step 2: Create a Virtual Environment

It is recommended to create a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required Python packages using pip:

```bash
pip install fastapi sqlalchemy pydantic alembic
```

### Step 4: Run Database Migrations

Before running the application, you need to set up the database schema. Run the migration script:

```bash
alembic upgrade head
```

## How to Use the Application

### Starting the Application

To start the FastAPI application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### API Endpoints

#### Create a Student

**Endpoint**: `POST /students/`

**Request Body**:
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "course_ids": [1, 2]  // List of course IDs to associate
}
```

**Response**:
Returns the created student object with their ID, name, email, and associated course IDs.

#### Create a Course

**Endpoint**: `POST /courses/`

**Request Body**:
```json
{
  "name": "Mathematics",
  "level": "Intermediate"
}
```

**Response**:
Returns the created course object with its ID, name, and level.

### Viewing Students and Courses

You can view all students and courses by implementing additional GET endpoints in the `main.py` file. Here’s an example of how to retrieve all students:

```python
@app.get("/students/", response_model=List[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()
```

### Testing the Application

You can test the API using tools like Postman or curl. Make sure to send requests to the correct endpoints with the appropriate request bodies.

## Conclusion

This application provides a simple yet effective way to manage students and courses, allowing for easy enrollment and data management. For further enhancements, consider adding features like user authentication, course scheduling, and more detailed reporting.

For any issues or feature requests, please reach out to the development team.
```