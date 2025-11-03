# README.md

# Project Title

## Introduction
This project provides a robust framework for managing course information, as well as student registration and performance tracking.

## Migration Instructions

To incorporate the new `Course` entity and update the database schema, follow these steps:

### 1. Create Migration for Course Table

To create the necessary migration for adding the `Course` table, utilize the database migration tool currently integrated into the project. This process ensures that existing data remains intact, specifically the `Student` data.

1. Make sure to have the migration tool installed and configured for your environment.
2. Run the following command to generate the migration:

   ```bash
   your_migration_tool create migration_name
   ```

3. Update the generated migration file to include the following schema for the `Course` table:

   ```sql
   CREATE TABLE courses (
       id SERIAL PRIMARY KEY,
       name VARCHAR(255) NOT NULL,
       level VARCHAR(255) NOT NULL,
   );
   ```

4. Apply the migration using the command:

   ```bash
   your_migration_tool upgrade
   ```

### 2. Verify Database Changes

Once the migration has been applied, verify that the new `Course` table has been created without affecting the existing `Student` data. You can do this by executing:

```sql
SELECT * FROM courses;
SELECT * FROM students;
```

Both tables should contain their respective data as expected.

### 3. Testing the Course Entity

After the migration, you should test the new Course routes to ensure that the entity can be created, retrieved, and updated correctly. Ensure to include validation for the `name` and `level`, adhering to the following:

- Both fields are mandatory and cannot be empty. If validation fails, the response should be a `400 Bad Request` with an appropriate error message:

```json
{
   "error": {
     "code": "E001",
     "message": "Name and level are required."
   }
}
```

### 4. Running Tests

Finally, ensure that all tests for the `Course` management functionality pass successfully. This includes unit tests for creation, retrieval, and validation of course data. Aim for a minimum of 70% test coverage for the new functionalities. Run your test suite:

```bash
pytest
```

## API Endpoints

### Create a Course
- **Route**: `POST /api/v1/courses`
- **Request Body**:
```json
{
  "name": "Introduction to Programming",
  "level": "Beginner"
}
```
- **Response**:
   - **201 Created**
```json
{
  "id": 1,
  "name": "Introduction to Programming",
  "level": "Beginner"
}
```
   - **400 Bad Request** for validation errors.

### Retrieve a Course
- **Route**: `GET /api/v1/courses/{id}`
- **Response**:
   - **200 OK**
```json
{
  "id": 1,
  "name": "Introduction to Programming",
  "level": "Beginner"
}
```
   - **404 Not Found** if Course does not exist.

### Update a Course
- **Route**: `PUT /api/v1/courses/{id}`
- **Request Body**:
```json
{
  "name": "Advanced Programming",
  "level": "Intermediate"
}
```
- **Response**:
   - **200 OK**
```json
{
  "id": 1,
  "name": "Advanced Programming",
  "level": "Intermediate"
}
```
   - **400 Bad Request** for validation errors.

## Conclusion

By following the above instructions, you will successfully update your database for the `Course` entity while maintaining the integrity of existing data. Ensure the API is well-documented and thoroughly tested.