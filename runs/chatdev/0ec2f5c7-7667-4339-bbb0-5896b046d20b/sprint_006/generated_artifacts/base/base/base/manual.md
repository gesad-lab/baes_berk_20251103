Here's a detailed user manual for the ChatDev Student Application, including installation instructions, main functions, and usage guidelines.

```markdown
# ChatDev Student Application

A powerful application for managing student and course data, designed to streamline educational administration.

## Main Functions

The ChatDev Student Application allows users to:

- **Manage Students**: Create, read, update, and delete student records.
- **Manage Courses**: Create and manage courses with specific attributes.
- **Database Management**: Automatically handle database migrations and schema updates while preserving existing data.

## Quick Install

To set up the ChatDev Student Application, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/chatdev_student_app.git
   cd chatdev_student_app
   ```

2. **Install Dependencies**:
   Create a virtual environment (optional but recommended) and install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, if you are using conda:
   ```bash
   conda create --name chatdev_env python=3.8
   conda activate chatdev_env
   conda install --file requirements.txt
   ```

## Database Setup

The application uses SQLite for database management. The database file will be created automatically upon the first run.

### Database Migration

To set up the database schema, run the following command:
```bash
python main.py
```
This command will create the necessary tables (`students` and `courses`) and ensure that existing student data is preserved during the migration.

## How to Use the Application

1. **Running the Application**:
   To start the application, run:
   ```bash
   python main.py
   ```

2. **Creating a Student**:
   You can create a new student by sending a POST request to the appropriate endpoint (e.g., `/students`) with the required fields (name and email).

3. **Creating a Course**:
   To create a new course, send a POST request to the `/courses` endpoint with the following JSON body:
   ```json
   {
       "name": "Course Name",
       "level": "Beginner"
   }
   ```

4. **Viewing Students and Courses**:
   You can retrieve the list of students and courses by sending a GET request to `/students` and `/courses`, respectively.

5. **Updating and Deleting Records**:
   Use the appropriate HTTP methods (PUT for updates and DELETE for deletions) to modify or remove student and course records.

## Additional Resources

For more detailed documentation, including API references and examples, please refer to the official documentation.

## Support

If you encounter any issues or have questions, please reach out to our support team via the contact form on our website.

---

Thank you for using the ChatDev Student Application! We hope it enhances your educational management experience.
```

This manual provides a comprehensive overview of the ChatDev Student Application, ensuring users can effectively install and utilize the software.