# Course Management System

A simple Course Management System built using FastAPI and SQLAlchemy to manage students and courses.

## Quick Install

To get started, you need to install the required dependencies. You can do this using pip:

```bash
pip install fastapi sqlalchemy pydantic alembic
```

Or if you prefer using conda:

```bash
conda install fastapi sqlalchemy pydantic alembic -c conda-forge
```

## 🤔 What is this?

This application allows users to manage students and courses. You can create, read, and manage student and course data through a RESTful API. The main features include:

- **Student Management**: Create and retrieve student records.
- **Course Management**: Create and retrieve course records.
- **Database Migration**: Migrate the database schema to include new tables without losing existing data.

## 📖 Main Functions

### 1. Student Management

- **Create a Student**: 
  - Endpoint: `POST /students/`
  - Request Body:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - Response: Returns the created student object with an ID.

- **Get a Student**: 
  - Endpoint: `GET /students/{student_id}`
  - Response: Returns the student object for the given ID.

### 2. Course Management

- **Create a Course**: 
  - Endpoint: `POST /courses/`
  - Request Body:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```
  - Response: Returns the created course object with an ID.

- **Get a Course**: 
  - Endpoint: `GET /courses/{course_id}`
  - Response: Returns the course object for the given ID.

### 3. Database Migration

To apply the database migrations and create the necessary tables, run the following command:

```bash
alembic upgrade head
```

This command will create the `courses` table while preserving existing student data.

## 🛠️ How to Use

1. **Set Up the Environment**: Follow the Quick Install section to set up your environment and install dependencies.

2. **Run the Application**: Start the FastAPI application by running:

   ```bash
   uvicorn main:app --reload
   ```

3. **Access the API**: Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

4. **Create Students and Courses**: Use the provided endpoints to create and manage students and courses.

5. **Database Migration**: Ensure to run the migration command to set up the database schema correctly.

## 📚 Documentation

For more detailed documentation, please refer to the following resources:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

This manual provides a comprehensive overview of the Course Management System and how to utilize its features effectively. Enjoy managing your courses and students!