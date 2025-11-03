```markdown
# Student Management Web Application

This is a simple web application designed to manage student records using FastAPI and SQLite. The application allows users to add and retrieve student names through a RESTful API.

## Main Functions

- **Add Student**: Allows users to add a new student by providing their name.
- **Get Students**: Retrieves a list of all students stored in the database.

## Installation Instructions

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   requests
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the FastAPI Server**:
   In the terminal, navigate to the directory containing `main.py` and run:
   ```bash
   uvicorn main:app --reload
   ```
   The application will be accessible at `http://127.0.0.1:8000`.

2. **Access the API Documentation**:
   Open your web browser and go to `http://127.0.0.1:8000/docs` to view the automatically generated API documentation.

## Using the Application

### Adding a Student

1. Open a tool like Postman or use the provided GUI (Tkinter application).
2. Send a POST request to `http://127.0.0.1:8000/students/` with the following JSON body:
   ```json
   {
       "name": "John Doe"
   }
   ```
3. You should receive a JSON response confirming the addition of the student.

### Retrieving Students

1. Send a GET request to `http://127.0.0.1:8000/students/`.
2. You will receive a JSON array of all students in the database.

### Using the GUI

1. Run the `gui.py` script:
   ```bash
   python gui.py
   ```
2. The GUI will open, allowing you to enter a student's name and add them to the database or retrieve the list of students.

## Conclusion

This application provides a simple interface for managing student records. It demonstrates the use of FastAPI for building RESTful APIs and SQLite for data persistence. Feel free to modify and expand upon this application to suit your needs.
```