# Student Management Application

The Student Management Application is aimed at providing a simple interface for creating, reading, and managing student records. Each student will have a mandatory name field. The application will support JSON responses to facilitate integration with other applications or services. The ultimate goal is to offer an efficient, user-friendly, and well-structured way to manage student entities.

## Project Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/student-management-app.git
   cd student-management-app
   ```

2. **Install Dependencies**:
   Use [Poetry](https://python-poetry.org/) to manage the dependencies. If you don't have Poetry installed, you can find the installation instructions [here](https://python-poetry.org/docs/#installation).

   Once Poetry is installed, run:
   ```bash
   poetry install
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the project root and define the following environment variables:
   ```env
   DATABASE_URL=postgresql://<username>:<password>@localhost:5432/student_db
   ```

   Make sure to replace `<username>`, `<password>`, and `student_db` with your PostgreSQL database credentials and the name of the database you want to use.

4. **Run the Application**:
   You can run the application using Docker. First, ensure you have Docker and Docker Compose installed. Then, use the following command:
   ```bash
   docker-compose up --build
   ```

   This will build the containers and start the application along with the PostgreSQL database.

## Usage Instructions

### API Endpoints

1. **Create Student Endpoint**
   - **Request**: POST to `/students`
   - **Required Body**: JSON containing the name of the student (must be a non-empty string).
   - **Response**: JSON containing the created student's ID and name.

   **Example Request**:
   ```json
   {
     "name": "John Doe"
   }
   ```

   **Example Response**:
   ```json
   {
     "id": 1,
     "name": "John Doe"
   }
   ```

2. **Retrieve Student Endpoint**
   - **Request**: GET to `/students/{id}`
   - **Response**: JSON containing the student's ID and name or a 404 error if not found.

3. **List Students Endpoint**
   - **Request**: GET to `/students`
   - **Response**: JSON array containing a list of all students with their IDs and names.

### Testing

1. **Create Student Scenario Testing**: Validate that a POST request with valid data creates a new student in the database.
2. **Retrieve Student Scenario Testing**: Validate that a GET request for a specific student ID returns the correct student information.
3. **List Students Scenario Testing**: Validate that a GET request retrieves a list of all students accurately.

## Database Schema

The application will automatically create a `students` table with the following structure upon startup:
- **id**: Integer, primary key, auto-increment.
- **name**: String, required.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.