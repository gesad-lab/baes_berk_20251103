Here's a detailed user manual for the software, including installation instructions, main functions, and usage guidelines.

```markdown
# Teacher Management System

A simple application for managing teachers, students, and courses.

## Overview

The Teacher Management System allows users to create and manage entities related to teachers, students, and courses. This application is built using Python and utilizes SQLAlchemy for database management. The main features include:

- Creating and managing Teacher entities with required fields (name and email).
- Preserving existing Student and Course data during database migrations.
- A user-friendly dashboard interface for interaction.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo/teacher-management-system.git
   cd teacher-management-system
   ```

2. **Create a Virtual Environment (Optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   Make sure to have the following dependencies in your `requirements.txt`:
   ```
   sqlalchemy
   pydantic
   ```

## Main Functions

### 1. Create a Teacher

You can create a new teacher by providing the required fields: `name` and `email`. The email field is validated to ensure it is in the correct format.

### 2. Database Migration

The application includes a migration script that updates the database schema to include a new `Teacher` table while preserving existing `Student` and `Course` data. The migration is handled in the `main.py` file.

### 3. User Interface

The application features a dashboard (defined in `gui.py`) that allows users to interact with the system. Users can create teachers, view existing records, and manage courses.

## How to Use

1. **Run the Application:**
   To start the application, run the following command:
   ```bash
   python main.py
   ```

2. **Access the Dashboard:**
   Open your web browser and navigate to `http://localhost:8000` (or the specified port) to access the dashboard.

3. **Creating a Teacher:**
   - Navigate to the "Create Teacher" section.
   - Fill in the required fields (name and email).
   - Click the "Submit" button to create the teacher entity.

4. **Viewing Teachers:**
   - Navigate to the "View Teachers" section to see a list of all created teachers.

5. **Database Migration:**
   The migration script will automatically run when you start the application, ensuring that the database schema is up to date.

## Documentation

For more detailed documentation, including API references and advanced usage, please refer to the following resources:

- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

## Support

If you encounter any issues or have questions, please reach out to our support team via the contact form on our website.

---

Thank you for using the Teacher Management System! We hope it helps you manage your educational entities effectively.
```

This manual provides a comprehensive overview of the software, installation instructions, main functions, and usage guidelines, ensuring that users can easily set up and utilize the Teacher Management System.