```markdown
# Student Management Application

A comprehensive application for managing students and courses, allowing users to add, view, and manage relationships between students and their courses.

## Main Functions

- **Add Student**: Users can add new students by providing their name and email.
- **View Students**: Users can view a list of all registered students.
- **Add Course**: Users can add new courses by providing the course name and level.
- **View Courses**: Users can view a list of all available courses.
- **Manage Relationships**: Students can be associated with multiple courses through a many-to-many relationship.

## Installation Instructions

To set up the Student Management Application, follow these steps:

### Prerequisites

Ensure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Create a Virtual Environment

It is recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### Step 4: Set Up the Database

Run the following command to create the database and apply migrations:

```bash
alembic upgrade head
```

This command will set up the database schema and create the necessary tables.

## How to Use the Application

1. **Run the Application**: Start the application by running the main script:

   ```bash
   python main.py
   ```

2. **Access the GUI**: The application will open a graphical user interface (GUI) where you can interact with the features.

3. **Add Students**:
   - Enter the student's name and email in the respective fields.
   - Click the "Add Student" button to save the student.

4. **View Students**: Click the "View Students" button to display a list of all registered students.

5. **Add Courses**:
   - Enter the course name and level in the respective fields.
   - Click the "Add Course" button to save the course.

6. **View Courses**: Click the "View Courses" button to display a list of all available courses.

7. **Manage Course Relationships**: You can extend the functionality to manage relationships between students and courses as needed.

## Additional Information

For further details on the application, including advanced features and customization options, please refer to the documentation provided in the repository.

If you encounter any issues or have questions, feel free to reach out for support.

Happy Learning!
```