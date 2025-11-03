# Student Management Web Application

## Overview
The Student Management Web Application is a simple platform designed to enable users to create and manage `Student` entities. Each `Student` has a required `name` field, which must be provided during the creation process. The application employs a RESTful API to facilitate operations on student data and automatically manages the underlying database schema, returning JSON responses for data representation.

## Setup Instructions

### Prerequisites
- Python 3.7 or later
- pip (Python package installer)
- A relational database (e.g., SQLite, PostgreSQL, or MySQL)

### Installation Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/student-management.git
   cd student-management
   ```

2. **Install dependencies**:
   Install the required Python packages using pip. It is recommended to use a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root and specify the necessary configuration, such as database connection details:
   ```
   DATABASE_URI=your_database_uri
   ```

4. **Run database migrations**:
   To create the necessary database schema, execute the following command:
   ```bash
   python manage.py migrate
   ```

5. **Start the application**:
   You can start the web application using:
   ```bash
   python manage.py runserver
   ```

## Usage Information

### API Endpoints
The application provides several endpoints to manage student data:

1. **Create a Student**
   - **Endpoint**: `POST /api/students`
   - **Request Body**: 
     ```json
     {
       "name": "Student Name"
     }
     ```
   - **Response**:
     - **Success**: Returns the created student's details.
     - **Error**: If the name field is missing, returns an error message.

2. **Retrieve All Students**
   - **Endpoint**: `GET /api/students`
   - **Response**: Returns a JSON array of all student objects in the database.

### Example Requests
- **Creating a Student**:
   ```bash
   curl -X POST http://localhost:5000/api/students -H "Content-Type: application/json" -d '{"name": "John Doe"}'
   ```
  
- **Retrieving Students**:
   ```bash
   curl -X GET http://localhost:5000/api/students
   ```

### DB Initialization
The database schema is automatically created upon starting the application. Ensure that the database details are correctly set in your environment variables to facilitate schema generation.

## Conclusion
The Student Management Web Application provides a simple yet effective way to manage student data via a RESTful API. Follow the setup instructions carefully to get the application up and running, and refer to the API endpoints for interaction with student records.