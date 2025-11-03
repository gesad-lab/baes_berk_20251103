```markdown
# Student Course Management Application

A comprehensive application designed to manage students and their associated courses. This application allows users to create courses, assign them to students, and manage student information efficiently.

## Main Functions

- **Add Courses**: Users can create new courses by providing a course name and level.
- **Student Management**: Manage student information including name and email.
- **Course Enrollment**: Students can be enrolled in multiple courses, establishing a many-to-many relationship between students and courses.

## Installation Instructions

To set up the environment and run the application, follow these steps:

### Prerequisites

Ensure you have Python 3.6 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Install Dependencies

You will need to install the required Python packages. You can do this using pip:

```bash
pip install sqlalchemy tkinter pydantic
```

### Step 3: Set Up the Database

The application uses SQLite for database management. The database will be created automatically when you run the application for the first time. However, you can manually create the database by running:

```bash
python -c "from database import create_database; create_database()"
```

### Step 4: Run the Application

To start the application, execute the following command:

```bash
python main.py
```

This will launch the graphical user interface (GUI) for the Student Course Management Application.

## How to Use the Application

1. **Adding a Course**:
   - Enter the course name in the "Course Name" field.
   - Enter the course level in the "Course Level" field.
   - Click the "Add Course" button to save the course.

2. **Managing Students**:
   - You can manage student information by creating a Student entity (this functionality can be implemented in future updates).
   - Each student can be assigned to multiple courses through the many-to-many relationship established in the database.

3. **Viewing Courses**:
   - The application can be extended to include a feature to view all courses and the students enrolled in each course.

## Future Enhancements

- Implement a feature to view all students and their enrolled courses.
- Add functionality to update and delete courses and students.
- Enhance the GUI for better user experience.

## Support

For any issues or feature requests, please contact the support team at [support@chatdev.com](mailto:support@chatdev.com).

Thank you for using the Student Course Management Application!
```
