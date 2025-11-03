Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Student Management API

A FastAPI application for managing student data, including the ability to create and retrieve student records with email support.

## Main Functions

- **Create Student**: Allows the creation of a new student record with a name and email address.
- **Retrieve Students**: Fetches a list of existing students from the database.

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

1. **Run the Application**:
   Start the FastAPI application by running:
   ```bash
   python main.py
   ```
   The application will be available at `http://127.0.0.1:8000`.

2. **API Endpoints**:
   - **Create a Student**:
     - **Endpoint**: `POST /students`
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

   - **Retrieve Students**:
     - **Endpoint**: `GET /students`
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

## Database Migration

The application uses SQLite as the database. When you run the application for the first time, it will automatically create the database and the `students` table if they do not already exist. The migration process preserves existing student data while adding the new email field.

## Additional Information

For more details on FastAPI and SQLAlchemy, please refer to the official documentation:
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

## Support

If you encounter any issues or have questions, please reach out to our support team at support@chatdev.com.
```

This manual provides a comprehensive overview of the software, including installation instructions, usage details, and support information. Let me know if you need any modifications or additional sections!