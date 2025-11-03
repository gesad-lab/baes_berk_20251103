# README.md

# Student Management Application

## Overview

The Student Management application is a web application that allows users to create, read, update, and delete (CRUD) student records. Each student has a required name field, thus providing a simple and effective way to manage student data.

## Technologies Used

- **Web Framework**: Flask
- **ORM/Database**: SQLAlchemy with SQLite
- **Testing Framework**: Pytest
- **API Documentation**: Flask-RESTful

## Deployment Instructions

To deploy the Student Management application, follow these steps:

1. **Clone the Repository**

   Clone the respository to your local machine using:
   ```bash
   git clone <repository-url>
   cd student_management
   ```

2. **Set Up the Environment**

   Create a virtual environment to isolate your package dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Install the necessary dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configuration**

   Create an environment file based on the provided example:
   ```bash
   cp .env.example .env
   ```

   The `.env` file will contain all the necessary configuration settings, ensuring the application runs without manual intervention.

5. **Run the Application**

   Start the application with:
   ```bash
   python src/app.py
   ```

   The application will automatically initialize the database schema on startup, so there is no further configuration required.

6. **Access the API**

   The application will be accessible at `http://localhost:5000`.

7. **API Endpoints**

   Ensure to review the API endpoints for creating, listing, updating, and deleting student records as documented in the API section below.

## API Documentation

- **POST /students**: Create a new student
- **GET /students**: List all students
- **PUT /students/<id>**: Update an existing student
- **DELETE /students/<id>**: Delete a student

## Testing the Application

To run the tests for the application, use:
```bash
pytest tests/
```

This will run all unit and integration tests ensuring the correct functionality of the student management features.

## Conclusion

The Student Management application is designed to be simple and effective for managing student records, while ensuring ease of deployment and use. For any issues or questions, please refer to the documentation or contact the maintainers.