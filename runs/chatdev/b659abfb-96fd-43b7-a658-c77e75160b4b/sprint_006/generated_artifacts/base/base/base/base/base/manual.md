Here's a detailed user manual for the Student Management web application, structured in Markdown format:

```markdown
# Student Management Web Application

A simple web application for managing student records, allowing users to add students with their names.

## Main Functions

- **Add Student**: Users can input a student's name and submit it to the database.
- **API Interaction**: The application exposes a RESTful API for creating and managing student records.
- **Database Persistence**: Student records are stored in an SQLite database, which is created automatically on startup.

## Installation Guide

To set up the environment and run the application, follow these steps:

### Prerequisites

- Ensure you have Python 3.11+ installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
- Install `pip`, the package installer for Python, if it's not already installed.

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd <repository-directory>
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
pip install fastapi[all] sqlalchemy requests
```

### Step 4: Run the Application

Start the FastAPI application by running the following command:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### Step 5: Access the API Documentation

Once the server is running, you can access the interactive API documentation at:

```
http://127.0.0.1:8000/docs
```

## How to Use the Application

### Adding a Student

1. **Open the GUI**: Run the GUI application by executing the following command in a separate terminal:

    ```bash
    python gui.py
    ```

2. **Input Student Name**: In the GUI window, enter the student's name in the provided text field.

3. **Submit**: Click the "Add Student" button to submit the name.

4. **Feedback**: The application will display a message indicating whether the student was added successfully or if there was an error.

### API Usage

You can also interact with the API directly using tools like Postman or curl. Here’s how to add a student using a POST request:

```bash
curl -X POST "http://127.0.0.1:8000/students" -H "Content-Type: application/json" -d '{"name": "John Doe"}'
```

### Response Format

The API will return a JSON response containing the student's ID and name:

```json
{
  "id": 1,
  "name": "John Doe"
}
```

## Conclusion

This Student Management web application provides a simple interface for managing student records. By following the installation and usage instructions, you can easily set up and interact with the application. For any issues or questions, feel free to reach out for support.
```

This manual provides a comprehensive overview of the application, installation steps, and usage instructions, ensuring that users can effectively utilize the software.