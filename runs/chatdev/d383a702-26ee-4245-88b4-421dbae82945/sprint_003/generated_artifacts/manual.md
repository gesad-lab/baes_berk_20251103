```markdown
# Course Management System

A simple API for managing students and courses, built using FastAPI and SQLAlchemy.

## Main Functions

This software provides the following main functionalities:

- **Student Management**: Create and retrieve student records.
- **Course Management**: Create and retrieve course records.
- **Database Migration**: Automatically manage database schema changes while preserving existing data.

## Quick Install

To set up the environment and install the required dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🤔 What is this?

This Course Management System allows users to manage students and courses through a RESTful API. It utilizes FastAPI for the web framework, SQLAlchemy for database interactions, and Alembic for database migrations.

### Key Features:

- **Create Students**: Add new students with their names and emails.
- **Retrieve Students**: Get a list of all students with pagination support.
- **Create Courses**: Add new courses with their names and levels.
- **Retrieve Courses**: Get a list of all courses with pagination support.

## 📖 Usage

### Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### API Endpoints

#### Student Endpoints

- **Create a Student**
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Retrieve Students**
  - **Endpoint**: `GET /students/`
  - **Query Parameters**: `skip` (int), `limit` (int)

#### Course Endpoints

- **Create a Course**
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Retrieve Courses**
  - **Endpoint**: `GET /courses/`
  - **Query Parameters**: `skip` (int), `limit` (int)

### Database Migration

To apply database migrations, run the following command:

```bash
alembic upgrade head
```

This will create the necessary tables in the database while preserving existing student data.

## Conclusion

This Course Management System provides a simple yet effective way to manage students and courses through a RESTful API. With the ability to create and retrieve records, along with database migration capabilities, it serves as a solid foundation for further development and enhancements.
```