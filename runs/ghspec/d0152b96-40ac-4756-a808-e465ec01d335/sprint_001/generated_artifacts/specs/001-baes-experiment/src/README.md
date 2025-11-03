# Student Management System

## Project Purpose
The Student Management System is a web application designed to help educational institutions manage student information efficiently. It provides features for creating, updating, retrieving, and deleting student records through a RESTful API. 

This system aims to simplify administrative processes, reduce paperwork, and enable better tracking of student data.

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Clone the Repository
```bash
git clone https://github.com/yourusername/student_management.git
cd student_management
```

### Install Dependencies
Before running the application, install the necessary dependencies. Make sure you are in the root directory of the project.

```bash
pip install -r requirements.txt
```

### Environment Variables
Set up your environment variables for database configuration and other settings. Create a `.env` file in the root directory with the following structure:

```
DATABASE_URL=sqlite:///./test.db
```

Adjust the `DATABASE_URL` according to your database configuration (e.g., PostgreSQL, MySQL).

### Run the Application
You can start the application by running the entry point:

```bash
python src/main.py
```

## API Usage Examples
The application exposes several API endpoints for managing student records. Below are examples of how to use these endpoints.

### Create a Student
**Endpoint:** `POST /students`

**Request Body:**
```json
{
  "name": "John Doe",
  "age": 20,
  "email": "john.doe@example.com"
}
```

**Response:**
- 201 Created
- Body: JSON object of the created student record.

### Retrieve a Student
**Endpoint:** `GET /students/{student_id}`

**Response:**
- 200 OK
- Body: JSON object of the student record.

### Update a Student
**Endpoint:** `PUT /students/{student_id}`

**Request Body:**
```json
{
  "name": "John Smith",
  "age": 21,
  "email": "john.smith@example.com"
}
```

**Response:**
- 200 OK
- Body: JSON object of the updated student record.

### Delete a Student
**Endpoint:** `DELETE /students/{student_id}`

**Response:**
- 204 No Content

## Running Tests
To ensure that everything is working as expected, you can run the unit tests:

```bash
pytest tests/test_student.py
```

## Contribution
If you would like to contribute to the project, please fork the repository and create a pull request. Your contributions are welcome!

## License
This project is licensed under the MIT License - see the LICENSE file for details.