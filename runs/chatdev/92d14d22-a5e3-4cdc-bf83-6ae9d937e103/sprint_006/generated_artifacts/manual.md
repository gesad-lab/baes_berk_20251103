```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students, courses, and teachers effectively. You can create, retrieve, and manage relationships between these entities seamlessly.

## Main Functions

1. **Student Management**: Create and manage student records, including their enrollment in courses.
2. **Course Management**: Create and manage courses, including assigning teachers to courses.
3. **Teacher Management**: Create and manage teacher records, allowing them to be associated with courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

### Running the Application

1. **Start the Server**:
   Run the following command to start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI. Here, you can test the endpoints for managing students, courses, and teachers.

### API Endpoints

#### Student Endpoints

- **Create Student**: 
  - **POST** `/students/`
  - Request Body: `{ "name": "John Doe", "email": "john@example.com", "course_ids": [1, 2] }`
  
- **Get Students**: 
  - **GET** `/students/`

#### Course Endpoints

- **Create Course**: 
  - **POST** `/courses/`
  - Request Body: `{ "name": "Mathematics", "level": "Beginner", "teacher_id": 1 }`
  
- **Get Courses**: 
  - **GET** `/courses/`

#### Teacher Endpoints

- **Create Teacher**: 
  - **POST** `/teachers/`
  - Request Body: `{ "name": "Jane Smith", "email": "jane@example.com" }`
  
- **Get Teachers**: 
  - **GET** `/teachers/`

### Database Migration

The application is designed to preserve existing data during database migrations. When you add a teacher relationship to the Course entity, the migration script will ensure that existing Student, Course, and Teacher data remains intact.

### Conclusion

This Course Management System is a powerful tool for educational institutions to manage their courses, students, and teachers efficiently. For further assistance, please refer to the API documentation or reach out to our support team.

Happy coding!
```