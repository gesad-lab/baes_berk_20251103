# README.md

## Project Documentation

### Overview
This project involves managing educational entities such as students, teachers, and courses. It provides various functionalities for creating, retrieving, and managing data associated with these entities.

### Schema Migration
In this sprint, we have introduced a new `teachers` table to the existing database schema. This table will allow for management of teacher information and their associations with courses and students.

### Migration Verification
After performing the migration, please verify that the new `teachers` table is accessible and functional. Below are the scenarios and test cases that you can use to validate the successful addition of this table.

### User Scenarios & Testing

1. **Creating a New Teacher**:
   - As an admin user, I want to add a new teacher to the system so that they can be associated with courses and students.
   - **Test Case**: Submit a request to create a teacher with a valid name and email. Verify that the response confirms the creation and that the data is properly stored in the database.

2. **Validating Teacher Data**:
   - As a user, I want to receive an error message when I try to create a teacher without required fields to ensure data integrity.
   - **Test Case**: Attempt to create a teacher without a name or email. Check that the system returns appropriate error messages indicating which fields are missing.

3. **Retrieving Teacher Information**:
   - As a user, I want to retrieve a teacher's information to verify their details and ensure correct entry into the system.
   - **Test Case**: Send a GET request for an existing teacher. Confirm that the system returns the correct name and email for the teacher.

4. **Database Migration Validation**:
   - As a developer, I want to ensure that existing data remains intact after the Teacher entity is added.
   - **Test Case**: After the migration, check that all existing records in the Student and Course tables remain accessible and unchanged.

### Functional Requirements
1. **Create a Teacher**:
   - **Endpoint**: `POST /teachers`
   - **Request Body**: JSON with the structure `{"name": "string", "email": "string"}` (both fields are required).
   - **Response**: JSON confirming the creation of the teacher with the teacher ID and stored details.

2. **Retrieve Teacher Information**:
   - **Endpoint**: `GET /teachers/{id}`
   - **Response**: JSON with teacher's details including `name` and `email`, or an error message if the teacher is not found.

3. **Error Handling**:
   - If required fields are missing when creating a teacher, respond with an HTTP 400 status and a JSON error message:
     - For missing name: `{"error": {"code": "E001", "message": "Name is required"}}`
     - For missing email: `{"error": {"code": "E002", "message": "Email is required"}}`

### Conclusion
Ensure to follow the above scenarios to validate the accessibility and functionality of the new `teachers` table after migration. Each test case is designed to confirm that the system behaves as expected following the schema update.