# README.md

# Project Title

## Overview

This project is designed to manage educational entities including students, courses, and now teachers. It provides a set of API endpoints and a database schema to facilitate the management of this data.

## Functional Requirements

1. **Create Teacher Entity**
   - Define a new entity called `Teacher` with the following required fields:
     - `name`: String (required)
     - `email`: String (required)

2. **Database Schema Update**
   - Updated the database schema to include a new table for Teachers with the following fields:
     - `id`: Integer (Automatically generated, primary key)
     - `name`: String
     - `email`: String

3. **Database Migration**
   - Executed a database migration that creates the new Teacher table while preserving existing data in the Student and Course tables. Ensured that no data is lost during this operation.

4. **API Endpoints**
   - **POST /teachers**
     - The endpoint accepts a JSON body containing the name and email to create a new teacher.
     - On successful creation, it returns the newly created teacher object.
     - **Request Example**:
       ```json
       {
         "name": "John Doe",
         "email": "john.doe@example.com"
       }
       ```
     - **Response Example**:
       ```json
       {
         "id": 1,
         "name": "John Doe",
         "email": "john.doe@example.com"
       }
       ```

   - **GET /teachers/{teacherId}**
     - This endpoint returns the details of the specified teacher, including their name and email.
     - **Response Example**:
       ```json
       {
         "id": 1,
         "name": "John Doe",
         "email": "john.doe@example.com"
       }
       ```

5. **JSON Responses**
   - All API responses are maintained in JSON format, confirming successful teacher creation and accurate retrieval of teacher details.

## Key Entities

- **Teacher**
  - `id`: Integer (Automatically generated, primary key)
  - `name`: String (required)
  - `email`: String (required)

- Updated **Student** (no changes needed for existing fields)
  - `id`: Integer (Automatically generated, primary key)
  - Other existing fields...

- Updated **Course** (no changes needed for existing fields)
  - `id`: Integer (Automatically generated, primary key)
  - Other existing fields...

## Setup Instructions

1. **Clone the Repository**:  
   Use the following command to clone the repository:
   ```bash
   git clone <repository-url>
   ```
   
2. **Install Dependencies**:  
   Navigate to the project directory and install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations**:  
   Execute the database migrations:
   ```bash
   alembic upgrade head
   ```

4. **Start the Application**:  
   You can start the Flask application using:
   ```bash
   flask run
   ```

5. **API Testing**:  
   You can test the API using Postman or any other API client.

## Development Phases Roadmap

1. **Week 1**: Project setup, database schema implementation, and migrations for the Teacher entity.
2. **Week 2**: API endpoint modifications and validation handling.
3. **Week 3**: Writing tests and implementation of logging, migration tests.
4. **Week 4**: Documentation updates, integration testing, and final code reviews.

## License

This project is licensed under the MIT License - see the LICENSE file for details.