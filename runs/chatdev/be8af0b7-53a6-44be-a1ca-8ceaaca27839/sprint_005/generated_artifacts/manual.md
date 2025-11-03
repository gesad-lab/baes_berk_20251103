Here's the `manual.md` file that provides a detailed user manual for the software, including an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Teacher Management System

A simple API for managing teachers, students, and courses.

## Overview

This application allows users to create and manage entities such as Teachers, Students, and Courses. It provides a RESTful API built with FastAPI, enabling easy integration and interaction with the data.

### Main Functions

- **Create Teacher**: Add a new teacher with required fields: name and email.
- **Create Student**: Add a new student with required fields: name and email, and optional course associations.
- **Create Course**: Add a new course with required fields: name and level.
- **Retrieve Students**: Fetch a list of all students with their details.
- **Retrieve Courses**: Fetch a list of all courses with their details.

## Quick Install

To get started, you need to install the required dependencies. You can do this using pip:

```bash
pip install fastapi[all] sqlalchemy
```

Or, if you prefer using conda:

```bash
conda install -c conda-forge fastapi sqlalchemy
```

## Setting Up the Environment

1. **Clone the Repository**: If you haven't already, clone the repository containing the code.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**: Follow the Quick Install instructions above.

4. **Run the Application**: Start the FastAPI application.

   ```bash
   python main.py
   ```

   The application will be running at `http://127.0.0.1:8000`.

## Using the API

You can interact with the API using tools like Postman or curl. Below are some example requests.

### Create a Teacher

```bash
curl -X POST "http://127.0.0.1:8000/teachers/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'
```

### Create a Student

```bash
curl -X POST "http://127.0.0.1:8000/students/" -H "Content-Type: application/json" -d '{"name": "Jane Smith", "email": "jane.smith@example.com", "courses": []}'
```

### Create a Course

```bash
curl -X POST "http://127.0.0.1:8000/courses/" -H "Content-Type: application/json" -d '{"name": "Mathematics", "level": "Beginner"}'
```

### Retrieve Students

```bash
curl -X GET "http://127.0.0.1:8000/students/"
```

### Retrieve Courses

```bash
curl -X GET "http://127.0.0.1:8000/courses/"
```

## Conclusion

This Teacher Management System provides a straightforward way to manage educational entities. For further customization or features, feel free to modify the code as per your requirements.

For more detailed documentation, please refer to the FastAPI documentation [here](https://fastapi.tiangolo.com/).
```

This manual provides a comprehensive guide for users to understand the software's functionality, installation process, and how to interact with the API effectively.