Here's a detailed user manual for the software, including installation instructions, main functions, and usage guidelines.

```markdown
# Student Management Application

A simple application for managing student records, including their names and email addresses.

## Main Functions

- **Create Student**: Add a new student record with a name and email address.
- **Get Students**: Retrieve a list of all students with their details.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/student-management-app.git
   cd student-management-app
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi sqlalchemy uvicorn
   ```

4. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

## Database Migration

To add the new email field to the existing Student entity and preserve existing data, run the migration script:

```bash
python main.py
```

This will update the database schema to include the new email column in the Student table.

## How to Use the Application

### Creating a Student

To create a new student, send a POST request to the `/students/` endpoint with the following JSON body:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

You can use tools like [Postman](https://www.postman.com/) or [curl](https://curl.se/) to make this request. Here's an example using curl:

```bash
curl -X POST "http://127.0.0.1:8000/students/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'
```

### Retrieving Students

To retrieve a list of all students, send a GET request to the `/students/` endpoint:

```bash
curl -X GET "http://127.0.0.1:8000/students/"
```

This will return a JSON array of student records, including their IDs, names, and email addresses.

## Conclusion

This application provides a straightforward way to manage student records. You can easily extend its functionality by adding more features as needed. For any issues or questions, please refer to the documentation or reach out for support.
```

This manual provides a comprehensive overview of the application, installation steps, and usage instructions, ensuring that users can effectively utilize the software.