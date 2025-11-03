```markdown
# Course Management System

A simple application for managing students and courses, allowing users to add and view student and course information through a graphical user interface.

## Main Functions

- **Student Management**: Add and manage student information, including name and email.
- **Course Management**: Create and manage courses with a name and level.
- **Database Integration**: The application uses a SQLite database to store student and course data, ensuring persistence across sessions.

## Installation

To run the Course Management System, you need to set up your environment and install the necessary dependencies. Follow the steps below:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/course-management-system.git
cd course-management-system
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

Make sure to include the following dependencies in your `requirements.txt`:

```
fastapi
uvicorn
sqlalchemy
pydantic
alembic
requests
tkinter
```

### Step 4: Run Database Migrations

Before running the application, you need to apply the database migrations to set up the necessary tables.

```bash
alembic upgrade head
```

## How to Use the Application

1. **Start the Application**: Run the main application file to launch the GUI.

```bash
python main.py
```

2. **Adding Students**:
   - Enter the student's name and email in the respective fields.
   - Click the "Add Student" button to save the information.
   - The application will display a confirmation message if the student is added successfully.

3. **Adding Courses**:
   - Enter the course name and level in the respective fields.
   - Click the "Add Course" button to save the information.
   - The application will display a confirmation message if the course is added successfully.

4. **Viewing Information**: The application will show feedback messages in the output area for both student and course additions.

## Database Structure

The application uses a SQLite database with the following tables:

- **students**: Stores student information (id, name, email).
- **courses**: Stores course information (id, name, level).

## Additional Notes

- Ensure that the database file (`students.db`) is created in the project directory after running the migrations.
- The application is designed to preserve existing student data during migrations.

## Support

For any issues or feature requests, please open an issue in the GitHub repository or contact the development team.

```
