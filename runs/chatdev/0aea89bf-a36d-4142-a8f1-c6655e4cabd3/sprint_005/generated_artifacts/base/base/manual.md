Here's a detailed user manual for the ChatDev software, specifically tailored to the Course entity functionality we've implemented.

```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This application allows you to manage students and courses efficiently through a simple API interface.

## Main Functions

The primary functions of the application include:

- **Create Students**: Add new students to the database with their names and email addresses.
- **Create Courses**: Add new courses with specified names and levels.
- **Database Management**: The application manages the database schema, ensuring that existing student data is preserved during migrations.

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
   Use pip to install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

### Starting the Application

To start the FastAPI application, run the following command:
```bash
uvicorn main:app --reload
```
This will start the server at `http://127.0.0.1:8000`.

### API Endpoints

#### 1. Create a Student

- **Endpoint**: `POST /students/`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

#### 2. Create a Course

- **Endpoint**: `POST /courses/`
- **Request Body**:
  ```json
  {
    "name": "Introduction to Programming",
    "level": "Beginner"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "Introduction to Programming",
    "level": "Beginner"
  }
  ```

### Database Migration

The application includes a migration function that ensures existing student data is preserved when the database schema is updated. This is handled automatically on application startup.

### Accessing the API Documentation

Once the application is running, you can access the interactive API documentation at `http://127.0.0.1:8000/docs`. This interface allows you to test the endpoints directly.

## Conclusion

The ChatDev Course Management System is designed to simplify the management of students and courses. With its easy-to-use API and robust database management, you can efficiently handle educational data. For any further questions or support, please reach out to our team.

Happy coding!
```

This manual provides a comprehensive overview of the application, installation instructions, usage guidelines, and API documentation, ensuring users can effectively utilize the software.