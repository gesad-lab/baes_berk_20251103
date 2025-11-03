# README.md

# Student Management Web Application

This application provides functionalities to manage student records and courses effectively, including the creation, retrieval, and updating of course details.

## Features

- **Student Management**: Create, retrieve, and manage student records.
- **Course Management**: Create, retrieve, and manage course records.
  
## User Scenarios & Testing

1. **As an Admin User**, I want to create a new course record with a name and level so that I can manage courses effectively.
   - Test: Verify that I can submit a name and level and successfully create a new course record.

2. **As an Admin User**, I want to retrieve a list of all course records to view existing course information.
   - Test: Ensure that all course records returned in a JSON format include the name and level fields.

3. **As an Admin User**, I want to handle cases where I input invalid data for the name or level fields to confirm the application responds appropriately.
   - Test: Submit an empty name or level field and confirm that meaningful error messages are returned.

4. **As an Admin User**, I want to update an existing course record to change its name or level so that I can maintain accurate course information.
   - Test: Verify that I can successfully update the name or level for an existing course record.

## Functional Requirements

1. **Course Entity Creation**
   - A new Course entity must be created with the following fields:
     - **Name**: String (required)
     - **Level**: String (required)
   - Users must be able to POST a request to create a new course with both name and level fields.

2. **Course Entity Retrieval**
   - Users must be able to GET a list of all courses.
   - The response should return all course records in JSON format, including the name and level fields.

3. **Error Handling**
   - The application must validate inputs for the name and level fields and return meaningful error messages in JSON format when either field is left empty.

4. **Database Schema Update**
   - The database schema must be updated to include the new Course table without affecting existing data, specifically preserving the Student data.
   - A proper database migration must be implemented for the addition of the Course entity.

## Testing

Tests are organized in the `tests/` directory and include:

- `test_routes.py`: Tests for the course-related API endpoints.
- `test_services.py`: Tests covering the business logic for course management.

### Running Tests

You can run the tests using pytest:

```bash
pytest tests/
```

## Installation

To set up the environment, clone the repository and install the required packages:

```bash
git clone <repository-url>
cd <repository-directory>
pip install -r requirements.txt
```

## Configuration

Ensure to configure any necessary environment variables before starting the application.

## Conclusion

This Student Management Web Application is designed to maintain efficient course and student records management. The integration of course management enhances the overall functionality, allowing administrators to effectively oversee and update course details.