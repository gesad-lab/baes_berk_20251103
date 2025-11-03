Here's a detailed user manual for the software, specifically tailored to the task of adding an email field to the Student entity.

```markdown
# Student Management System

A simple application for managing student records, including their names and email addresses.

## Quick Install

To get started with the Student Management System, you'll need to install the necessary environment dependencies. You can do this using pip:

```bash
pip install sqlalchemy pydantic uvicorn
```

## 🤔 What is this?

The Student Management System is designed to manage student information, allowing you to create, read, update, and delete student records. The recent update includes the addition of an email field to the Student entity, which is now a required field.

### Main Functions

- **Create Student**: Add a new student record with a name and email.
- **Retrieve Students**: Get a list of all students along with their details.
- **Update Student**: Modify existing student records.
- **Delete Student**: Remove a student record from the system.

## 📖 Documentation

### Setting Up the Environment

1. **Clone the Repository**:
   Clone the repository to your local machine using:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Make sure to install the required dependencies as mentioned in the Quick Install section.

3. **Database Setup**:
   The application uses SQLite for database management. The database file will be created automatically when you run the application for the first time.

### Running the Application

To start the application, run the following command in your terminal:

```bash
uvicorn main:app --reload
```

This command will start the server, and you can access the application at `http://127.0.0.1:8000`.

### API Endpoints

- **Create Student**:
  - **Endpoint**: `POST /students`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Retrieve Students**:
  - **Endpoint**: `GET /students`
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
    ]
    ```

- **Update Student**:
  - **Endpoint**: `PUT /students/{id}`
  - **Request Body**:
    ```json
    {
      "name": "John Doe Updated",
      "email": "john.updated@example.com"
    }
    ```

- **Delete Student**:
  - **Endpoint**: `DELETE /students/{id}`

### Database Migration

The application includes a migration script that automatically adds the email field to the existing Student entity without losing any existing data. This is handled in the `main.py` file, which checks if the email column exists and adds it if it doesn't.

### Conclusion

This Student Management System provides a straightforward way to manage student records with the added functionality of email management. For further assistance, please refer to the code comments or reach out to the development team.
```

This manual provides a comprehensive overview of the software, installation instructions, and usage guidelines, ensuring that users can effectively utilize the Student Management System.