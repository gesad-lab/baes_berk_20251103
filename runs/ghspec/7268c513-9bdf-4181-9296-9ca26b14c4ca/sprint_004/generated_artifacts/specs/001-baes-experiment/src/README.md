# README.md

# Project Title

## Overview
This project aims to manage student enrollments in courses, allowing students to keep track of their academic commitments effectively. 

## Setup Instructions

To set up this project locally, follow these steps:

### Prerequisites
- Python 3.7 or higher
- Flask
- SQLAlchemy
- A SQLite database (default for this project)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   - Run the following command to create the database and the necessary tables:
     ```bash
     flask db upgrade
     ```

5. **Run the application**
   ```bash
   flask run
   ```

6. **Access the API**
   - The API will be accessible at `http://127.0.0.1:5000`.

### API Endpoints

- **Enroll Student in Course**  
  - Endpoint: `POST /students/{studentId}/courses`  
  - Request Body: 
    ```json
    {
      "courseId": "integer"  // courseId is required
    }
    ```
  - Response: 
    - `201 Created` with the updated student details and enrolled course
    - `400 Bad Request` if courseId is missing or invalid
  
- **Get Enrolled Courses**  
  - Endpoint: `GET /students/{studentId}/courses`  
  - Response: 
    - `200 OK` with a JSON array of enrolled course records for the specified student

### Testing
To run the tests, ensure you are in your virtual environment and execute:
```bash
pytest
```

### User Stories
- **User Story 1**: As a student, I want to view my enrolled courses so that I can keep track of my academic commitments.
- **User Story 2**: As an admin, I want to enroll a student in a course so that the student can participate in the course.
- **User Story 3**: As an admin, I want to ensure that existing student records remain unaffected despite modifying the database schema to add relationships between students and courses.
- **User Story 4**: As a student, I want to confirm I cannot enroll in a non-existent course so that the system can maintain data integrity.

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.