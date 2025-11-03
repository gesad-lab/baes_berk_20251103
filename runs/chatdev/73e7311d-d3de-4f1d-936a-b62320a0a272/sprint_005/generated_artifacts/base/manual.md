Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Student Course Management Application

A simple application for managing students and their associated courses.

## Overview

This application allows users to create and manage students and courses, establishing a many-to-many relationship between them. Students can enroll in multiple courses, and each course can have multiple students.

## Main Functions

- **Create a Student**: Add a new student with a name, email, and associated course IDs.
- **Read Student Information**: Retrieve details about a specific student, including their enrolled courses.
- **Create a Course**: Add a new course with a name and level.
- **Read Course Information**: Retrieve details about a specific course and its enrolled students.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Dependencies

The following dependencies are required for the application:

- **fastapi**: The web framework used to build the API.
- **uvicorn**: The ASGI server for running the FastAPI application.
- **sqlalchemy**: The ORM (Object Relational Mapper) used for database interactions.
- **pydantic**: Used for data validation and settings management, particularly for the schemas defined in `schemas.py`.

You can install these dependencies using pip with the following command:

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

## How to Use the Application

1. **Start the Application**:
   Run the following command to start the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API Documentation**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

3. **Creating a Student**:
   Use the POST endpoint `/students/` to create a new student. You need to provide a JSON body with the following structure:
   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com",
       "course_ids": [1, 2]  // List of course IDs the student is enrolling in
   }
   ```

4. **Reading Student Information**:
   Use the GET endpoint `/students/{student_id}` to retrieve information about a specific student by their ID.

5. **Creating a Course**:
   Use the POST endpoint `/courses/` to create a new course. You need to provide a JSON body with the following structure:
   ```json
   {
       "name": "Mathematics",
       "level": "Intermediate"
   }
   ```

6. **Reading Course Information**:
   Use the GET endpoint `/courses/{course_id}` to retrieve information about a specific course by its ID.

## Conclusion

This application provides a straightforward way to manage students and courses, allowing for easy enrollment and retrieval of information. For further customization or enhancements, feel free to modify the code as needed.

For any issues or support, please reach out to the development team.
```

This manual provides a comprehensive overview of the application, its functionalities, installation instructions, and usage guidelines, ensuring that users can effectively utilize the software.