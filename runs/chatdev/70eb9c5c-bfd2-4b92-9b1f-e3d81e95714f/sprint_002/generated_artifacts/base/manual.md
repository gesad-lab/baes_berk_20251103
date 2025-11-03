Here’s a detailed user manual for the Student Management web application, structured in Markdown format:

```markdown
# Student Management Application

A simple web application for managing student records, allowing users to add and view students by their names.

## Main Functions

- **Add Student**: Users can input a student's name and submit it to the database.
- **View Students**: Users can retrieve a list of all students stored in the database.

## Installation Guide

To run the Student Management Application, you'll need to set up your environment and install the necessary dependencies. Follow these steps:

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

First, clone the repository containing the application code:

```bash
git clone https://github.com/yourusername/student_management.git
cd student_management
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment to manage your dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required Python packages using pip:

```bash
pip install fastapi[all] sqlalchemy requests
```

### Step 4: Run the Application

To start the FastAPI application, run the following command:

```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

## Using the Application

### Accessing the GUI

1. **Run the GUI Application**: Open a new terminal window and run the GUI application:

   ```bash
   python gui.py
   ```

2. **Add a Student**:
   - Enter the student's name in the input field.
   - Click the "Add Student" button.
   - If successful, the application will display a confirmation message with the added student's name.

3. **View Students**: The GUI currently does not display the list of students directly. You can implement this feature by modifying the GUI code to fetch and display the list of students from the API.

### API Endpoints

The application exposes the following API endpoints:

- **POST /students/**: Add a new student.
  - **Request Body**: 
    ```json
    {
      "name": "Student Name"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "Student Name"
    }
    ```

- **GET /students/**: Retrieve a list of students.
  - **Query Parameters**: 
    - `skip`: Number of records to skip (default is 0).
    - `limit`: Maximum number of records to return (default is 10).
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "Student Name"
      },
      ...
    ]
    ```

## Conclusion

This Student Management Application provides a simple interface for managing student records. You can extend its functionality by adding features such as viewing all students directly in the GUI or implementing additional fields for the Student entity.

For any issues or feature requests, please contact the development team.
```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and API details, ensuring users can effectively interact with the software.