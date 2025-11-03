Here’s a detailed user manual for the software, including an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Course Management System

A simple application for managing courses and students.

## Overview

The Course Management System allows users to create and manage courses and students. The main functionalities include:

- Creating new courses with a name and level.
- Storing student information, including their names and email addresses.
- Preserving existing student data during database migrations.

## Main Functions

1. **Course Creation**: Users can create new courses by providing a name and level.
2. **Student Management**: Users can add students with their names and email addresses.
3. **Database Migration**: The system supports database migrations that preserve existing student data while adding new features.

## Quick Install

To set up the Course Management System, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/course-management-system.git
   cd course-management-system
   ```

2. **Install Dependencies**:
   Ensure you have Python installed (version 3.6 or higher). Then, install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt` file, you can manually install the necessary packages:
   ```bash
   pip install sqlalchemy alembic pydantic
   ```

3. **Set Up the Database**:
   The application uses SQLite for the database. The database will be created automatically when you run the application for the first time.

## Usage

### Running the Application

To start the application, run the following command:
```bash
python main.py
```

### Creating a Course

1. **Access the Course Creation Interface**: Once the application is running, navigate to the course creation section.
2. **Fill in the Course Details**:
   - **Name**: Enter the name of the course (required).
   - **Level**: Enter the level of the course (required).
3. **Submit**: Click the submit button to create the course.

### Adding a Student

1. **Access the Student Management Interface**: Navigate to the student management section.
2. **Fill in the Student Details**:
   - **Name**: Enter the name of the student (required).
   - **Email**: Enter the email address of the student (required).
3. **Submit**: Click the submit button to add the student.

### Database Migration

The application includes migration scripts to update the database schema without losing existing data. To run the migration, execute the following command:
```bash
alembic upgrade head
```

This command will create the `courses` table and add the `email` column to the `students` table, ensuring that existing student data is preserved.

## Documentation

For more detailed documentation, including API references and advanced usage, please refer to the following sections:

- [Getting Started](#)
- [How-To Examples](#)
- [Reference](#)
- [Resources](#)

## Support

If you encounter any issues or need further assistance, please reach out to our support team by filling out the support form [here](#).

Thank you for using the Course Management System!
```

This manual provides a comprehensive guide for users to understand the software's functionalities, installation process, and usage instructions.