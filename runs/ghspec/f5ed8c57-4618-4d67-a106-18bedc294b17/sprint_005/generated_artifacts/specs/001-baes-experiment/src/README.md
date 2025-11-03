# Complete content for README.md

# Teacher API Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [API Endpoints](#api-endpoints)
   - [Create Teacher Endpoint](#create-teacher-endpoint)
   - [Retrieve Teacher Endpoint](#retrieve-teacher-endpoint)
   - [Update Teacher Endpoint](#update-teacher-endpoint)
   - [Delete Teacher Endpoint](#delete-teacher-endpoint)
3. [Database Migration Process](#database-migration-process)

## Introduction
This document provides an overview of the Teacher API, including its endpoints and the necessary steps for database migration.

## API Endpoints

### Create Teacher Endpoint
- **Request**: `POST /teachers`
- **Required Body**: 
  ```json
  {
    "name": "string",
    "email": "string"
  }
  ```
- **Response**: 
  ```json
  {
    "id": "integer",
    "name": "string",
    "email": "string"
  }
  ```

### Retrieve Teacher Endpoint
- **Request**: `GET /teachers/{teacher_id}`
- **Response**: 
  ```json
  {
    "id": "integer",
    "name": "string",
    "email": "string"
  }
  ```

### Update Teacher Endpoint
- **Request**: `PUT /teachers/{teacher_id}`
- **Required Body**: 
  ```json
  {
    "name": "string (optional)",
    "email": "string (optional)"
  }
  ```
- **Response**: 
  ```json
  {
    "id": "integer",
    "name": "string",
    "email": "string"
  }
  ```

### Delete Teacher Endpoint
- **Request**: `DELETE /teachers/{teacher_id}`
- **Response**: 
  ```json
  {
    "message": "Teacher successfully deleted"
  }
  ```

## Database Migration Process
To accommodate the new Teacher API, the database schema needs to be updated to include a `teachers` table. This section outlines the migration process.

### Migration Strategy
1. **Migration Tool**: Use [Alembic](https://alembic.sqlalchemy.org/en/latest/) for database migrations.
   
2. **Create Migration Script**: Execute the command to generate a migration script which will create the new `teachers` table with the proper constraints:
   ```bash
   alembic revision --autogenerate -m "create teachers table"
   ```

3. **Teachers Table Schema**:
   - **id**: Integer, primary key.
   - **name**: String, required.
   - **email**: String, required, must be unique.

4. **Data Preservation**: Ensure that this migration does not impact existing data in the `students` or `courses` tables. 

5. **Testing Migrations**: After the migration script is applied, verify the following:
   - The `teachers` table is created correctly.
   - Existing data for students and courses remains intact.

### Execution of Migrations
- Run the Alembic upgrade command:
  ```bash
  alembic upgrade head
  ```

## Conclusion
This documentation provides the necessary information for integrating the Teacher API and updating the database schema with minimal disruption to existing data. Ensure to follow the migration steps carefully to maintain data integrity.