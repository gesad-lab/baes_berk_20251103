```markdown
# Student Course Management Application

This application allows users to manage students and their course enrollments. It provides functionalities to create students, create courses, and associate students with courses.

## Main Functions

- **Create Student**: Add a new student with a name, email, and a list of course IDs they are enrolled in.
- **Create Course**: Add a new course with a name and level.
- **View Students**: Retrieve a list of all students along with their enrolled courses.
- **View Courses**: Retrieve a list of all available courses.

## Installation

To run this application, you need to set up your environment and install the necessary dependencies. Follow these steps:

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
   Make sure you have `pip` installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt`, you can manually install the necessary packages:
   ```bash
   pip install fastapi sqlalchemy alembic pydantic requests
   ```

4. **Run Database Migrations**:
   Ensure that the database schema is up to date by running the migration script:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:
   You can run the application using:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use the Application

1. **Access the GUI**:
   Once the application is running, you can access the GUI by navigating to `http://127.0.0.1:8000` in your web browser.

2. **Adding a Student**:
   - Enter the student's name in the "Enter Student Name" field.
   - Enter the student's email in the "Enter Student Email" field.
   - Enter the course IDs (comma-separated) in the "Enter Course IDs" field.
   - Click the "Submit" button to add the student.

3. **Adding a Course**:
   You can add courses by implementing a similar form in the GUI or by creating a separate endpoint in the FastAPI application.

4. **Viewing Students and Courses**:
   You can implement additional GUI elements or API endpoints to retrieve and display lists of students and courses.

## Additional Information

- **Database**: The application uses SQLite for data storage. The database file is located at `./students.db`.
- **Data Migration**: The application includes migration scripts to ensure that existing data is preserved when adding new fields or tables.
- **Error Handling**: If there are issues adding a student or course, appropriate error messages will be displayed in the GUI.

For further documentation and examples, please refer to the FastAPI documentation at [FastAPI Documentation](https://fastapi.tiangolo.com/).

```
