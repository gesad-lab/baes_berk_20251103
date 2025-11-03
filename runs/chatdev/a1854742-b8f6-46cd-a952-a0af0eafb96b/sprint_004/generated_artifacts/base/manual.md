```markdown
# Course Management Application

A simple application for managing students and courses using FastAPI and SQLAlchemy.

## Main Functions

- **Student Management**: Create and manage student records, including their names and email addresses.
- **Course Management**: Create and manage course records, including course names and levels.
- **Database Migration**: Automatically handle database schema changes while preserving existing data.

## Quick Install

To set up the environment and install the required dependencies, follow these steps:

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
   alembic
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

### Running the Application

1. **Start the FastAPI Application**:
   Run the following command in your terminal:
   ```bash
   uvicorn main:app --reload
   ```
   The application will be accessible at `http://127.0.0.1:8000`.

### API Endpoints

- **Create a Student**:
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

### Database Migration

To manage database schema changes, the application uses Alembic. To create the initial database schema and apply migrations:

1. **Run Migrations**:
   ```bash
   alembic upgrade head
   ```

This command will create the necessary tables in the database while preserving existing data.

## Additional Information

- **Documentation**: For more detailed information on FastAPI and SQLAlchemy, please refer to their official documentation:
  - [FastAPI Documentation](https://fastapi.tiangolo.com/)
  - [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

- **Contributing**: If you would like to contribute to the project, please fork the repository and submit a pull request.

- **Support**: For any issues or questions, please open an issue in the repository.

Enjoy using the Course Management Application!
```