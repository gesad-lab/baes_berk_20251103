```markdown
# Course Management System

A simple application for managing courses and students.

## Overview

The Course Management System allows users to create and manage courses with specific attributes. The main functionalities include creating courses with a name and level, while preserving existing student data in the database.

## Main Functions

- **Create Course**: Allows users to create a new course with a name and level.
- **Database Migration**: Updates the database schema to include the new Course table without affecting existing Student data.

## Installation

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
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   alembic
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**:
   Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

3. **Create a Course**:
   Use the `/courses` endpoint to create a new course. You will need to provide the following JSON body:
   ```json
   {
       "name": "Course Name",
       "level": "Course Level"
   }
   ```

4. **Database Migration**:
   To apply the latest changes to the database schema, run the following command:
   ```bash
   alembic upgrade head
   ```
   This will create the `courses` table while preserving existing student data.

## Additional Information

- **Database**: The application uses SQLite for simplicity. The database file will be created in the project directory as `students.db`.
- **Models**: The application defines two models: `Student` and `Course`, where `Course` includes fields for `name` and `level`.
- **Pydantic Schemas**: The application uses Pydantic for request and response validation.

## Support

For any issues or support requests, please contact the development team or refer to the documentation for further assistance.

```
