Here's a detailed user manual for the Student Management web application, structured in Markdown format as requested:

```markdown
# Student Management Application

A simple web application for managing student records, built using Python, FastAPI, and SQLite.

## Main Functions

The Student Management Application allows users to:

- **Add a Student**: Enter a student's name and add it to the database.
- **View Students**: Retrieve and display a list of all students stored in the database.

## Installation

To run the application, you need to set up your environment and install the required dependencies. Follow these steps:

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd student_app
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment for your project:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required Python packages using pip:

```bash
pip install fastapi[all] sqlalchemy
```

### Step 4: Run the Application

Start the FastAPI server by running the following command:

```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

### Step 5: Run the GUI

In a separate terminal, run the GUI application:

```bash
python gui.py
```

## How to Use the Application

1. **Adding a Student**:
   - Open the GUI application.
   - Enter the student's name in the input field.
   - Click the "Add Student" button.
   - A success message will appear if the student is added successfully.

2. **Viewing Students**:
   - Click the "Show Students" button.
   - A list of all students will be displayed in the list box.

## API Endpoints

The application exposes the following API endpoints:

- **POST /students/**: Add a new student.
  - Request Body: 
    ```json
    {
      "name": "Student Name"
    }
    ```
  - Response: 
    ```json
    {
      "id": 1,
      "name": "Student Name"
    }
    ```

- **GET /students/**: Retrieve a list of students.
  - Response: 
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

This Student Management Application provides a simple interface for managing student records. By following the installation and usage instructions, you can easily set up and run the application on your local machine. For any issues or feedback, please reach out to the development team.

```

This manual provides a comprehensive overview of the application, including its main functions, installation steps, usage instructions, and API endpoints. Let me know if you need any further modifications or additional information!