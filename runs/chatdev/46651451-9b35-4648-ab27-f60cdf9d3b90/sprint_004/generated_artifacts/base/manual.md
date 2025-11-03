Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Course Management System

A simple application for managing courses and students.

## Overview

The Course Management System allows users to create and manage courses, each defined by a name and level. The system also preserves existing student data while introducing the new Course entity.

## Main Functions

- **Create Course**: Add a new course with a specified name and level.
- **Preserve Student Data**: Ensure that existing student data remains intact during database migrations.

## Quick Install

To set up the Course Management System, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Ensure you have Python installed (version 3.7 or higher). Then, install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt` file, you can manually install the necessary packages:
   ```bash
   pip install sqlalchemy pydantic uvicorn
   ```

3. **Set Up the Database**:
   The application uses SQLite for the database. The database file will be created automatically when you run the application for the first time.

## How to Use

1. **Run the Application**:
   Start the application using the following command:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   Once the application is running, you can access the API at `http://127.0.0.1:8000`.

3. **Create a Course**:
   To create a new course, send a POST request to the `/courses` endpoint with the following JSON body:
   ```json
   {
       "name": "Course Name",
       "level": "Beginner"
   }
   ```

   Example using `curl`:
   ```bash
   curl -X POST "http://127.0.0.1:8000/courses" -H "Content-Type: application/json" -d '{"name": "Course Name", "level": "Beginner"}'
   ```

4. **Check Existing Courses**:
   You can retrieve all existing courses by sending a GET request to the `/courses` endpoint:
   ```bash
   curl -X GET "http://127.0.0.1:8000/courses"
   ```

## Database Migration

The application includes a migration script that ensures existing student data is preserved while adding the new Course entity. The migration is handled automatically when the application starts.

## Additional Resources

For more information on how to extend the functionality of the Course Management System, refer to the following resources:

- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

## Support

If you encounter any issues or have questions, please reach out to our support team at [support@chatdev.com](mailto:support@chatdev.com).

```

This manual provides a comprehensive guide for users to understand the software's functionality, installation process, and usage instructions. Let me know if you need any modifications or additional information!