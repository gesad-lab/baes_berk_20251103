# README.md

# Student Management System

This application is a simple student management system that allows users to create and manage student records with essential information such as name and email. It includes API endpoints for creating students and retrieving student records.

## Prerequisites

- Python 3.8 or higher
- A PostgreSQL database (or any other supported database) for storing student data
- Required Python packages as specified in `requirements.txt`

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd student_management
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure your environment variables. Create a `.env` file in the root directory:
   ```plaintext
   DATABASE_URL=your_database_url_here
   ```

## Running the Application

1. Ensure your database is running and accessible.
2. Run the application:
   ```bash
   uvicorn src.main:app --reload
   ```

3. The application will perform migrations on startup, adding any necessary fields to the database schema.

## API Endpoints

### Create a Student

- **Endpoint:** `POST /students`
- **Request Body:**
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```
- **Responses:**
  - `201 Created`: Returns the created student's ID, name, and email.
  - `400 Bad Request`: If the email is empty or improperly formatted.

### Retrieve Students

- **Endpoint:** `GET /students`
- **Responses:**
  - `200 OK`: Returns a JSON array of student records including names and email addresses.

## Migration Guidelines

When starting the application for the first time, the system will automatically execute migrations. This process includes the following:

- Update the existing `Student` entity in the database schema to include the required `email` field of type string.
- Existing student records will have a default value assigned to the new `email` field until updated.

## Testing

To test the application after setting up, run:
```bash
pytest
```

Ensure that you have covered all scenarios, including creating students with valid information and testing error handling for invalid inputs.

## Error Handling

If you encounter issues during migrations or application startup, please check your database configuration and ensure that the necessary migrations have been applied successfully.

--- 

This README now includes updated API usage examples, migration guidelines, and a structured setup process to help users initialize the application without errors and check migration results effectively.