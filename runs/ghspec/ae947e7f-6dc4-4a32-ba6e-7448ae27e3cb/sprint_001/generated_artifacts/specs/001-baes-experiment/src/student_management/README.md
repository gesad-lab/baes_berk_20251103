# Student Management System

Welcome to the Student Management System! This application allows you to manage student data by adding new students and retrieving their information using a simple API.

## Project Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- PostgreSQL or SQLite for the database

### Installation Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/student_management.git
   cd student_management
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**  
   Create a `.env` file in the root directory and set the following environment variables:
   ```
   DATABASE_URL=sqlite:///students.db  # Use your database URL if using PostgreSQL
   ```

5. **Run Database Migrations**  
   The application will automatically create the database schema for the Student entity on startup.

6. **Start the Application**
   ```bash
   python app.py
   ```

## API Usage

### Endpoints

1. **Create a Student**
   - **URL**: `/students`
   - **Method**: `POST`
   - **Request Body**:
     ```json
     {
       "name": "John Doe"
     }
     ```
   - **Success Response**:
     - **Code**: 201 Created
     - **Content**:
       ```json
       {
         "message": "Student created successfully",
         "student": {
           "id": 1,
           "name": "John Doe"
         }
       }
       ```

   - **Error Response**:
     - **Code**: 400 Bad Request
     - **Content**:
       ```json
       {
         "error": {
           "code": "E001",
           "message": "Name is required."
         }
       }
       ```

   - **Example using curl**:
     ```bash
     curl -X POST http://localhost:5000/students -H "Content-Type: application/json" -d '{"name": "John Doe"}'
     ```

2. **Retrieve a Student**
   - **URL**: `/students/{id}`
   - **Method**: `GET`
   - **Success Response**:
     - **Code**: 200 OK
     - **Content**:
       ```json
       {
         "student": {
           "id": 1,
           "name": "John Doe"
         }
       }
       ```

   - **Error Response**:
     - **Code**: 404 Not Found
     - **Content**:
       ```json
       {
         "error": {
           "code": "E002",
           "message": "Student not found."
         }
       }
       ```

   - **Example using curl**:
     ```bash
     curl -X GET http://localhost:5000/students/1
     ```

### Database Schema
The application manages a simple `Student` entity with the following structure:
- **id**: Auto-incremented unique identifier (integer).
- **name**: The name of the student (string, required).

## Error Handling
The application validates user inputs and provides clear error messages if input is missing or invalid, including error codes for easier debugging.

## Conclusion
You are now ready to use the Student Management System API for managing student data. If you have any questions or issues, please refer to the documentation or open an issue in the repository. Enjoy!