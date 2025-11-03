# README.md

# Student Management Application

## Overview
The Student Management Application allows users to manage student records by providing CRUD (Create, Read, Update, Delete) functionalities specifically focused on the 'name' field. This web application efficiently handles JSON responses and utilizes an SQLite database for persistence, following best practices for structure and organization.

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/student_app.git
   cd student_app
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   uvicorn src.main:app --reload
   ```

## Endpoints
- `POST /students`: Create a new student record.
- `GET /students`: Retrieve all student records.
- `PUT /students/{id}`: Update an existing student record by ID.
- `DELETE /students/{id}`: Delete a student record by ID.

## Testing
To ensure all CRUD operations work as expected, navigate to the tests directory and run the following command:

```bash
pytest tests/test_api.py
```

## User Scenarios & Testing
1. **Create a Student Record**:
   - **Test**: Ensure that submitting a valid name creates a new student entry.
2. **Retrieve All Student Records**:
   - **Test**: Ensure that the response returns a JSON array of all student records.
3. **Update a Student Record**:
   - **Test**: Ensure that updating a valid student ID with a new name reflects the changes in the database.
4. **Delete a Student Record**:
   - **Test**: Ensure that a valid delete request removes the student record and that subsequent retrieval attempts return an empty result or an error.