# Student Management Web Application

## Overview
This is a Student Management Web Application designed to manage student data efficiently. It offers a structured API for performing CRUD operations on student records.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Running Tests](#running-tests)
- [License](#license)

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.x installed
- Pip package manager installed
- A working internet connection

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student_management.git
   cd student_management
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # Activate it using:
   # Windows: venv\Scripts\activate
   # macOS/Linux: source venv/bin/activate
   ```

3. Install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To start the application, run the following command:
```bash
python src/app.py
```
This will launch the web server, and you can access the application at `http://localhost:5000`.

### Docker Setup (Optional)
If you want to run the application within a Docker container, use the provided Dockerfile.
1. Build the Docker image:
   ```bash
   docker build -t student_management .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 student_management
   ```

## API Documentation
The API offers the following endpoints:
- **GET /api/students**: Retrieve a list of students.
- **POST /api/students**: Create a new student.
- **GET /api/students/{id}**: Retrieve a student by ID.
- **PUT /api/students/{id}**: Update a student by ID.
- **DELETE /api/students/{id}**: Delete a student by ID.

## Running Tests
To run the tests, execute the following command:
```bash
pytest
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.