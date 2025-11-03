Here's a detailed user manual for the Student Management System, including installation instructions, main functions, and usage guidelines.

```markdown
# Student Management System

A simple application for managing student records, including the ability to create, read, and manage student information.

## Main Functions

- **Create Student**: Add a new student record with a name and email.
- **View Students**: Retrieve a list of all students in the system.
- **Update Student**: Modify existing student information.
- **Delete Student**: Remove a student record from the system.

## Quick Install

To set up the Student Management System, you need to install the required dependencies. You can do this using pip:

```bash
pip install fastapi sqlalchemy pydantic
```

Alternatively, if you are using Anaconda, you can install the dependencies with:

```bash
conda install fastapi sqlalchemy pydantic -c conda-forge
```

## Environment Setup

1. **Clone the Repository**: Start by cloning the repository containing the Student Management System code.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Use the commands mentioned above to install the necessary packages.

3. **Database Setup**: The application uses SQLite for the database. The database will be created automatically when you run the application for the first time.

## How to Use the Application

1. **Run the Application**: Start the FastAPI application by executing the following command in your terminal:

   ```bash
   uvicorn main:app --reload
   ```

   This will start the server at `http://127.0.0.1:8000`.

2. **Access the API Documentation**: Once the server is running, you can access the interactive API documentation provided by FastAPI at `http://127.0.0.1:8000/docs`.

3. **Create a Student**: To add a new student, send a POST request to `/students/` with a JSON body containing the student's name and email. For example:

   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

4. **View All Students**: You can retrieve the list of all students by sending a GET request to `/students/`.

5. **Update a Student**: To update a student's information, send a PUT request to `/students/{id}` with the updated data.

6. **Delete a Student**: To remove a student, send a DELETE request to `/students/{id}`.

## Database Migration

The application includes a migration script to add the email field to the existing Student entity. The migration will preserve existing student data. The SQL command used for migration is:

```sql
ALTER TABLE students ADD COLUMN email TEXT;  -- Allow null values for existing records
```

## Conclusion

The Student Management System is a straightforward application designed to help manage student records efficiently. With its easy-to-use API and interactive documentation, you can quickly integrate it into your projects or use it as a standalone application.

For further assistance or support, please reach out to our development team.
```

This manual provides a comprehensive overview of the Student Management System, guiding users through installation, setup, and usage. Let me know if you need any further modifications or additional sections!