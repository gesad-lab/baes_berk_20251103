```markdown
# Course Management System

A web application for managing courses and students, allowing users to create and retrieve course and student information.

## Main Functions

- **Create Student**: Allows users to add new students with their names and email addresses.
- **Read Students**: Fetches a list of existing students from the database.
- **Create Course**: Enables users to create new courses with a name and level.
- **Read Courses**: Retrieves a list of all courses available in the system.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

1. **Initialize the database**:
   The application uses SQLite for database management. The database will be automatically created when the application starts, and the necessary tables will be generated.

2. **Run migrations**:
   To create the Course table and add any necessary fields to the Student table, run the following command:
   ```bash
   alembic upgrade head
   ```

## How to Use the Application

1. **Start the FastAPI server**:
   Run the following command to start the application:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

3. **Creating a Student**:
   - **Endpoint**: `POST /students/`
   - **Request Body**:
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```

4. **Retrieving Students**:
   - **Endpoint**: `GET /students/`
   - This will return a list of all students in the database.

5. **Creating a Course**:
   - **Endpoint**: `POST /courses/`
   - **Request Body**:
     ```json
     {
       "name": "Introduction to Programming",
       "level": "Beginner"
     }
     ```

6. **Retrieving Courses**:
   - **Endpoint**: `GET /courses/`
   - This will return a list of all courses in the database.

## Additional Information

- **CORS Support**: The application allows cross-origin requests, making it suitable for integration with frontend applications.
- **Error Handling**: The application will return appropriate HTTP status codes and messages for various error scenarios.

For further details and advanced usage, please refer to the API documentation available at the `/docs` endpoint.
```