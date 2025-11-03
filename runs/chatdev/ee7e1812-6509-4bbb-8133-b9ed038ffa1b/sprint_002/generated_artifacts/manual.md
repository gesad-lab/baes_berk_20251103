```markdown
# Student Management Application

A simple application for managing student records, including the ability to create and retrieve student information.

## Main Functions

- **Create Student**: Allows users to add a new student with a name and email address.
- **Retrieve Students**: Fetches a list of all students, displaying their names and email addresses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Use the following command to install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the Application**:
   Start the application by executing the following command:
   ```bash
   python main.py
   ```

2. **Create a New Student**:
   To create a new student, send a POST request to the `/students/` endpoint with the following JSON body:
   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

   Example using `curl`:
   ```bash
   curl -X POST "http://localhost:8000/students/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'
   ```

3. **Retrieve Students**:
   To get a list of all students, send a GET request to the `/students/` endpoint:
   ```bash
   curl -X GET "http://localhost:8000/students/"
   ```

   This will return a JSON array of students with their IDs, names, and email addresses.

## Database Migration

The application includes a migration script to add the email field to the existing Student entity without losing any existing data. The migration is handled automatically when you run the application.

## Requirements

Make sure you have the following dependencies in your `requirements.txt`:

```
fastapi
uvicorn
sqlalchemy
pydantic
```

You can install these dependencies using the command:
```bash
pip install -r requirements.txt
```

## Conclusion

This Student Management Application provides a straightforward way to manage student records. With the ability to create and retrieve student information, it serves as a foundational tool for educational institutions or any organization needing to track student data.
```
