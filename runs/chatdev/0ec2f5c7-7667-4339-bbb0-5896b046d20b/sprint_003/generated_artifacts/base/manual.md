Here's a detailed user manual for the ChatDev Student Application, including installation instructions, main functions, and usage guidelines.

```markdown
# ChatDev Student Application

The ChatDev Student Application is designed to manage student records efficiently. It allows for the creation, retrieval, and management of student data, including the newly added email field for each student.

## Main Functions

- **Create Student**: Add a new student record with a name and email.
- **Retrieve Students**: Fetch a list of all students along with their details.
- **Update Student**: Modify existing student records, including updating the email field.
- **Delete Student**: Remove a student record from the database.

## Quick Install

To set up the ChatDev Student Application, you need to install the required dependencies. You can do this using `pip`:

```bash
pip install -r requirements.txt
```

### Required Dependencies

- **SQLAlchemy**: ORM for database interactions.
- **Pydantic**: For data validation and serialization.
- **sqlite3**: Built-in SQLite database support.
- **FastAPI**: Framework for building APIs.
- **Uvicorn**: ASGI server for running FastAPI applications.

## Setting Up the Environment

1. **Clone the Repository**: 
   Clone the repository containing the ChatDev Student Application code.

   ```bash
   git clone <repository-url>
   cd chatdev_student_app
   ```

2. **Install Dependencies**: 
   Use the command provided above to install all necessary packages.

3. **Run Database Migration**: 
   To add the email field to the Student entity and ensure existing data is preserved, run the migration script.

   ```bash
   python main.py
   ```

## How to Use the Application

1. **Start the Application**: 
   You can start the FastAPI application using Uvicorn. Run the following command in your terminal:

   ```bash
   uvicorn main:app --reload
   ```

   This will start the server and allow you to access the API at `http://127.0.0.1:8000`.

2. **API Endpoints**:
   - **Create Student**: 
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
   - **Update Student**: 
     - **Endpoint**: `PUT /students/{id}`
     - **Request Body**:
       ```json
       {
         "name": "John Doe Updated",
         "email": "john.doe.updated@example.com"
       }
       ```
   - **Delete Student**: 
     - **Endpoint**: `DELETE /students/{id}`

3. **Testing the API**: 
   You can use tools like Postman or curl to test the API endpoints. Make sure to replace `{id}` with the actual student ID when updating or deleting a student.

## Conclusion

The ChatDev Student Application provides a robust solution for managing student records with the added capability of handling email addresses. Follow the installation and usage instructions to get started with the application. For further assistance, please refer to the documentation or reach out to the support team.

```

This manual provides a comprehensive overview of the ChatDev Student Application, ensuring users can easily install, set up, and utilize the software effectively.