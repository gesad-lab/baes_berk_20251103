Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Student Management System

A simple application for managing student records, including the ability to create and retrieve student information.

## Main Functions

- **Create Student**: Add a new student with a name and email address.
- **Retrieve Students**: Fetch a list of existing students from the database.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-management-system.git
   cd student-management-system
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have the following dependencies in your `requirements.txt`:
   ```
   fastapi
   sqlalchemy
   pydantic
   alembic
   uvicorn
   ```

## Database Setup

The application uses SQLite for the database. The database will be automatically created when you run the application for the first time.

### Running Migrations

To add the new email field to the Student entity, run the migration script. Ensure you have Alembic installed and configured.

1. **Run Migrations**:
   ```bash
   alembic upgrade head
   ```

This command will add the email column to the existing students table while preserving existing data.

## How to Use the Application

1. **Start the Application**:
   ```bash
   uvicorn main:app --reload
   ```

   The application will be running at `http://127.0.0.1:8000`.

2. **Create a New Student**:
   You can create a new student by sending a POST request to `/students/` with the following JSON body:
   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

   Example using `curl`:
   ```bash
   curl -X POST "http://127.0.0.1:8000/students/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'
   ```

3. **Retrieve Students**:
   To get a list of students, send a GET request to `/students/`:
   ```bash
   curl -X GET "http://127.0.0.1:8000/students/"
   ```

## Documentation

For more detailed documentation, including API references and examples, please refer to the following sections:

- **Getting Started**: Installation, setting up the environment, and simple examples.
- **How-To Examples**: Demos, integrations, and helper functions.
- **Reference**: Full API documentation.
- **Resources**: High-level explanations of core concepts.

For further assistance or to report issues, please contact our support team or visit our GitHub repository.

```

This manual provides a comprehensive overview of the Student Management System, including installation instructions, usage guidelines, and links to further documentation. Let me know if you need any additional information or modifications!