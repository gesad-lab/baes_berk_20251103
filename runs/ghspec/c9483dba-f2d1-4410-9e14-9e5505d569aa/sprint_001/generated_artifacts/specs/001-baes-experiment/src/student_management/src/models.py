# student_management/README.md

# Student Management Web Application

## Overview & Purpose
The purpose of this web application is to provide a platform for managing Student entities. Each Student will have a required `name` field. Users will be able to create and retrieve Student records, with the application automatically setting up the necessary database schema upon startup. This application is designed for educational institutions and developers looking to learn about basic web application concepts.

## User Scenarios
1. **Create a Student**:
   - Users can send a request to create a new Student, providing a name.
   - The application will respond with a confirmation and details of the created Student.

2. **Retrieve a Student**:
   - Users can request the details of a specific Student using their ID.
   - The application will return the Student's details in JSON format.

3. **Validation Scenarios**:
   - If a user tries to create a Student without a name, the application will respond with an error message indicating that the name is required.

## Functional Requirements
1. **Create Student**:
   - **Endpoint**: `POST /students`
   - **Input**: JSON payload containing `name` (string, required).
   - **Output**: JSON response with the created Student's ID and name.

2. **Retrieve Student**:
   - **Endpoint**: `GET /students/{id}`
   - **Input**: Student ID in the URL.
   - **Output**: JSON response with the Student's ID and name.

3. **Database Management**:
   - The application will create the SQLite database schema for Students at startup if it does not exist.

## Application Architecture
- **Type**: RESTful web application
- **Design Pattern**: MVC (Model-View-Controller) for clear separation of concerns.
- **Framework**: Flask (Python) is used as the backend framework due to its lightweight nature and ease of use for RESTful API development.
- **Database**: SQLite is chosen for local development and its simplicity.

## Getting Started
To run the application:

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd student_management
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python src/app.py
   ```

The application will be available at `http://localhost:5000`.

## Testing
- Unit tests for both create and retrieve endpoints are provided in `tests/test_app.py`.
- Ensure a minimum of 70% coverage of functional paths by running the tests with:
   ```bash
   pytest
   ```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.