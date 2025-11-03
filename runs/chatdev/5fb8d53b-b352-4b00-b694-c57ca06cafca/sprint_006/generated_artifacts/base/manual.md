Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Teacher Management System

A simple API for managing Teachers, Students, and Courses.

## 📦 Main Functions

This software provides the following main functionalities:

- **Create Teacher**: Add new teachers with their names and email addresses.
- **Create Student**: Add new students with their names and email addresses.
- **Create Course**: Add new courses with their names and levels.
- **Manage Relationships**: Associate students with courses through a many-to-many relationship.

## 🚀 Quick Install

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

3. **Install dependencies**:
   ```bash
   pip install fastapi sqlalchemy alembic uvicorn
   ```

## 🛠️ Setting Up the Database

Before running the application, you need to initialize the database:

1. **Run the database initialization script**:
   ```bash
   python -c "from database import init_db; init_db()"
   ```

This will create the necessary tables in the SQLite database while preserving existing Student and Course data.

## 🎮 How to Use the API

Once the environment is set up and the database is initialized, you can start the FastAPI application:

1. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   Open your browser and go to `http://127.0.0.1:8000/docs` to view the interactive API documentation provided by FastAPI.

### API Endpoints

- **Create a Teacher**:
  - **Endpoint**: `POST /teachers/`
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

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

## 📚 Documentation

For more detailed documentation on how to use the API, please refer to the FastAPI documentation [here](https://fastapi.tiangolo.com/).

## 🤝 Support

If you encounter any issues or have questions, please reach out to our support team at [support@chatdev.com](mailto:support@chatdev.com).
```

This manual provides a comprehensive overview of the software, including installation instructions, usage guidelines, and API endpoints. Let me know if you need any further modifications or additional information!