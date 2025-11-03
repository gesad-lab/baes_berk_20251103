# Student Entity Web Application Setup Guide

## Overview
This document provides a setup guide for the Student Entity Web Application, which manages student records through a RESTful API. The application allows for the creation and retrieval of student records, focusing on the student’s name.

## Prerequisites
- Python 3.7 or higher
- SQLite (comes pre-installed with Python)
- pip (Python package installer)

## Installation Steps

1. **Clone the Repository**
   Start by cloning the repository from the version control system.
   ```bash
   git clone https://github.com/yourusername/student-entity-web-app.git
   cd student-entity-web-app
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   It's a good practice to use a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   Use pip to install the required packages.
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   Create a `.env` file in the root directory of the project and specify the necessary environment variables. An example is provided in `.env.example`.
   ```
   DATABASE_URL=sqlite:///students.db
   ```

5. **Run Database Migrations**
   The application automatically creates the SQLite database schema for the Student entity on startup. Ensure that the database path specified in the `.env` file is correct.

6. **Start the Application**
   Run the application using the following command:
   ```bash
   python app.py
   ```

7. **Test the Endpoints**
   Use tools like Postman or curl to test the endpoints:
   - **Create Student**
     - Endpoint: `POST /students`
     - Payload: `{"name": "John Doe"}`
   - **Retrieve Students**
     - Endpoint: `GET /students`

## Health Check
You can access the health check endpoint to confirm that the application is running properly:
- **Health Check Endpoint**
  - URL: `GET /health`

## Error Handling
The application includes error handling for invalid inputs. For instance, if the "name" field is missing when creating a student, the application will return a JSON error response with a status code of 400.

## Success Criteria
Ensure the following criteria are met:
1. Successful student creation returns a status of 201 with the expected details.
2. Retrieval of students returns a status of 200 with a JSON array of students.
3. Submission of invalid input results in an appropriate 400 error message.
4. The application successfully creates the database schema and connects to the SQLite database upon startup.

## Conclusion
By following these steps, you will have a fully functional Student Entity Web Application. For more information on usage and additional features, refer to the rest of the documentation or the inline comments in the code.