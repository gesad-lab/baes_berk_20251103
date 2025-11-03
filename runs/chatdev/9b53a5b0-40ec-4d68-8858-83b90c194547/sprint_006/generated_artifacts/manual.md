```markdown
# ChatDev Course Management System

Welcome to the ChatDev Course Management System! This software allows users to manage students, courses, and teachers efficiently. You can add, view, and manage relationships between these entities through a user-friendly GUI.

## Main Functions

### 1. Student Management
- **Add Student**: Enter the student's name and email to add them to the system.
- **View Students**: Retrieve and display a list of all students in the system.

### 2. Course Management
- **Add Course**: Enter the course name, level, and optionally assign a teacher by their ID.
- **View Courses**: Retrieve and display a list of all courses, including associated teacher IDs.

### 3. Teacher Management
- **Add Teacher**: Enter the teacher's name and email to add them to the system.
- **View Teachers**: Retrieve and display a list of all teachers in the system.

## Installation Instructions

To set up the environment and install the necessary dependencies, follow these steps:

### Step 1: Clone the Repository
Clone the repository to your local machine using the following command:
```bash
git clone https://github.com/your-repo/chatdev-course-management.git
cd chatdev-course-management
```

### Step 2: Create a Virtual Environment (Optional but Recommended)
Create a virtual environment to manage dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies
Install the required dependencies listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

## How to Use the Application

### Step 1: Run the FastAPI Backend
Start the FastAPI backend server using Uvicorn:
```bash
uvicorn main:app --reload
```
This will run the server locally at `http://127.0.0.1:8000`.

### Step 2: Launch the GUI
Run the GUI application:
```bash
python main.py
```
This will open a Tkinter window where you can interact with the application.

### Step 3: Interact with the Application
- **Adding Students**: Enter the student's name and email, then click "Add Student".
- **Viewing Students**: Click "View Students" to see the list of all students.
- **Adding Courses**: Enter the course name, level, and optional teacher ID, then click "Add Course".
- **Viewing Courses**: Click "View Courses" to see the list of all courses.
- **Adding Teachers**: Enter the teacher's name and email, then click "Add Teacher".
- **Viewing Teachers**: Click "View Teachers" to see the list of all teachers.

## Conclusion

The ChatDev Course Management System provides a comprehensive solution for managing students, courses, and teachers. With its intuitive GUI and robust backend, you can efficiently handle educational data and relationships. For any issues or feature requests, please contact our support team.

Happy managing!
```