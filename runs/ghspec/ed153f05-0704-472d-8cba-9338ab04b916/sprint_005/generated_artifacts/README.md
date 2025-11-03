# README.md

# Project Title

## Description

A brief description of your project goes here.

## API Endpoints

### Create a Teacher

- **POST /teachers**
  
  Create a new teacher in the system.

  #### Request
  - **Body**: 
    ```json
    {
      "name": "string",
      "email": "string"
    }
    ```

  #### Response
  - **Success**: 
    ```json
    {
      "message": "Teacher created successfully."
    }
    ``` 
    (Status Code: 201 Created)

  - **Error Responses**:
    - If the name is missing: 
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Name is required."
      }
    }
    ```
    (Status Code: 400 Bad Request)

    - If the email is missing: 
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Email is required."
      }
    }
    ```
    (Status Code: 400 Bad Request)

## Teacher Entity Definition

The `Teacher` entity must have the following fields:
- `name`: String (required)
- `email`: String (required)

### Database Schema Update

- The database schema will include a new `Teacher` table with the following columns:
  - `id`: Integer (Primary Key)
  - `name`: String (not null)
  - `email`: String (not null, must be unique)

### Database Migration

- Ensure that the migration process preserves existing `Student` and `Course` data while adding the new `Teacher` table.

## Testing

Make sure to write unit tests for the new teacher model and API endpoint with emphasis on successful creation and validation failure scenarios.

## Environment Setup

Make sure the `.env` file is updated with any necessary configuration settings.

## Additional Notes

- Ensure that all new features are documented in this README.
- Validate the API responses using the suggested structures.