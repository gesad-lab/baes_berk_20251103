# README.md

# API Documentation

## Overview
This API allows users to manage teacher records. It is built using Flask as the web framework and uses SQLAlchemy for database abstraction. The database used for this project is SQLite, which simplifies setup and testing during development.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- A virtual environment is recommended.

### Installation

1. **Clone the Repository:**
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up a Virtual Environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages:**
   ```
   pip install -r requirements.txt
   ```

4. **Set Up Database:**
   - Ensure you have SQLite installed.
   - Run the following command to create the database and tables:
     ```
     flask db upgrade
     ```

### Running the Application

To start the server, ensure you are in your virtual environment and run:
```
flask run
```

The API will be available at `http://127.0.0.1:5000`.

## API Endpoints

### Create Teacher
- **Endpoint:** `/api/v1/teachers`
- **Method:** `POST`
- **Description:** Creates a new teacher record.
  
#### Request Body
```json
{
  "name": "string",       // Name of the teacher
  "subject": "string",    // Subject taught by the teacher
  "email": "string"       // Email of the teacher
}
```

#### Response
- **201 Created:** When the teacher is successfully created.
- **400 Bad Request:** When the input is invalid. The response will include error details.

### Documentation
API documentation is automatically generated using Swagger. Access it by navigating to `/apidocs` in your web browser after running the application.

## Testing

To run tests, execute:
```
pytest
```

This will run all the test cases defined in the tests directory. Ensure that the database is properly set up before running tests.

## Conclusion

This API facilitates the efficient management of teacher records. For further customization, feel free to dive into the codebase and explore the endpoints.