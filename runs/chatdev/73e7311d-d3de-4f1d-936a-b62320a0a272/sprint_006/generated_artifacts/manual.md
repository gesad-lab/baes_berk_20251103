```markdown
# Student Course Management System

A comprehensive application for managing students, courses, and teachers, allowing for easy tracking of relationships and data.

## Main Functions

1. **Student Management**: Create, read, and manage student information including their associated courses.
2. **Course Management**: Create, read, and manage courses, including assigning teachers to courses.
3. **Teacher Management**: Create, read, and manage teacher information and their associated courses.
4. **Relationships**: Establish relationships between students and courses, as well as between courses and teachers.

## Installation

To set up the environment for the Student Course Management System, follow these steps:

### Prerequisites

- Ensure you have Python 3.7 or higher installed on your machine.
- Install pip if it is not already installed.

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-repo/student-course-management.git
cd student-course-management
```

### Step 2: Install Dependencies

You can install the required dependencies using pip. Run the following command in your terminal:

```bash
pip install fastapi[all] sqlalchemy pydantic
```

### Step 3: Initialize the Database

Before running the application, you need to initialize the database. This can be done by running the `main.py` file, which will create the necessary database schema.

```bash
python main.py
```

## How to Use the Application

### Starting the Application

To start the application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server, and you can access the application at `http://127.0.0.1:8000`.

### API Endpoints

The application provides several API endpoints for managing students, courses, and teachers.

#### 1. Students

- **Create a Student**
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  
- **Get a Student**
  - **Endpoint**: `GET /students/{student_id}`
  
#### 2. Courses

- **Create a Course**
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Intermediate",
      "teacher_id": 1
    }
    ```
  
- **Get a Course**
  - **Endpoint**: `GET /courses/{course_id}`

#### 3. Teachers

- **Create a Teacher**
  - **Endpoint**: `POST /teachers/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```
  
- **Get a Teacher**
  - **Endpoint**: `GET /teachers/{teacher_id}`

### Testing the API

You can test the API using tools like Postman or curl. Simply send requests to the specified endpoints with the appropriate request bodies.

### Example Usage

1. **Create a Teacher**:
   - Send a POST request to `/teachers/` with the teacher's details.
   
2. **Create a Course**:
   - Send a POST request to `/courses/` with the course details and the ID of the teacher assigned to the course.
   
3. **Create a Student**:
   - Send a POST request to `/students/` with the student's details.

4. **Enroll a Student in a Course**:
   - Update the student's `course_ids` to include the ID of the course they are enrolling in.

## Conclusion

This application provides a robust framework for managing students, courses, and teachers, with a focus on maintaining relationships between entities. For further documentation and advanced usage, please refer to the FastAPI documentation [here](https://fastapi.tiangolo.com/).
```