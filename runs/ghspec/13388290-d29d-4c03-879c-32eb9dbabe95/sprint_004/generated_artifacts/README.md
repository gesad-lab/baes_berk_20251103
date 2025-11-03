# README.md

# Project Title

## Overview

This project is a microservice that manages Students and Courses, enabling enrollment and course assignment. The latest features allow for a many-to-many relationship between Student and Course entities through a junction table.

## Features

- Many-to-many relationship between Students and Courses.
- API endpoints for course assignment and retrieval for students.

## Setup Instructions

To set up the project, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. **Create a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Install the required packages using pip.

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database**

   Update your database configuration in the `.env` file (or equivalent) to include the necessary connection information. Make sure to include the new `StudentCourses` junction table.

   ```plaintext
   DATABASE_URL=sqlite:///site.db  # Example for SQLite, adjust for your DB
   ```

5. **Run Migrations**

   Apply migrations to update the database schema. This will create the necessary tables, including the `StudentCourses` junction table while preserving existing data.

   ```bash
   flask db upgrade
   ```

6. **Start the Application**

   You can run the application using:

   ```bash
   flask run
   ```

7. **API Endpoints**

   The following endpoints are available to manage student course assignments:

   - **POST /students/{id}/courses**: Assign courses to a student by student ID.
   - **GET /students/{id}/courses**: Retrieve all courses associated with a specific student.
   - **DELETE /students/{id}/courses/{course_id}**: Remove a specific course from a student's enrollment.

## Testing

To run the test suite and ensure everything is working correctly, execute:

```bash
pytest
```

## Contributions

Contributions are welcome! Please submit a pull request or open an issue for discussion.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.