```markdown
# ChatDev Student-Course Management System

Welcome to the ChatDev Student-Course Management System! This software allows you to manage students and their associated courses efficiently. Below is a detailed user manual that covers the main functions of the software, installation instructions, and usage guidelines.

## Main Functions

### 1. Student Management
- **Create Student**: Add a new student with their name, email, and associated courses.
- **Get Students**: Retrieve a list of all students along with their details and enrolled courses.

### 2. Course Management
- **Create Course**: Add a new course with its name and level.
- **Get Courses**: Retrieve a list of all available courses.

### 3. Relationship Management
- Students can be associated with multiple courses, and courses can have multiple students, allowing for a many-to-many relationship.

## Installation Instructions

### Prerequisites
Ensure you have Python 3.7 or higher installed on your machine.

### Step 1: Clone the Repository
Clone the repository containing the code to your local machine using the following command:
```bash
git clone https://github.com/your-repo/chatdev-student-course-management.git
cd chatdev-student-course-management
```

### Step 2: Create a Virtual Environment (Optional but Recommended)
Create a virtual environment to manage dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies
Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```

### Step 4: Run Database Migration
Run the migration script to set up the database schema:
```bash
python migration_script.py
```

### Step 5: Start the Application
Run the FastAPI application using Uvicorn:
```bash
python main.py
```
The application will be accessible at `http://127.0.0.1:8000`.

## Usage Guidelines

### API Endpoints

#### Student Endpoints
- **Create Student**: 
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "course_ids": [1, 2]
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com",
      "courses": [...]
    }
    ```

- **Get Students**: 
  - **Endpoint**: `GET /students/`
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "courses": [...]
      },
      ...
    ]
    ```

#### Course Endpoints
- **Create Course**: 
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Intermediate"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Mathematics",
      "level": "Intermediate"
    }
    ```

- **Get Courses**: 
  - **Endpoint**: `GET /courses/`
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "Mathematics",
        "level": "Intermediate"
      },
      ...
    ]
    ```

## Conclusion

The ChatDev Student-Course Management System provides a robust solution for managing students and their courses. By following the installation and usage guidelines, you can easily set up and utilize the system for your educational needs. For further assistance, please refer to the documentation or contact support.

Happy coding!
```