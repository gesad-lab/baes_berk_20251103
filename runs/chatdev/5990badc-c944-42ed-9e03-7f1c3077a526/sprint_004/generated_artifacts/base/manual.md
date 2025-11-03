Here’s a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Student Course Management Application

A simple application for managing students and courses, allowing users to create and manage course entities with specific attributes.

## Main Functions

- **Add Course**: Users can create new courses by providing a name and level.
- **Database Management**: The application manages a SQLite database to store student and course information, ensuring that existing student data is preserved during schema updates.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/student-course-management.git
   cd student-course-management
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have the following dependencies in your `requirements.txt`:
   ```
   sqlalchemy
   pydantic
   tkinter
   ```

## How to Use the Application

1. **Run the Application**:
   Start the application by executing the main script:
   ```bash
   python main.py
   ```

2. **Using the GUI**:
   - Upon launching, the application will display a graphical user interface (GUI).
   - Enter the **Course Name** and **Course Level** in the respective fields.
   - Click the **Add Course** button to create a new course.
   - If the input fields are empty, a warning message will prompt you to fill in all fields.

3. **Database Migration**:
   - The application automatically checks and upgrades the database schema to include the new Course table without affecting existing student data.

## Application Structure

- **gui.py**: Contains the graphical user interface code for interacting with the application.
- **schemas.py**: Defines Pydantic schemas for validating requests and responses.
- **database.py**: Manages database connections, session handling, and schema migrations.
- **models.py**: Defines the database models for students and courses.
- **main.py**: The entry point of the application that initializes the GUI and database.
- **course.py**: Contains functions related to course management.

## Additional Information

For more details on how to extend the application or contribute to its development, please refer to the documentation in the repository or contact the development team.

**Support**: If you encounter any issues or have questions, please reach out via the support channel provided in the repository.

```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and a brief description of the application's structure. Let me know if you need any modifications or additional information!