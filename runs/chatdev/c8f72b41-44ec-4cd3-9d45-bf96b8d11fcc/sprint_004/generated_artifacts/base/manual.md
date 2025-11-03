Here's the `manual.md` file that outlines the main functions of the software, installation instructions, and usage guidelines:

```markdown
# Student Course Management Application

This application provides a simple API for managing Student and Course entities. It allows users to create and retrieve information about students and courses, making it a useful tool for educational institutions or any organization that needs to manage course-related data.

## Main Functions

- **Student Management**
  - Create a new student with a name and email.
  - Retrieve a list of all students.

- **Course Management**
  - Create a new course with a name and level.
  - Retrieve a list of all courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd student_app
   ```

2. **Create a Virtual Environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   You can install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the Application**
   Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

   The application will be running at `http://127.0.0.1:8000`.

2. **Access the API Endpoints**
   You can interact with the API using tools like Postman or cURL, or directly through the interactive API documentation provided by FastAPI at `http://127.0.0.1:8000/docs`.

### API Endpoints

- **Students**
  - **Create a Student**
    - **Endpoint:** `POST /students/`
    - **Request Body:**
      ```json
      {
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
      ```
    - **Response:** Returns the created student object.

  - **Get All Students**
    - **Endpoint:** `GET /students/`
    - **Response:** Returns a list of all students.

- **Courses**
  - **Create a Course**
    - **Endpoint:** `POST /courses/`
    - **Request Body:**
      ```json
      {
        "name": "Mathematics",
        "level": "Beginner"
      }
      ```
    - **Response:** Returns the created course object.

  - **Get All Courses**
    - **Endpoint:** `GET /courses/`
    - **Response:** Returns a list of all courses.

## Conclusion

This application provides a straightforward way to manage students and courses through a RESTful API. With the ability to create and retrieve data, it serves as a foundational tool for educational management systems. For further customization or enhancements, feel free to modify the code as per your requirements.

For any issues or support, please reach out to the development team.
```

This manual provides a comprehensive overview of the application, its functionalities, installation steps, and usage instructions, ensuring that users can easily understand and utilize the software.