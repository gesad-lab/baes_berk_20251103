```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers efficiently. With this system, you can create and manage relationships between courses and teachers, ensuring a seamless educational experience.

## Main Functions

1. **Student Management**: Create, read, and manage student records, including their associated courses.
2. **Course Management**: Create, read, and manage courses, including assigning teachers to courses.
3. **Teacher Management**: Create, read, and manage teacher records, including their associated courses.
4. **Database Migration**: Automatically migrate existing data while adding new relationships between courses and teachers.

## Installation

To get started with the ChatDev Course Management System, you need to set up your environment and install the necessary dependencies. Follow the steps below:

### Prerequisites

- Python 3.7 or higher
- SQLite (included with Python)

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/chatdev-course-management.git
cd chatdev-course-management
```

### Step 2: Create a Virtual Environment

It's recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required Python packages using pip:

```bash
pip install fastapi sqlalchemy pydantic
```

### Step 4: Run the Application

You can run the application using the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server, and you can access the application at `http://127.0.0.1:8000`.

## How to Use the Application

### API Endpoints

The application exposes several API endpoints to manage students, courses, and teachers.

#### 1. Create a Student

**Endpoint**: `POST /students/`

**Request Body**:
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "course_ids": [1, 2]  // Optional: List of course IDs to associate with the student
}
```

#### 2. Create a Course

**Endpoint**: `POST /courses/`

**Request Body**:
```json
{
  "name": "Mathematics 101",
  "level": "Beginner",
  "teacher_id": 1  // Optional: ID of the teacher assigned to the course
}
```

#### 3. Create a Teacher

**Endpoint**: `POST /teachers/`

**Request Body**:
```json
{
  "name": "Jane Smith",
  "email": "jane.smith@example.com"
}
```

### Viewing the API Documentation

FastAPI automatically generates interactive API documentation. You can view it by navigating to:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## Conclusion

The ChatDev Course Management System is designed to simplify the management of educational entities. By following the installation and usage instructions, you can efficiently manage students, courses, and teachers while preserving existing data through automatic migrations.

For further assistance or support, please contact our support team.
```
