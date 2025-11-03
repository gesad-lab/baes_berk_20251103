```markdown
# Teacher Management Application

Welcome to the Teacher Management Application! This software allows users to manage students, courses, and teachers efficiently. Below is a detailed user manual that covers the main functions of the software, how to install the necessary environment dependencies, and how to use the application.

## Main Functions

The Teacher Management Application provides the following functionalities:

1. **Manage Students**:
   - Add new students with their names and email addresses.
   - Retrieve a list of all students.

2. **Manage Courses**:
   - Add new courses with their names and levels.
   - Retrieve a list of all courses.

3. **Manage Teachers**:
   - Add new teachers with their names and email addresses.
   - Retrieve a list of all teachers.

## Installation

To get started with the Teacher Management Application, you need to install the required dependencies. Follow the steps below:

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/teacher-management-app.git
cd teacher-management-app
```

### Step 2: Set Up a Virtual Environment

It's recommended to create a virtual environment to manage dependencies. You can use `venv` or `conda` for this purpose.

Using `venv`:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Using `conda`:

```bash
conda create --name teacher_management python=3.8
conda activate teacher_management
```

### Step 3: Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install fastapi sqlalchemy pydantic requests
```

### Step 4: Run the Application

To run the application, execute the following command:

```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

## How to Use the Application

Once the application is running, you can interact with it through the GUI. Follow these steps to use the application:

1. **Adding a Student**:
   - Enter the student's name in the "Enter Student Name" field.
   - Enter the student's email in the "Enter Student Email" field.
   - Click the "Add Student" button to save the student.

2. **Adding a Course**:
   - Enter the course name in the "Enter Course Name" field.
   - Enter the course level in the "Enter Course Level" field.
   - Click the "Add Course" button to save the course.

3. **Adding a Teacher**:
   - Enter the teacher's name in the "Enter Teacher Name" field.
   - Enter the teacher's email in the "Enter Teacher Email" field.
   - Click the "Add Teacher" button to save the teacher.

4. **Displaying Students**:
   - Click the "Display Students" button to retrieve and display a list of all students in the output area.

## Conclusion

The Teacher Management Application is designed to simplify the management of students, courses, and teachers. By following the steps outlined in this manual, you can easily set up and use the application. If you have any questions or need further assistance, please feel free to reach out.

Happy managing!
```