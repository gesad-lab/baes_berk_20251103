```markdown
# Student Management Application

A simple web application for managing student records, built using Python, FastAPI, and SQLite. This application allows users to add and retrieve student names through a user-friendly interface.

## Main Functions

- **Add Student**: Users can input a student's name, which will be stored in the SQLite database.
- **Retrieve Student**: Users can fetch a student's details by their unique ID.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd student_app
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
   Open a terminal and navigate to the `student_app` directory. Run the following command:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the FastAPI server at `http://127.0.0.1:8000`.

2. **Open the GUI**:
   In another terminal, run the GUI application:
   ```bash
   python gui.py
   ```
   This will open a Tkinter window where you can interact with the application.

## How to Use the Application

1. **Adding a Student**:
   - Enter the student's name in the input field.
   - Click the "Add Student" button.
   - If successful, a message will display the added student's name. If there is an error, an error message will appear.

2. **Retrieving a Student**:
   - Currently, the GUI does not support retrieving students directly. You can use tools like Postman or curl to interact with the API endpoints directly:
     - To retrieve a student by ID, send a GET request to:
       ```
       GET http://127.0.0.1:8000/students/{student_id}
       ```

## API Endpoints

- **POST /students/**: Create a new student.
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

- **GET /students/{student_id}**: Retrieve a student by ID.
  - Response:
    ```json
    {
      "id": 1,
      "name": "Student Name"
    }
    ```

## Conclusion

This Student Management Application provides a simple interface for managing student records. With FastAPI and SQLite, it ensures efficient data handling and a responsive user experience. For further enhancements, consider adding features like student retrieval in the GUI or additional fields for the student entity.

For any issues or feature requests, please contact the development team.
```