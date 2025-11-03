Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Student Management API

A FastAPI application for managing student records, including the ability to create and retrieve student information.

## Main Functions

- **Create Student**: Allows users to add a new student with a name and email address.
- **Get Students**: Retrieves a list of students with pagination support.

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
   alembic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

1. **Initialize the Database**:
   The database will be automatically initialized when the application starts. Ensure that the `init_db()` function in `main.py` is called during the startup event.

2. **Run Migrations**:
   To apply the database migrations, run the following command:
   ```bash
   alembic upgrade head
   ```

## How to Use the API

### Start the Application

Run the FastAPI application using Uvicorn:
```bash
uvicorn main:app --reload
```
The application will be available at `http://127.0.0.1:8000`.

### API Endpoints

#### Create a Student

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

#### Get Students

- **Endpoint**: `GET /students/`
- **Query Parameters**:
  - `skip` (optional): Number of records to skip (default is 0).
  - `limit` (optional): Number of records to return (default is 10).
- **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    },
    {
      "id": 2,
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
  ]
  ```

## Additional Information

- **Documentation**: For more detailed information on FastAPI, please refer to the [FastAPI Documentation](https://fastapi.tiangolo.com/).
- **Database Migration**: The application uses Alembic for database migrations. The migration script `migration_script.py` adds the email column to the students table while preserving existing data.

## Conclusion

This Student Management API provides a simple yet effective way to manage student records. By following the installation and usage instructions, you can quickly set up and start using the API for your student management needs.
```

This manual provides a comprehensive overview of the software, installation instructions, and usage guidelines, ensuring that users can effectively utilize the Student Management API.