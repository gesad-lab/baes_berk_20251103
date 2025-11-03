```markdown
# Student and Course Management Application

Welcome to the Student and Course Management Application! This software allows you to manage student and course data efficiently through a user-friendly interface and a robust backend API.

## Main Functions

- **Student Management**: Add and retrieve student information including name and email.
- **Course Management**: Create and retrieve courses with specified names and levels.
- **Database Management**: The application uses SQLite for data storage, ensuring that existing student data is preserved during migrations.

## Installation of Environment Dependencies

To get started with the application, you need to install the required dependencies. Follow these steps:

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
   alembic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the API**:
   Start the FastAPI server by running:
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`.

2. **Run the GUI**:
   In a separate terminal, run the GUI application:
   ```bash
   python gui.py
   ```

3. **Using the GUI**:
   - **Add a Student**:
     - Enter the student's name and email in the respective fields.
     - Click the "Submit Student" button to add the student. A success message will appear if the operation is successful.
   
   - **Add a Course**:
     - Enter the course name and level in the respective fields.
     - Click the "Submit Course" button to add the course. A success message will appear if the operation is successful.

4. **Database Migration**:
   The application includes a migration script to create the courses table without affecting existing student data. To apply the migration, run:
   ```bash
   alembic upgrade head
   ```

## Additional Information

For more detailed documentation, including API endpoints and usage examples, please refer to the code comments and the FastAPI documentation.

Thank you for using the Student and Course Management Application! We hope it meets your needs for managing student and course data effectively.
```