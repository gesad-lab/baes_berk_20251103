```markdown
# Course Management System

A simple application to manage courses and students using Python, SQLAlchemy, and Pydantic.

## Main Functions

This software provides the following main functionalities:

- **Course Management**: Create and manage courses with required fields such as name and level.
- **Student Management**: Manage student records, including their names and emails.
- **Database Migration**: Automatically migrate the database schema to include new fields and tables while preserving existing data.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

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

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

1. **Run the migration script** to create the necessary database tables:
   ```bash
   python main.py
   ```

2. **Interacting with the Application**:
   - You can interact with the application through a dashboard or API (if implemented).
   - Use the provided schemas in `schemas.py` to validate data when creating or updating courses and students.

### Creating a Course

To create a new course, ensure you provide the following fields:

- `name`: A string representing the name of the course (required).
- `level`: A string representing the level of the course (required).

### Example of Creating a Course

If you are using an API, you might send a POST request like this:

```json
{
  "name": "Introduction to Programming",
  "level": "Beginner"
}
```

### Database Structure

- **Students Table**: Contains fields for student ID, name, and email.
- **Courses Table**: Contains fields for course ID, name, and level.

### Database Migration

The application includes a migration script that ensures existing student data is preserved while adding new fields and tables. The migration process is handled automatically when you run `main.py`.

## Documentation

For more detailed documentation on how to extend the application, manage data, and integrate with other systems, please refer to the following sections:

- **Getting Started**: Installation, setting up the environment, and simple examples.
- **How-To Examples**: Demos, integrations, and helper functions.
- **Reference**: Full API documentation.
- **Resources**: High-level explanations of core concepts.

For any issues or support, please reach out to our support team.

```
