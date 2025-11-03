# Updated README.md

# Project Title

## Overview

This project is a Flask-based web application designed to manage educational entities, including students and courses. This README provides an overview of setup, functionality, and development instructions.

## Incremental Development Instructions

### Sprint 3 Enhancements

1. **Introduce Course Entity**: 
   - A new `Course` entity has been integrated into the application to enhance course management functionalities.

2. **Database Schema Migration**:
   - The database schema has been updated to include a new `Course` table using Alembic for migration, ensuring existing data, particularly related to the `Student` entity, remains intact.

3. **Alignment with Existing Technology**:
   - The new functionalities align with the established technology stack from previous sprints and adhere to existing coding conventions and naming practices.

4. **Migration Strategy Documentation**:
   - The migration strategy is designed to accommodate the new `Course` entity while preserving existing `Student` data.

5. **API Endpoints Integration**:
   - New endpoints for managing courses have been integrated, ensuring they work smoothly with existing workflows, especially regarding `Student` records.

## Development Steps

1. **Set Up Environment**: 
   - Ensure the virtual environment is active and install necessary dependencies:
     ```bash
     pip install Flask SQLAlchemy Marshmallow pytest
     ```

2. **Database Schema Migration**:
   - Create the new `Course` model in your `models.py` file.
   - Use Alembic to create a migration script that adds the `Course` table while preserving existing data integrity.

3. **API Development**:
   - Implement the following endpoints:
     - **POST** `/courses`: Create a new course record (requires both `name` and `level`).
     - **GET** `/courses/{id}`: Retrieve information for a specific course by ID.
   - Use Marshmallow for schema validation and serialization of course data.

4. **Testing**:
   - Write unit tests to ensure proper functionality of the new course features, targeting:
     - Creation and retrieval of courses.
     - Achieve at least 70% coverage for business logic, with critical validation routes exceeding 90% coverage.

5. **Documentation**:
   - Update the API documentation to reflect the new Courses endpoints.
   - Include setup instructions and usage examples for the new functionality in this README file.

## Running the Application

To run the application, use the following command in your terminal:
```bash
flask run
```

Ensure that your environment variables are correctly configured.

## Health Check Endpoint

Use the following endpoint to verify the health of the API:
- **GET** `/health`: Returns the status of the API.

### Example Response:
```json
{
    "status": "ok"
}
```

## Contribution

Feel free to fork the repository and submit pull requests. Ensure your code follows the established patterns and includes proper test coverage.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.