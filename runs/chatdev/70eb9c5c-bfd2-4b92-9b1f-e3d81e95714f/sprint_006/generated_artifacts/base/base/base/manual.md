```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows you to manage courses and students effectively through a simple API interface. Below you will find instructions on how to install the necessary dependencies, as well as how to use the application.

## Main Functions

The Course Management System provides the following functionalities:

- **Create Students**: Add new students to the database.
- **Retrieve Students**: Fetch a list of students with pagination support.
- **Create Courses**: Add new courses with specified names and levels.
- **Retrieve Courses**: Fetch a list of courses with pagination support.

## Installation

To get started with the Course Management System, you need to install the required dependencies. Follow these steps:

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   alembic
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

1. **Start the FastAPI server**:
   You can run the application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the server on `http://127.0.0.1:8000`.

2. **Access the API Documentation**:
   Once the server is running, you can access the interactive API documentation at:
   ```
   http://127.0.0.1:8000/docs
   ```

### API Endpoints

#### Students

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Retrieve Students**:
  - **Endpoint**: `GET /students/`
  - **Query Parameters**: `skip`, `limit` (for pagination)

#### Courses

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Introduction to Programming",
      "level": "Beginner"
    }
    ```

- **Retrieve Courses**:
  - **Endpoint**: `GET /courses/`
  - **Query Parameters**: `skip`, `limit` (for pagination)

## Database Migrations

The application uses Alembic for managing database migrations. To apply the migrations, run the following command:
```bash
alembic upgrade head
```

This will create the necessary tables in the database, including the `students` and `courses` tables, while preserving existing data.

## Conclusion

The ChatDev Course Management System is designed to be simple and efficient for managing courses and students. If you have any questions or need further assistance, please refer to the API documentation or contact our support team.

Happy coding!
```