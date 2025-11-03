Here's a detailed user manual for the software, including an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Course Management System

A simple Course Management System built using FastAPI and SQLAlchemy, designed to manage courses and students effectively.

## Main Functions

- **Create Course**: Allows users to create a new course with a name and level.
- **Database Management**: Automatically manages the database schema, including the preservation of existing student data during migrations.
- **API Integration**: Provides a RESTful API for interacting with courses and students.

## Quick Install

To set up the Course Management System, you need to install the required dependencies. You can do this using pip. 

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Dependencies

Make sure you have the following dependencies installed:

- **fastapi**: The web framework used to build the API.
- **uvicorn**: The ASGI server to run the FastAPI application.
- **sqlalchemy**: The ORM used for database interactions.
- **pydantic**: The data validation and settings management library used with FastAPI.

You can install these dependencies using the command:
```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

## How to Use

1. **Run the Application**:
   Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   Once the server is running, you can access the API documentation at:
   ```
   http://127.0.0.1:8000/docs
   ```

3. **Creating a Course**:
   To create a new course, send a POST request to the `/courses` endpoint with the following JSON body:
   ```json
   {
       "name": "Course Name",
       "level": "Course Level"
   }
   ```

   Example using `curl`:
   ```bash
   curl -X POST "http://127.0.0.1:8000/courses" -H "Content-Type: application/json" -d '{"name": "Math 101", "level": "Beginner"}'
   ```

4. **Database Migration**:
   The application automatically handles database migrations. When you run the application for the first time, it will create the necessary tables for both students and courses while preserving existing student data.

## Additional Information

For more detailed documentation on FastAPI, SQLAlchemy, and Pydantic, please refer to their official documentation:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

## Support

If you encounter any issues or have questions, please reach out to our support team at support@chatdev.com.

```

This manual provides a comprehensive guide for users to understand the functionality of the Course Management System, how to set it up, and how to use it effectively.