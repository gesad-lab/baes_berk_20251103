Here's a detailed user manual for the software, following the structure you provided:

```markdown
# Course and Student Registration System

A simple application for managing student and course registrations using FastAPI and a Tkinter GUI.

## Main Functions

This application allows users to:
- Register new students with their names and emails.
- Create new courses with specified names and levels.
- View the list of registered students and courses.

## Quick Install

To set up the environment and install the required dependencies, follow these steps:

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🤔 What is this?

This application is designed to facilitate the registration of students and courses in an educational context. It leverages FastAPI for the backend API and Tkinter for a simple graphical user interface (GUI). 

### Key Features:
- **Student Registration**: Users can input student names and emails to register them in the system.
- **Course Creation**: Users can create courses by specifying the course name and level.
- **Data Persistence**: The application uses SQLite to store student and course data, ensuring that existing student data is preserved during database migrations.

## 📖 How to Use the Application

### Starting the Application

1. **Run the FastAPI server**:
   In your terminal, navigate to the directory containing `main.py` and run:
   ```bash
   uvicorn main:app --reload
   ```
   This will start the FastAPI server on `http://127.0.0.1:8000`.

2. **Launch the GUI**:
   In a separate terminal, run the following command to start the Tkinter GUI:
   ```bash
   python gui.py
   ```

### Using the GUI

- **Registering a Student**:
  1. Enter the student's name in the "Student Name" field.
  2. Enter the student's email in the "Student Email" field.
  3. Click the "Create Student" button. A confirmation message will appear if the registration is successful.

- **Creating a Course**:
  1. Enter the course name in the "Course Name" field.
  2. Enter the course level in the "Course Level" field.
  3. Click the "Create Course" button. A confirmation message will appear if the course creation is successful.

### Viewing Registered Data

- You can view the list of registered students and courses by accessing the following endpoints:
  - **Students**: `GET http://127.0.0.1:8000/students/`
  - **Courses**: `GET http://127.0.0.1:8000/courses/`

## 🛠️ Troubleshooting

- If you encounter issues with the GUI not connecting to the FastAPI server, ensure that the server is running and accessible at `http://127.0.0.1:8000`.
- Check for any error messages in the terminal where the FastAPI server is running for additional debugging information.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

We welcome contributions to improve the application. Please fork the repository and submit a pull request with your changes.

For any questions or support, please contact the development team at [support@chatdev.com](mailto:support@chatdev.com).
```

This manual provides a comprehensive overview of the application, installation instructions, usage guidelines, and troubleshooting tips, ensuring that users can effectively utilize the software.