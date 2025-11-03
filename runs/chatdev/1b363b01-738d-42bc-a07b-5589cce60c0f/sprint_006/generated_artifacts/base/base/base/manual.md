Here's the `manual.md` file for the ChatDev application, detailing the main functions, installation instructions, and usage guidelines.

```markdown
# ChatDev Course Management Application

Welcome to the ChatDev Course Management Application! This software allows you to manage students and courses effectively through a simple API built with FastAPI and SQLAlchemy.

## Main Functions

The application provides the following functionalities:

- **Student Management**:
  - Create new students.
  - Retrieve a list of existing students.

- **Course Management**:
  - Create new courses with specified names and levels.
  - Retrieve a list of existing courses.

## Installation

To get started with the ChatDev application, you'll need to set up your environment and install the required dependencies. Follow these steps:

### Prerequisites

Ensure you have Python 3.7 or higher installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Clone the repository containing the application code:

```bash
git clone https://github.com/your-repo/chatdev.git
cd chatdev
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment for your project to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### Step 4: Run Database Migrations

Before running the application, ensure that the database schema is up to date. The application uses Alembic for database migrations. Run the following command:

```bash
python -m alembic upgrade head
```

## Usage

### Running the Application

To start the application, execute the following command:

```bash
python main.py
```

The application will be accessible at `http://127.0.0.1:8000`.

### API Endpoints

#### Student Endpoints

- **Create a Student**:
  - **Endpoint**: `POST /students`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Retrieve Students**:
  - **Endpoint**: `GET /students`
  - **Response**: Returns a list of students.

#### Course Endpoints

- **Create a Course**:
  - **Endpoint**: `POST /courses`
  - **Request Body**:
    ```json
    {
      "name": "Introduction to Programming",
      "level": "Beginner"
    }
    ```

- **Retrieve Courses**:
  - **Endpoint**: `GET /courses`
  - **Response**: Returns a list of courses.

## Additional Information

For more detailed documentation on FastAPI, SQLAlchemy, and Alembic, please refer to their official documentation:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)

If you encounter any issues or have questions, feel free to reach out to our support team.

Happy coding!
```

This manual provides a comprehensive overview of the application, installation steps, and usage instructions, ensuring users can effectively utilize the software for managing courses and students.