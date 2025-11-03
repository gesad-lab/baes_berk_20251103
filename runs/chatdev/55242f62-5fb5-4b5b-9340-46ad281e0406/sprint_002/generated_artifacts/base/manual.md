Here's a detailed user manual for the Student web application, structured in Markdown format:

```markdown
# Student Web Application

A simple web application for managing student records, allowing users to create and store student names using FastAPI and SQLite.

## Main Functions

- **Create Student**: Users can input a student's name, which will be stored in an SQLite database.
- **JSON Responses**: The application returns JSON responses for all API interactions, making it easy to integrate with other systems or front-end applications.

## Installation

To run the Student web application, you need to set up your environment and install the necessary dependencies. Follow these steps:

### Prerequisites

- **Python 3.11+**: Ensure you have Python 3.11 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the application files:

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

To start the FastAPI application, run the following command:

```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

## How to Use the Application

### Accessing the GUI

1. **Run the GUI**: In a separate terminal, run the GUI application:

```bash
python gui.py
```

2. **Enter Student Name**: A window will appear prompting you to enter a student's name.

3. **Submit**: Click the "Submit" button to create a new student record. If successful, you will see a confirmation message in the terminal.

### API Endpoints

You can also interact with the API directly using tools like Postman or curl. Here are the available endpoints:

- **Create Student**: 
  - **Endpoint**: `POST /students/`
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

### Viewing API Documentation

FastAPI automatically generates interactive API documentation. You can access it at:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## Conclusion

This Student web application provides a simple interface for managing student records. With FastAPI's powerful features and SQLite's lightweight database capabilities, you can easily extend this application to include more functionalities as needed.

For any issues or questions, please refer to the documentation or contact support.
```

This manual provides a comprehensive overview of the application, installation instructions, usage guidelines, and API documentation, ensuring users can effectively utilize the software.