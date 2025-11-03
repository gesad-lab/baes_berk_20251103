```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage students and their course enrollments efficiently. Below, you will find a detailed user manual that covers the main functions of the software, how to install the necessary environment dependencies, and how to use the application.

## Main Functions

### 1. Student Management
- **Create Student**: Add a new student with their name and email address.
- **Retrieve Students**: Fetch a list of all registered students.

### 2. Course Management
- **Create Course**: Add a new course with its name and level.
- **Retrieve Courses**: Fetch a list of all available courses.

### 3. Course Enrollment
- **Enroll Student in Courses**: When creating a student, you can also specify which courses they should be enrolled in.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```plaintext
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   alembic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

To run the FastAPI application, execute the following command:
```bash
uvicorn main:app --reload
```
This will start the server at `http://127.0.0.1:8000`.

### API Endpoints

You can interact with the application through the following API endpoints:

#### Student Endpoints
- **Create Student**: 
  - **POST** `/students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "course_ids": [1, 2]  // Optional: List of course IDs to enroll in
    }
    ```

- **Get Students**:
  - **GET** `/students/`
  - **Response**: List of all students.

#### Course Endpoints
- **Create Course**:
  - **POST** `/courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Get Courses**:
  - **GET** `/courses/`
  - **Response**: List of all courses.

### Database Migration

The application uses Alembic for database migrations. To apply migrations, run:
```bash
alembic upgrade head
```
This will ensure that your database schema is up-to-date with the latest changes.

## Conclusion

The ChatDev Course Management System provides a robust solution for managing students and their course enrollments. By following the instructions in this manual, you can easily set up the environment, run the application, and utilize its features effectively.

For further assistance, please refer to the documentation or contact support.
```