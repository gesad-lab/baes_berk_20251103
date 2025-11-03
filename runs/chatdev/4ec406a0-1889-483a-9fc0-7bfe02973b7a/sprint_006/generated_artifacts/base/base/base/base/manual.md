Here is the `manual.md` file that provides a detailed user manual for the Student Management application, including an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Student Management Application

A simple GUI application for managing student records, including adding and fetching student details.

## Main Functions

- **Add Student**: Allows users to input a student's name and email address and save it to the database.
- **Fetch Students**: Retrieves and displays a list of all students stored in the database, including their names and email addresses.

## Installation Instructions

To run the Student Management application, you need to set up your environment and install the required dependencies. Follow these steps:

### Step 1: Install Python

Ensure you have Python 3.7 or higher installed on your machine. You can download it from the official [Python website](https://www.python.org/downloads/).

### Step 2: Create a Virtual Environment (Optional but Recommended)

Creating a virtual environment helps manage dependencies for your project. You can create one using the following commands:

```bash
# Navigate to your project directory
cd path/to/your/project

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Required Dependencies

Install the necessary Python packages using pip. Run the following command:

```bash
pip install fastapi[all] sqlalchemy pydantic requests
```

### Step 4: Set Up the Database

The application uses SQLite as the database. The database schema will be created automatically when you run the application for the first time.

## How to Use the Application

1. **Run the Application**: Start the FastAPI server by running the following command in your terminal:

   ```bash
   uvicorn main:app --reload
   ```

   This will start the server at `http://127.0.0.1:8000`.

2. **Open the GUI**: The GUI will open automatically if you run the `main.py` file. If not, you can run the following command in a separate terminal to start the GUI:

   ```bash
   python main.py
   ```

3. **Add a Student**:
   - Enter the student's name in the "Student Name" field.
   - Enter the student's email in the "Student Email" field.
   - Click the "Add Student" button to save the information.

4. **Fetch Students**: Click the "Fetch Students" button to retrieve and display the list of all students, including their names and email addresses.

## Additional Notes

- Ensure that your FastAPI server is running before using the GUI application.
- The email field is required when adding a student, and it must be in a valid email format.

## Support

If you encounter any issues or have questions, please reach out to our support team at support@chatdev.com.

Happy managing your students!
```

This manual provides a comprehensive overview of the Student Management application, guiding users through installation and usage while ensuring they understand the main functionalities.